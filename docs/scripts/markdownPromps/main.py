import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox
import tkinter.font as tkfont
import logging
from markdown_generator import generate_prompts_md, generate_results_md
from utils import process_input as utils_process_input
from file_operations import get_next_filename, save_markdown_files
import os

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class MarkdownGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Markdown Generator")
        self.geometry("800x600")
        self.configure(bg='#2b2b2b')

        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        self.configure_styles()

        self.create_widgets()
        self.create_layout()
        self.create_bindings()

    def configure_styles(self):
        self.style.configure('TLabel', background='#2b2b2b', foreground='white')
        self.style.configure('TButton', background='#4a4a4a', foreground='white')
        self.style.map('TButton', background=[('active', '#5a5a5a')])
        self.style.configure('TFrame', background='#2b2b2b')

    def create_widgets(self):
        self.main_frame = ttk.Frame(self)
        
        self.instructions = ttk.Label(self.main_frame, text="Use '§§§' to create multiple entries", wraplength=300)
        
        self.prompts_frame = ttk.LabelFrame(self.main_frame, text="Prompts")
        self.results_frame = ttk.LabelFrame(self.main_frame, text="Results")

        prompt_placeholder = "Enter your prompt here...\n§§§\nYou can add more prompts like this"
        result_placeholder = "Enter your response here...\n§§§\nYou can add more responses like this"

        self.input_text_prompts = TableText(self.prompts_frame, is_prompt=True, placeholder_text=prompt_placeholder, width=40, height=10)
        self.input_text_results = TableText(self.results_frame, is_prompt=False, placeholder_text=result_placeholder, width=40, height=10)

        self.process_button = ttk.Button(self.main_frame, text="Process", command=self.handle_input)
        self.process_button.state(['disabled'])

        self.output_text = scrolledtext.ScrolledText(self.main_frame, wrap=tk.WORD, width=80, height=10, bg='#1e1e1e', fg='white')
        self.output_text.tag_configure("error", foreground="red")
        self.output_text.tag_configure("info", foreground="lightblue")
        self.output_text.tag_configure("success", foreground="lightgreen")

        self.log_frame = ttk.LabelFrame(self.main_frame, text="Log")
        self.log_text = scrolledtext.ScrolledText(self.log_frame, wrap=tk.WORD, width=80, height=5, bg='#1e1e1e', fg='white')
        self.log_text.tag_configure("file", foreground="yellow")
        self.log_text.tag_configure("found", foreground="lightgreen")
        self.log_text.tag_configure("not_found", foreground="red")

        self.toggle_log_button = ttk.Button(self.main_frame, text="Show Log", command=self.toggle_log)

        self.status_bar = ttk.Label(self, text="Ready", anchor=tk.W)

    def create_layout(self):
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.instructions.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        self.prompts_frame.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        self.results_frame.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

        self.input_text_prompts.pack(fill=tk.BOTH, expand=True)
        self.input_text_results.pack(fill=tk.BOTH, expand=True)

        self.process_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.output_text.grid(row=3, column=0, columnspan=2, pady=10, sticky="nsew")

        self.toggle_log_button.grid(row=4, column=0, columnspan=2, pady=(0, 5))
        self.log_frame.grid(row=5, column=0, columnspan=2, pady=5, sticky="nsew")
        self.log_text.pack(fill=tk.BOTH, expand=True)

        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.rowconfigure(1, weight=1)
        self.main_frame.rowconfigure(3, weight=1)
        self.main_frame.rowconfigure(5, weight=1)

    def create_bindings(self):
        self.input_text_prompts.bind("<KeyRelease>", self.update_identifiers)
        self.input_text_results.bind("<KeyRelease>", self.check_fields)

    def update_identifiers(self, event=None):
        self.input_text_results.identifiers = self.input_text_prompts.identifiers
        self.input_text_results.update_rows()  # Update the rows to reflect the new identifiers
        self.check_fields(event)

    def toggle_log(self):
        if self.log_frame.winfo_viewable():
            self.log_frame.grid_remove()
            self.toggle_log_button.config(text="Show Log")
        else:
            self.log_frame.grid()
            self.toggle_log_button.config(text="Hide Log")

    def check_fields(self, event=None):
        prompt_text = self.input_text_prompts.get("1.0", tk.END).strip()
        response_text = self.input_text_results.get("1.0", tk.END).strip()
        prompt_empty = prompt_text == '' or prompt_text == self.input_text_prompts.placeholder_text
        response_empty = response_text == '' or response_text == self.input_text_results.placeholder_text

        if not prompt_empty and not response_empty:
            self.process_button.state(['!disabled'])
        else:
            self.process_button.state(['disabled'])

    def handle_input(self):
        """Process the input from the user and generate markdown files."""
        try:
            # Disable the UI
            self.process_button.state(['disabled'])
            self.input_text_prompts.config(state=tk.DISABLED)
            self.input_text_results.config(state=tk.DISABLED)
            self.output_text.config(state=tk.NORMAL)
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, "Processing...\n", 'info')
            self.output_text.config(state=tk.DISABLED)
            self.update()  # Force update of the UI

            # Get the input text
            prompts_text = self.input_text_prompts.get("1.0", tk.END).strip()
            results_text = self.input_text_results.get("1.0", tk.END).strip()

            # Remove placeholder text if present
            if prompts_text == self.input_text_prompts.placeholder_text:
                prompts_text = ""
            if results_text == self.input_text_results.placeholder_text:
                results_text = ""

            # Validate input fields
            if not prompts_text or not results_text:
                raise ValueError("Both prompt and response fields must be filled.")

            # Ask for output directory
            output_directory = filedialog.askdirectory(title="Select Output Directory")
            if not output_directory:
                raise ValueError("No output directory selected. Process aborted.")

            # Use the name of the selected folder as the project name
            project_name = os.path.basename(output_directory)

            # Process the input text
            identifiers = [row['identifier']['text'] for row in self.input_text_results.rows if row['identifier']['text'] != "○"]
            # Ensure we have at least one identifier
            if not identifiers:
                identifiers = ['1']
            conversation = utils_process_input(prompts_text, results_text, identifiers)
            if not conversation:
                raise ValueError("Failed to process input. Please check your prompts and results.")

            # Check the number of prompts and responses
            prompt_count = len(prompts_text.split('\n§§§\n'))
            response_count = len(results_text.split('\n§§§\n'))

            # Generate markdown
            prompts_markdown = generate_prompts_md(conversation, project_name)
            results_markdown = generate_results_md(conversation, project_name)

            # Get unique filenames
            prompts_filename = get_next_filename("prompts", output_directory)
            results_filename = get_next_filename("results", output_directory)

            # Save markdown files
            prompts_file_path, results_file_path = save_markdown_files(
                prompts_markdown, 
                results_markdown, 
                output_directory, 
                project_name,
                prompts_filename,
                results_filename
            )

            # Display success message
            self.output_text.config(state=tk.NORMAL)
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, "Success: ", 'success')
            self.output_text.insert(tk.END, "Markdown files generated successfully.\n", 'info')
            self.output_text.insert(tk.END, f"Prompts file: {prompts_file_path}\n", 'info')
            self.output_text.insert(tk.END, f"Results file: {results_file_path}\n", 'info')
            self.output_text.insert(tk.END, f"Number of prompts: {prompt_count}\n", 'info')
            self.output_text.insert(tk.END, f"Number of responses: {response_count}\n", 'info')
            self.output_text.insert(tk.END, f"Number of entries generated: {len(conversation)}\n", 'info')
            self.output_text.config(state=tk.DISABLED)

            # Update log with detailed information
            self.update_log(prompts_file_path, results_file_path, conversation)

            # Show a success message box
            messagebox.showinfo("Success", "Markdown files generated successfully!")

        except ValueError as ve:
            # Display error message in output text area
            self.output_text.config(state=tk.NORMAL)
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, "Error: ", 'error')
            self.output_text.insert(tk.END, f"{str(ve)}\n", 'info')
            self.output_text.config(state=tk.DISABLED)

            # Show an error message box
            messagebox.showerror("Error", str(ve))

        except Exception as e:
            # Display unexpected error message in output text area
            self.output_text.config(state=tk.NORMAL)
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, "Unexpected Error: ", 'error')
            self.output_text.insert(tk.END, f"{str(e)}\n", 'info')
            self.output_text.config(state=tk.DISABLED)

            # Log the error
            logging.error(f"Unexpected error: {str(e)}")
            logging.error(f"Error details: ", exc_info=True)  # This will log the full traceback

            # Show an error message box
            messagebox.showerror("Unexpected Error", f"An unexpected error occurred: {str(e)}")

        finally:
            # Re-enable the UI
            self.process_button.state(['!disabled'])
            self.input_text_prompts.config(state=tk.NORMAL)
            self.input_text_results.config(state=tk.NORMAL)

    def update_log(self, prompts_file_path, results_file_path, conversation):
        self.log_text.config(state=tk.NORMAL)
        self.log_text.delete(1.0, tk.END)
        
        self.log_text.insert(tk.END, "Created Files:\n", "file")
        self.log_text.insert(tk.END, f"Prompts file: {prompts_file_path}\n", "file")
        self.log_text.insert(tk.END, f"Results file: {results_file_path}\n\n", "file")

        self.log_text.insert(tk.END, "Found Values:\n", "found")
        for item in conversation:
            for key, value in item.items():
                if value:
                    self.log_text.insert(tk.END, f"{key}: {value}\n", "found")
    
        self.log_text.insert(tk.END, "\nNot Found Values:\n", "not_found")
        for item in conversation:
            for key, value in item.items():
                if not value:
                    self.log_text.insert(tk.END, f"{key}\n", "not_found")

        self.log_text.config(state=tk.DISABLED)

