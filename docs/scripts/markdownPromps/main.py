import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
import os
import logging
from markdown_generator import generate_prompts_md, generate_results_md  # Import the functions
from utils import parse_prompts  # Import the parse_prompts function
from file_operations import save_markdown_files
from ui import create_ui
import threading

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize the main window
root = tk.Tk()
root.title("Markdown Generator")

# Initialize UI elements
input_text_prompts = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
input_text_results = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)

def process_input():
    """Process the input from the user and generate markdown files."""
    try:
        # Disable the UI
        process_button.config(state=tk.DISABLED)
        input_text_prompts.config(state=tk.DISABLED)
        input_text_results.config(state=tk.DISABLED)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Processing text...\n")

        # Initialize variables
        prompts_text = input_text_prompts.get("1.0", tk.END).strip()
        results_text = input_text_results.get("1.0", tk.END).strip()

        # Ask user to select a folder
        folder_selected = filedialog.askdirectory()
        if not folder_selected:
            messagebox.showerror("Error", "No folder selected.")
            logging.error("No folder selected by the user.")
            return

        # Validate inputs
        if not prompts_text or not results_text:
            output_text.insert(tk.END, "Error: Prompts or Results cannot be empty.\n", 'red')
            logging.warning("Empty prompts or results provided.")
            return

        # Generate markdown content
        project_stage = os.path.basename(folder_selected)
        prompts_md = generate_prompts_md(parse_prompts(prompts_text), project_stage)
        results_md = generate_results_md(parse_prompts(results_text), project_stage)

        # Save markdown files
        prompts_file_path, results_file_path = save_markdown_files(prompts_md, results_md, folder_selected, project_stage)

        # Log file save locations
        output_text.insert(tk.END, f"\nPrompts saved to {prompts_file_path}\n", 'blue')
        output_text.insert(tk.END, f"Results saved to {results_file_path}\n", 'blue')
        logging.info(f"Markdown files saved: {prompts_file_path}, {results_file_path}")

    except Exception as e:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"Error: {str(e)}\n")
        logging.error(f"An error occurred: {str(e)}")

    finally:
        # Re-enable the UI
        input_text_prompts.config(state=tk.NORMAL)
        input_text_results.config(state=tk.NORMAL)
        process_button.config(state=tk.NORMAL)

# Add UI elements to the window
input_text_prompts.pack()
input_text_results.pack()
output_text.pack()

# Add a button to process input
process_button = tk.Button(root, text="Process", command=process_input)
process_button.pack()

# Start the GUI event loop
root.mainloop()

# Define the main function
def main():
    # Your main code logic here
    pass  # Replace with actual code

if __name__ == "__main__":
    main()
