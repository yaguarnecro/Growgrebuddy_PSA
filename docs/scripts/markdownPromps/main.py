import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox
import tkinter.font as tkfont
import logging
from markdown_generator import generate_prompts_md, generate_results_md
from utils import process_input as utils_process_input
from file_operations import get_next_filename, save_markdown_files
import os
import re

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Add TableText class definition
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
        
        while len(self.rows) < len(lines):
            self.add_row()
        while len(self.rows) > len(lines):
            self.remove_row()
        
        if self.is_prompt:
            self.identifiers = [str(i+1) for i in range(len(lines))]
            if not self.identifiers:
                self.identifiers = ['1']
        
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
            
            self.text.insert(f"{line}.end", "\n")
            self.text.insert(f"{line+1}.0", "§§§")
            self.text.insert(f"{line+1}.end", "\n")
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
            row['border'].configure(height=2)

    def checkbox_clicked(self, row_index):
        if self.rows[row_index]['checkbox_var'].get():
            self.rows[row_index]['separator'].pack()
        else:
            self.rows[row_index]['separator'].pack_forget()

    def insert_separator(self, row_index):
        current_line = self.text.get(f"{row_index+1}.0", f"{row_index+1}.end")
        if not current_line.endswith("§§§"):
            if self.text.get(f"{row_index+1}.end") != "\n":
                self.text.insert(f"{row_index+1}.end", "\n")
            
            self.text.insert(f"{row_index+2}.0", "§§§")
            self.text.insert(f"{row_index+2}.end", "\n")
            self.text.mark_set(tk.INSERT, f"{row_index+3}.0")
        
        self.rows[row_index]['checkbox_var'].set(False)
        self.rows[row_index]['separator'].pack_forget()
        self.on_text_change()

    def show_dropdown(self, row_index):
        if self.is_prompt:
            return
        
        dropdown = tk.Toplevel(self)
        dropdown.overrideredirect(True)
        dropdown.geometry(f"+{self.winfo_rootx() + self.rows[row_index]['identifier'].winfo_x()}+{self.winfo_rooty() + self.rows[row_index]['identifier'].winfo_y() + self.rows[row_index]['identifier'].winfo_height()}")
        
        listbox = tk.Listbox(dropdown)
        listbox.pack(fill=tk.BOTH, expand=True)
        
        for identifier in self.identifiers:
            listbox.insert(tk.END, identifier)
        
        def on_select(event):
            if listbox.curselection():
                selection = listbox.get(listbox.curselection())
                self.rows[row_index]['identifier'].config(text=selection)
            dropdown.destroy()
        
        listbox.bind('<<ListboxSelect>>', on_select)
        
        if listbox.size() == 0:
            listbox.insert(tk.END, "No identifiers available")
            listbox.config(state=tk.DISABLED)

    def on_paste(self, event):
        self.after(10, self.on_text_change)

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