class TableText(tk.Frame):
    def __init__(self, master, is_prompt=True, placeholder_text="", **kwargs):
        super().__init__(master, bg='white')
        self.is_prompt = is_prompt
        self.placeholder_text = placeholder_text.split('\n')
        self.placeholder_visible = True
        
        self.checkbox_frame = tk.Frame(self, width=30, bg='white')
        self.separator_frame = tk.Frame(self, width=30, bg='white')
        self.identifier_frame = tk.Frame(self, width=30, bg='white')
        self.text_frame = tk.Frame(self, bg='white')

        self.checkbox_frame.pack(side=tk.LEFT, fill=tk.Y)
        self.separator_frame.pack(side=tk.LEFT, fill=tk.Y)
        self.identifier_frame.pack(side=tk.LEFT, fill=tk.Y)
        self.text_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.text = tk.Text(self.text_frame, wrap="word", bg='white', **kwargs)
        self.vsb = tk.Scrollbar(self.text_frame, orient="vertical", command=self.text.yview)
        self.text.configure(yscrollcommand=self.vsb.set)

        self.text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.vsb.pack(side=tk.RIGHT, fill=tk.Y)

        self.rows = []
        self.identifiers = ['1']  # Initialize with at least one identifier
        self.add_row()  # Start with one row

        self.text.bind("<FocusIn>", self.on_focus_in)
        self.text.bind("<FocusOut>", self.on_focus_out)
        self.text.bind("<KeyRelease>", self.on_text_change)
        self.text.bind("<<Paste>>", self.on_paste)
        self.text.bind("<Configure>", self.update_row_heights)
        self.text.bind("<Return>", self.on_enter)
        self.text.bind("<Shift-Return>", self.on_shift_enter)

        self.show_placeholder()

    def show_placeholder(self):
        self.text.delete("1.0", tk.END)
        for i, line in enumerate(self.placeholder_text):
            self.text.insert(f"{i+1}.0", line + '\n')
        self.text.config(fg='grey')
        self.placeholder_visible = True
        self.update_rows()

    def on_focus_in(self, event):
        if self.placeholder_visible:
            self.text.delete("1.0", tk.END)
            self.text.config(fg='black')
            self.placeholder_visible = False
            self.update_rows()

    def on_focus_out(self, event):
        if not self.text.get("1.0", tk.END).strip():
            self.show_placeholder()

    def add_row(self):
        row_index = len(self.rows)
        checkbox_var = tk.BooleanVar()
        checkbox = tk.Checkbutton(self.checkbox_frame, variable=checkbox_var, bg='white', command=lambda: self.checkbox_clicked(row_index))
        separator = tk.Button(self.separator_frame, text="§§§", bg='white', command=lambda: self.insert_separator(row_index))
        if self.is_prompt:
            identifier = tk.Label(self.identifier_frame, text=str(row_index+1), bg="darkgray", fg="white")
            if str(row_index+1) not in self.identifiers:
                self.identifiers.append(str(row_index+1))
        else:
            identifier = tk.Button(self.identifier_frame, text="○", bg='white', command=lambda i=row_index: self.show_dropdown(i))
        
        border = tk.Frame(self.identifier_frame, bg='gray', width=2)
        
        checkbox.pack(side=tk.TOP, anchor=tk.W, fill=tk.X)
        separator.pack(side=tk.TOP, anchor=tk.W, fill=tk.X)
        identifier.pack(side=tk.TOP, anchor=tk.W, fill=tk.X)
        border.pack(side=tk.TOP, fill=tk.X)
        
        self.rows.append({
            'checkbox': checkbox,
            'checkbox_var': checkbox_var,
            'separator': separator,
            'identifier': identifier,
            'border': border
        })

    def update_rows(self):
        content = self.text.get("1.0", "end-1c")
        lines = content.split('\n')
        
        # Add or remove rows as needed
        while len(self.rows) < len(lines):
            self.add_row()
        while len(self.rows) > len(lines):
            self.remove_row()
        
        # Update identifiers for prompt section
        if self.is_prompt:
            self.identifiers = [str(i+1) for i in range(len(lines))]
            if not self.identifiers:  # Ensure there's always at least one identifier
                self.identifiers = ['1']
        
        # Show/hide rows based on content
        for i, line in enumerate(lines):
            self.rows[i]['checkbox'].pack()
            self.rows[i]['separator'].pack()
            self.rows[i]['identifier'].pack()
            self.rows[i]['border'].pack(fill=tk.X)
            
            if "§§§" in line:
                self.rows[i]['border'].config(bg='black')
            else:
                self.rows[i]['border'].config(bg='gray')
            
            if self.is_prompt:
                self.rows[i]['identifier'].config(text=str(i+1))
        
        self.update_row_heights()

    def on_text_change(self, event=None):
        if not self.placeholder_visible:
            self.update_rows()

    def on_enter(self, event):
        if not self.placeholder_visible:
            current_index = self.text.index(tk.INSERT)
            line, column = map(int, current_index.split('.'))
            
            # Insert a newline
            self.text.insert(f"{line}.end", "\n")
            
            # Insert "§§§" on the next line
            self.text.insert(f"{line+1}.0", "§§§")
            
            # Insert another newline
            self.text.insert(f"{line+1}.end", "\n")
            
            # Move cursor to the start of the new empty line
            self.text.mark_set(tk.INSERT, f"{line+2}.0")
            
            self.update_rows()
        return "break"

    def on_shift_enter(self, event):
        if not self.placeholder_visible:
            self.text.insert(tk.INSERT, "\n")
            self.update_rows()
        return "break"

    def remove_row(self):
        if self.rows:
            row = self.rows.pop()
            row['checkbox'].destroy()
            row['separator'].destroy()
            row['identifier'].destroy()
            row['border'].destroy()

    def update_row_heights(self, event=None):
        font = tkfont.Font(font=self.text['font'])
        line_height = font.metrics()['linespace']
        for i, row in enumerate(self.rows):
            row_content = self.text.get(f"{i+1}.0", f"{i+1}.end")
            num_lines = max(1, len(row_content.split('\n')))
            height = line_height * num_lines
            
            row['checkbox'].configure(height=height)
            row['separator'].configure(height=height)
            row['identifier'].configure(height=height)
            row['border'].configure(height=2)  # Keep border height constant

    def checkbox_clicked(self, row_index):
        if self.rows[row_index]['checkbox_var'].get():
            self.rows[row_index]['separator'].pack()
        else:
            self.rows[row_index]['separator'].pack_forget()

    def insert_separator(self, row_index):
        current_line = self.text.get(f"{row_index+1}.0", f"{row_index+1}.end")
        if not current_line.endswith("§§§"):
            # Insert a newline if we're not at the end of the line
            if self.text.get(f"{row_index+1}.end") != "\n":
                self.text.insert(f"{row_index+1}.end", "\n")
            
            # Insert "§§§" on the next line
            self.text.insert(f"{row_index+2}.0", "§§§")
            
            # Insert another newline
            self.text.insert(f"{row_index+2}.end", "\n")
            
            # Move cursor to the start of the new empty line
            self.text.mark_set(tk.INSERT, f"{row_index+3}.0")
        
        self.rows[row_index]['checkbox_var'].set(False)
        self.rows[row_index]['separator'].pack_forget()
        self.on_text_change()

    def show_dropdown(self, row_index):
        if self.is_prompt:
            return  # Do nothing for prompt section
        
        # Create a toplevel window for the dropdown
        dropdown = tk.Toplevel(self)
        dropdown.overrideredirect(True)
        dropdown.geometry(f"+{self.winfo_rootx() + self.rows[row_index]['identifier'].winfo_x()}+{self.winfo_rooty() + self.rows[row_index]['identifier'].winfo_y() + self.rows[row_index]['identifier'].winfo_height()}")
        
        # Create a listbox with identifiers
        listbox = tk.Listbox(dropdown)
        listbox.pack(fill=tk.BOTH, expand=True)
        
        for identifier in self.identifiers:
            listbox.insert(tk.END, identifier)
        
        def on_select(event):
            if listbox.curselection():  # Check if an item is selected
                selection = listbox.get(listbox.curselection())
                self.rows[row_index]['identifier'].config(text=selection)
            dropdown.destroy()
        
        listbox.bind('<<ListboxSelect>>', on_select)
        
        # If the listbox is empty, show a message
        if listbox.size() == 0:
            listbox.insert(tk.END, "No identifiers available")
            listbox.config(state=tk.DISABLED)

    def get(self, *args, **kwargs):
        return self.text.get(*args, **kwargs)

    def insert(self, *args, **kwargs):
        self.text.insert(*args, **kwargs)
        self.on_text_change()

    def delete(self, *args, **kwargs):
        self.text.delete(*args, **kwargs)
        self.on_text_change()

    def bind(self, *args, **kwargs):
        self.text.bind(*args, **kwargs)

    def config(self, **kwargs):
        self.text.config(**kwargs)

    def configure(self, **kwargs):
        self.config(**kwargs)

    def on_paste(self, event):
        self.after(10, self.on_text_change)  # Schedule on_text_change to run after the paste is complete

if __name__ == "__main__":
    app = MarkdownGeneratorApp()
    app.mainloop()