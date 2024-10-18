import os
import sys
import traceback
import tkinter as tk
from tkinter import filedialog, messagebox
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import random
import pyperclip
import logging
import json

# Add this function to get the correct path to the JSON file
def get_credentials_path():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, 'random-cell-in-column-caam-aa1c8982cf34.json')

def authenticate_google_sheets(credentials_file):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
    client = gspread.authorize(creds)
    return client

def get_data_from_google_sheet(sheet_url, sheet_name):
    try:
        credentials_path = get_credentials_path()
        client = authenticate_google_sheets(credentials_path)
        sheet = client.open_by_url(sheet_url).worksheet(sheet_name)
        data = sheet.get_all_records()
        return pd.DataFrame(data)
    except gspread.exceptions.SpreadsheetNotFound:
        raise ValueError(f"Spreadsheet not found. Please check the URL: {sheet_url}")
    except gspread.exceptions.WorksheetNotFound:
        raise ValueError(f"Worksheet '{sheet_name}' not found in the spreadsheet.")
    except (gspread.exceptions.APIError, PermissionError) as e:
        with open(get_credentials_path(), 'r') as f:
            creds = json.load(f)
        service_account_email = creds['client_email']
        error_message = (
            f"The service account doesn't have permission to access this sheet. "
            f"Please share the sheet with {service_account_email}\n"
            f"Steps to share the sheet:\n"
            f"1. Open the Google Sheet at {sheet_url}\n"
            f"2. Click the 'Share' button in the top-right corner\n"
            f"3. In the 'Add people and groups' field, paste this email: {service_account_email}\n"
            f"4. Set the role to 'Editor' or 'Viewer' as needed\n"
            f"5. Click 'Send' to grant access\n"
            f"After sharing, try running the script again."
        )
        raise PermissionError(error_message)
    except Exception as e:
        raise ValueError(f"An unexpected error occurred: {str(e)}")

def extract_table_from_md(md_file):
    def read_file_with_encoding(file_path, encoding='utf-8'):
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                return file.read()
        except UnicodeDecodeError:
            with open(file_path, 'r', encoding='latin-1') as file:
                return file.read()

    content = read_file_with_encoding(md_file)
    table_start = content.find('|')
    table_end = content.rfind('|')
    if table_start == -1 or table_end == -1:
        raise ValueError("No table found in the markdown file")

    table_content = content[table_start:table_end+1]
    rows = [row.strip() for row in table_content.split('\n') if row.strip()]

    if len(rows) > 1 and all(c in '|-:' for c in rows[1].replace('|', '')):
        rows.pop(1)

    data = []
    headers = [header.strip() for header in rows[0].split('|')[1:-1] if header.strip()]
    
    current_row = []
    for row in rows[1:]:
        cells = [cell.strip() for cell in row.split('|')[1:-1]]
        if len(cells) >= len(headers):
            if current_row:
                data.append(current_row)
            current_row = cells[:len(headers)]
        elif cells:
            if current_row:
                current_row[-1] += '\n' + ' '.join(cells)
            else:
                continue
    
    if current_row:
        data.append(current_row)

    data = [row + [''] * (len(headers) - len(row)) for row in data]
    return pd.DataFrame(data, columns=headers)

def select_random_email_content(data_source, is_google_sheet=False, sheet_url=None, sheet_name=None):
    if is_google_sheet:
        df = get_data_from_google_sheet(sheet_url, sheet_name)
    else:
        df = extract_table_from_md(data_source)

    if 'Email Content' not in df.columns:
        raise ValueError("The 'Email Content' column was not found in the table")

    df = df.dropna(subset=['Email Content'])
    
    if df.empty:
        raise ValueError("No valid email content found in the table")

    random_row = random.randint(0, len(df) - 1)
    random_email_content = df.iloc[random_row]['Email Content']
    random_email_content = '\n'.join(line.strip() for line in random_email_content.split('\n') if line.strip())
    
    try:
        pyperclip.copy(random_email_content)
    except pyperclip.PyperclipException:
        return f"Failed to copy to clipboard. Content: {random_email_content}", None, None

    column_index = df.columns.get_loc('Email Content')
    return random_email_content, column_index + 1, random_row + 2  # +2 because spreadsheet rows start at 1 and we have a header row