class InputTab(ttk.Frame):
    def __init__(self, master, is_single_entry=True, on_text_change=None):
        super().__init__(master)
        self.is_single_entry = is_single_entry
        self.on_text_change = on_text_change
        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        if self.is_single_entry:
            self.prompts_frame = ttk.LabelFrame(self, text="Prompt")
            self.results_frame = ttk.LabelFrame(self, text="Result")
            self.input_text_prompts = scrolledtext.ScrolledText(self.prompts_frame, wrap=tk.WORD, width=40, height=10)
            self.input_text_results = scrolledtext.ScrolledText(self.results_frame, wrap=tk.WORD, width=40, height=10)
            
            self.input_text_prompts.bind("<KeyRelease>", self.text_changed)
            self.input_text_results.bind("<KeyRelease>", self.text_changed)
        else:
            self.instructions = ttk.Label(self, text="Use '§§§' to create multiple entries", wraplength=300)
            self.prompts_frame = ttk.LabelFrame(self, text="Prompts")
            self.results_frame = ttk.LabelFrame(self, text="Results")
            prompt_placeholder = "Enter your prompt here...\n§§§\nYou can add more prompts like this"
            result_placeholder = "Enter your response here...\n§§§\nYou can add more responses like this"
            self.input_text_prompts = TableText(self.prompts_frame, is_prompt=True, placeholder_text=prompt_placeholder, width=40, height=10)
            self.input_text_results = TableText(self.results_frame, is_prompt=False, placeholder_text=result_placeholder, width=40, height=10)
            
            self.input_text_prompts.text.bind("<KeyRelease>", self.text_changed)
            self.input_text_results.text.bind("<KeyRelease>", self.text_changed)

    def create_layout(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

        if not self.is_single_entry:
            self.instructions.grid(row=0, column=0, columnspan=2, pady=(0, 10))
        self.prompts_frame.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        self.results_frame.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        self.input_text_prompts.pack(fill=tk.BOTH, expand=True)
        self.input_text_results.pack(fill=tk.BOTH, expand=True)

    def text_changed(self, event=None):
        if self.on_text_change:
            self.on_text_change()

class ControlPanel(tk.Frame):
    def __init__(self, master, process_command, toggle_log_command):
        super().__init__(master, bg='#2b2b2b')
        print("Initializing ControlPanel")
        self.create_widgets(process_command, toggle_log_command)
        self.create_layout()

    def create_widgets(self, process_command, toggle_log_command):
        self.process_button = tk.Button(self, text="Process", command=process_command, 
                                        bg='#4a4a4a', fg='white', activebackground='#5a5a5a')
        self.toggle_log_button = tk.Button(self, text="Show Log", command=toggle_log_command,
                                           bg='#4a4a4a', fg='white', activebackground='#5a5a5a')
        self.progress_bar = ttk.Progressbar(self, orient=tk.HORIZONTAL, length=200, mode='indeterminate')

    def create_layout(self):
        self.process_button.pack(side=tk.LEFT, padx=(0, 10))
        self.toggle_log_button.pack(side=tk.LEFT)
        self.progress_bar.pack(side=tk.LEFT, padx=(10, 0))

class OutputPanel(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.output_text = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=80, height=10, bg='#1e1e1e', fg='white')
        self.output_text.tag_configure("error", foreground="red")
        self.output_text.tag_configure("info", foreground="lightblue")
        self.output_text.tag_configure("success", foreground="lightgreen")

        self.log_frame = ttk.LabelFrame(self, text="Log")
        self.log_text = scrolledtext.ScrolledText(self.log_frame, wrap=tk.WORD, width=80, height=5, bg='#1e1e1e', fg='white')
        self.log_text.tag_configure("file", foreground="yellow")
        self.log_text.tag_configure("found", foreground="lightgreen")
        self.log_text.tag_configure("not_found", foreground="red")

    def create_layout(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.output_text.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.log_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        self.log_text.pack(fill=tk.BOTH, expand=True)

def read_ai_tools(file_path):
    ai_tools = ["Pick an AI tool"]
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line.startswith('##'):
                    ai_tools.append(line.strip('# \n'))
    except FileNotFoundError:
        print(f"Warning: AI tools file not found at {file_path}")
    return ai_tools

class MarkdownGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Markdown Generator")
        self.geometry("1000x800")
        self.configure(bg='#2b2b2b')

        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        self.configure_styles()

        self.selected_folder = None
        
        # Initialize AI tool variables
        self.ai_tool = tk.StringVar()
        self.ai_tool.set("Pick an AI tool")
        self.ai_tools = read_ai_tools("docs/aiPrompts/templates/[AI Tool used].md")

        self.create_widgets()
        print("Widgets created successfully")
        self.create_layout()
        print("Layout created successfully")
        self.create_bindings()
        print("Bindings created successfully")

        # Force update of the window
        self.update_idletasks()
        self.update()

    def configure_styles(self):
        self.style.configure('TLabel', background='#2b2b2b', foreground='white')
        self.style.configure('TButton', background='#4a4a4a', foreground='white')
        self.style.map('TButton', background=[('active', '#5a5a5a')])
        self.style.configure('TFrame', background='#2b2b2b')

    def create_widgets(self):
        # AI Tool Dropdown
        self.ai_tool_dropdown = ttk.Combobox(self, textvariable=self.ai_tool, values=self.ai_tools, state="readonly")

        # Folder placeholder
        self.folder_placeholder = ttk.Label(self, text="Folder...", anchor=tk.W)

        # Notebook (tabs)
        self.notebook = ttk.Notebook(self)
        self.single_entry_tab = InputTab(self.notebook, is_single_entry=True, on_text_change=self.enable_process_button)
        self.multiple_entry_tab = InputTab(self.notebook, is_single_entry=False, on_text_change=self.enable_process_button)
        self.notebook.add(self.single_entry_tab, text="Single Entry")
        self.notebook.add(self.multiple_entry_tab, text="Multiple Entry")

        # Control Panel
        self.control_panel = ControlPanel(self, self.handle_input, self.toggle_log)

        # Output Panel
        self.output_panel = OutputPanel(self)

        # Status Bar
        self.status_bar = ttk.Label(self, text="Ready", anchor=tk.W)

        # Initial check to enable/disable process button
        self.enable_process_button()

    def create_layout(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=0)  # Changed from 1 to 0
        self.grid_rowconfigure(4, weight=1)

        # AI Tool Dropdown
        self.ai_tool_dropdown.grid(row=0, column=0, sticky="nw", padx=10, pady=(10, 0))

        # Folder placeholder
        self.folder_placeholder.grid(row=1, column=0, sticky="nw", padx=10, pady=(10, 0))

        # Notebook (tabs)
        self.notebook.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

        # Control Panel
        self.control_panel.grid(row=3, column=0, sticky="ew", padx=10, pady=(0, 10))

        # Output Panel
        self.output_panel.grid(row=4, column=0, sticky="nsew", padx=10, pady=(0, 10))

        # Status Bar
        self.status_bar.grid(row=5, column=0, sticky="ew", padx=10, pady=(0, 10))

    def enable_process_button(self):
        current_tab = self.notebook.index(self.notebook.select())
        if current_tab == 0:  # Single Entry tab
            prompts = self.single_entry_tab.input_text_prompts.get("1.0", tk.END).strip()
            results = self.single_entry_tab.input_text_results.get("1.0", tk.END).strip()
        else:  # Multiple Entry tab
            prompts = self.multiple_entry_tab.input_text_prompts.get("1.0", tk.END).strip()
            results = self.multiple_entry_tab.input_text_results.get("1.0", tk.END).strip()

        if prompts and results:
            self.control_panel.process_button.config(state=tk.NORMAL)
        else:
            self.control_panel.process_button.config(state=tk.DISABLED)

        # Force update to ensure changes are visible
        self.update_idletasks()

    def handle_input(self):
        try:
            if not self.selected_folder:
                self.selected_folder = filedialog.askdirectory(title="Select Output Folder")
                if not self.selected_folder:
                    messagebox.showinfo("Info", "Folder selection cancelled. Please select a folder to continue.")
                    return
                self.update_folder_display()

            # Get the current tab
            current_tab = self.notebook.index(self.notebook.select())
            if current_tab == 0:  # Single Entry tab
                prompts_text = self.single_entry_tab.input_text_prompts.get("1.0", tk.END).strip()
                results_text = self.single_entry_tab.input_text_results.get("1.0", tk.END).strip()
            else:  # Multiple Entry tab
                prompts_text = self.multiple_entry_tab.input_text_prompts.get("1.0", tk.END).strip()
                results_text = self.multiple_entry_tab.input_text_results.get("1.0", tk.END).strip()

            # Get the selected AI tool
            selected_ai_tool = self.ai_tool.get()
            if selected_ai_tool == "Pick an AI tool":
                selected_ai_tool = "Not specified"

            # Process the input
            self.control_panel.progress_bar.start()
            self.status_bar.config(text="Processing...")
            self.update_idletasks()

            conversation = utils_process_input(prompts_text, results_text, ['1'], selected_ai_tool)
            if not conversation:
                raise ValueError("Failed to process input. Please check your prompts and results.")

            # Generate markdown
            prompts_markdown = generate_prompts_md(conversation, os.path.basename(self.selected_folder))
            results_markdown = generate_results_md(conversation, os.path.basename(self.selected_folder))

            # Get unique filenames
            prompts_filename = get_next_filename("prompts", self.selected_folder)
            results_filename = get_next_filename("results", self.selected_folder)

            # Save markdown files
            prompts_file_path, results_file_path = save_markdown_files(
                prompts_markdown, 
                results_markdown, 
                self.selected_folder, 
                os.path.basename(self.selected_folder),
                prompts_filename,
                results_filename
            )

            self.control_panel.progress_bar.stop()
            self.status_bar.config(text="Ready")

            # Display success message
            success_message = f"Markdown files generated successfully.\n"
            success_message += f"Prompts file: {prompts_file_path}\n"
            success_message += f"Results file: {results_file_path}\n"
            messagebox.showinfo("Success", success_message)

            # Update output panel
            self.output_panel.output_text.config(state=tk.NORMAL)
            self.output_panel.output_text.delete("1.0", tk.END)
            self.output_panel.output_text.insert(tk.END, success_message, "success")
            self.output_panel.output_text.config(state=tk.DISABLED)

        except Exception as e:
            self.control_panel.progress_bar.stop()
            self.status_bar.config(text="Error occurred")
            error_message = f"An error occurred: {str(e)}\n\nError type: {type(e).__name__}"
            logging.error(f"Error in handle_input: {error_message}", exc_info=True)
            messagebox.showerror("Error", error_message)
            
            # Update output panel with error message
            self.output_panel.output_text.config(state=tk.NORMAL)
            self.output_panel.output_text.delete("1.0", tk.END)
            self.output_panel.output_text.insert(tk.END, error_message, "error")
            self.output_panel.output_text.config(state=tk.DISABLED)

        finally:
            self.control_panel.process_button.config(state=tk.DISABLED)

    def update_folder_display(self):
        if self.selected_folder:
            folder_name = os.path.basename(self.selected_folder)
            display_text = f"{folder_name}...>"
            self.folder_placeholder.config(
                text=display_text,
                foreground="green",
                font=("TkDefaultFont", 10, "bold"),
                cursor="hand2"
            )
            self.folder_placeholder.bind("<Button-1>", self.select_new_folder)

    def select_new_folder(self, event=None):
        new_folder = filedialog.askdirectory(title="Select Output Folder")
        if new_folder:
            self.selected_folder = new_folder
            self.update_folder_display()

    def create_bindings(self):
        # Add your bindings here
        pass  # Remove this 'pass' statement when you add actual bindings

    def toggle_log(self):
        if self.output_panel.log_frame.winfo_viewable():
            self.output_panel.log_frame.grid_remove()
            self.control_panel.toggle_log_button.config(text="Show Log")
        else:
            self.output_panel.log_frame.grid()
            self.control_panel.toggle_log_button.config(text="Hide Log")

if __name__ == "__main__":
    app = MarkdownGeneratorApp()
    app.mainloop()