import os
import sys
import traceback
import tkinter as tk
from tkinter import filedialog, messagebox
from io import StringIO  # Add this import

try:
    import pandas as pd
    import random
    import pyperclip
except ImportError as e:
    print(f"Error importing required modules: {e}")
    print("Please ensure you have installed all required packages.")
    sys.exit(1)

def extract_table_from_md(md_file):
    """
    Function to read a markdown file and extract the first table found.
    """
    def read_file_with_encoding(file_path, encoding='utf-8'):
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                return file.read()
        except UnicodeDecodeError:
            with open(file_path, 'r', encoding='latin-1') as file:
                return file.read()

    content = read_file_with_encoding(md_file)

    # Find the table in the content
    table_start = content.find('|')
    table_end = content.rfind('|')
    if table_start == -1 or table_end == -1:
        raise ValueError("No table found in the markdown file")

    table_content = content[table_start:table_end+1]

    # Split the table into rows
    rows = [row.strip() for row in table_content.split('\n') if row.strip()]

    # Remove the header separator line
    if len(rows) > 1 and all(c in '|-:' for c in rows[1].replace('|', '')):
        rows.pop(1)

    # Parse the table
    data = []
    headers = [header.strip() for header in rows[0].split('|')[1:-1] if header.strip()]
    print(f"Debug: Headers found: {headers}")  # Debug print
    
    current_row = []
    for row in rows[1:]:
        cells = [cell.strip() for cell in row.split('|')[1:-1]]
        if len(cells) >= len(headers):
            if current_row:
                data.append(current_row)
            current_row = cells[:len(headers)]  # Ensure we don't exceed the number of headers
        elif cells:  # Check if cells is not empty
            # This is a continuation of the previous row
            if current_row:
                current_row[-1] += '\n' + ' '.join(cells)
            else:
                # If we encounter content before the first valid row, skip it
                continue
    
    if current_row:
        data.append(current_row)

    # Ensure all rows have the same number of columns as headers
    data = [row + [''] * (len(headers) - len(row)) for row in data]

    df = pd.DataFrame(data, columns=headers)
    print(f"Debug: DataFrame columns: {df.columns}")  # Debug print
    print(f"Debug: DataFrame shape: {df.shape}")  # Debug print
    return df

def select_random_email_content(md_file):
    df = extract_table_from_md(md_file)

    if 'Email Content' not in df.columns:
        print(f"Debug: Columns in DataFrame: {df.columns}")  # Debug print
        raise ValueError("The 'Email Content' column was not found in the table")

    df = df.dropna(subset=['Email Content'])
    email_contents = df['Email Content'].tolist()
    
    if not email_contents:
        print(f"Debug: Email contents: {email_contents}")  # Debug print
        raise ValueError("No valid email content found in the table")

    random_email_content = random.choice(email_contents)
    
    # Remove any leading/trailing whitespace and extra newlines
    random_email_content = '\n'.join(line.strip() for line in random_email_content.split('\n') if line.strip())
    
    try:
        pyperclip.copy(random_email_content)
    except pyperclip.PyperclipException:
        return f"Failed to copy to clipboard. Content: {random_email_content}"
    
    return random_email_content

class RandomCopyApp:
    def __init__(self, master):
        self.master = master
        master.title("Random Copy App")
        master.geometry("300x150")

        self.file_path = None

        self.select_file_button = tk.Button(master, text="Select File", command=self.select_file)
        self.select_file_button.pack(pady=10)

        self.random_copy_button = tk.Button(master, text="Random Copy", command=self.random_copy, state=tk.DISABLED)
        self.random_copy_button.pack(pady=10)

        self.status_label = tk.Label(master, text="No file selected", wraplength=280)
        self.status_label.pack(pady=10)

    def select_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Markdown files", "*.md")])
        if self.file_path:
            self.status_label.config(text=f"Selected file: {os.path.basename(self.file_path)}")
            self.random_copy_button.config(state=tk.NORMAL)
        else:
            self.status_label.config(text="No file selected")
            self.random_copy_button.config(state=tk.DISABLED)

    def random_copy(self):
        try:
            content = select_random_email_content(self.file_path)
            if content.startswith("Failed to copy to clipboard"):
                self.status_label.config(text="Content retrieved but not copied to clipboard")
                messagebox.showwarning("Warning", content)
            else:
                self.status_label.config(text="Random content copied to clipboard!")
                messagebox.showinfo("Success", f"Copied content:\n\n{content}")
        except ValueError as e:
            self.status_label.config(text=f"Error: {str(e)}")
            messagebox.showerror("Error", str(e))
        except Exception as e:
            self.status_label.config(text=f"Unexpected error: {str(e)}")
            messagebox.showerror("Unexpected Error", f"{str(e)}\n\nTraceback:\n{traceback.format_exc()}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RandomCopyApp(root)
    root.mainloop()