class RandomCopyApp:
    def __init__(self, master):
        self.master = master
        master.title("Random Copy App")
        master.geometry("300x200")

        self.file_path = None
        self.is_google_sheet = False
        self.sheet_url = None
        self.sheet_name = None

        self.select_file_button = tk.Button(master, text="Select Markdown File", command=self.select_file)
        self.select_file_button.pack(pady=5)

        self.google_sheet_button = tk.Button(master, text="Use Google Sheet", command=self.use_google_sheet)
        self.google_sheet_button.pack(pady=5)

        self.random_copy_button = tk.Button(master, text="Random Copy", command=self.random_copy, state=tk.DISABLED)
        self.random_copy_button.pack(pady=10)

        self.status_label = tk.Label(master, text="No file or sheet selected", wraplength=280)
        self.status_label.pack(pady=10)

    def select_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Markdown files", "*.md")])
        if self.file_path:
            self.is_google_sheet = False
            self.status_label.config(text=f"Selected file: {os.path.basename(self.file_path)}")
            self.random_copy_button.config(state=tk.NORMAL)
        else:
            self.status_label.config(text="No file selected")
            self.random_copy_button.config(state=tk.DISABLED)

    def use_google_sheet(self):
        self.is_google_sheet = True
        self.file_path = None
        self.prompt_google_sheet_info()
        if self.sheet_url and self.sheet_name:
            self.status_label.config(text=f"Using Google Sheet: {self.sheet_name}")
            self.random_copy_button.config(state=tk.NORMAL)
        else:
            self.status_label.config(text="Google Sheet info not provided")
            self.random_copy_button.config(state=tk.DISABLED)

    def prompt_google_sheet_info(self):
        dialog = tk.Toplevel(self.master)
        dialog.title("Google Sheet Information")
        dialog.geometry("300x150")

        tk.Label(dialog, text="Sheet URL:").pack(pady=5)
        url_entry = tk.Entry(dialog, width=40)
        url_entry.pack(pady=5)

        tk.Label(dialog, text="Sheet Name:").pack(pady=5)
        name_entry = tk.Entry(dialog, width=40)
        name_entry.pack(pady=5)

        def save_info():
            self.sheet_url = url_entry.get().strip()
            self.sheet_name = name_entry.get().strip()
            dialog.destroy()

        tk.Button(dialog, text="Save", command=save_info).pack(pady=10)

        dialog.transient(self.master)
        dialog.grab_set()
        self.master.wait_window(dialog)

    def random_copy(self):
        try:
            logging.info("Starting random_copy operation")
            if self.is_google_sheet:
                if not self.sheet_url or not self.sheet_name:
                    raise ValueError("Google Sheet URL or name is missing")
                logging.info(f"Using Google Sheet: URL={self.sheet_url}, Name={self.sheet_name}")
                content, column, row = select_random_email_content(None, is_google_sheet=True, sheet_url=self.sheet_url, sheet_name=self.sheet_name)
            else:
                logging.info(f"Using Markdown file: {self.file_path}")
                content, column, row = select_random_email_content(self.file_path)

            if content.startswith("Failed to copy to clipboard"):
                self.status_label.config(text="Content retrieved but not copied to clipboard")
                messagebox.showwarning("Warning", content)
                logging.warning(content)
                print("Warning:", content, file=sys.stderr)
            else:
                location_info = f"Selected from column {column}, row {row}"
                self.status_label.config(text=f"Random content copied to clipboard! {location_info}")
                messagebox.showinfo("Success", f"Copied content:\n\n{content}\n\n{location_info}")
                logging.info(f"Successfully copied content to clipboard. {location_info}")
                print(f"Success: Random content copied to clipboard! {location_info}")
        except PermissionError as e:
            error_message = str(e)
            self.status_label.config(text="Permission error. Check the error message for details.")
            messagebox.showerror("Permission Error", error_message)
            logging.error(error_message)
            print(error_message, file=sys.stderr)
        except Exception as e:
            error_message = f"Unexpected error: {str(e)}"
            traceback_message = traceback.format_exc()
            self.status_label.config(text=error_message)
            error_details = f"{error_message}\n\nTraceback:\n{traceback_message}"
            messagebox.showerror("Unexpected Error", error_details)
            logging.error(error_details)
            print(error_details, file=sys.stderr)
        
        # Additional debugging information
        print("Debug Information:")
        print(f"Is Google Sheet: {self.is_google_sheet}")
        print(f"File Path: {self.file_path}")
        print(f"Sheet URL: {self.sheet_url}")
        print(f"Sheet Name: {self.sheet_name}")
        
        # Check if the credentials file exists
        credentials_path = get_credentials_path()
        if os.path.exists(credentials_path):
            print(f"Credentials file exists at: {credentials_path}")
        else:
            print(f"Credentials file not found at: {credentials_path}")

# Add this function at the beginning of your script
def setup_logging():
    logging.basicConfig(filename='randomcopycell.log', level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s')

# Modify the __main__ section at the end of your script
if __name__ == "__main__":
    setup_logging()
    try:
        root = tk.Tk()
        app = RandomCopyApp(root)
        root.mainloop()
    except Exception as e:
        logging.critical(f"Critical error in main: {str(e)}\n{traceback.format_exc()}")
        print(f"Critical error: {str(e)}", file=sys.stderr)
