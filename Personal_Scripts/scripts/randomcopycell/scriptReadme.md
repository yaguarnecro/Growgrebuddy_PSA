# Random Copy App

## Overview

The Random Copy App is a versatile GUI application built with Python's Tkinter library. It allows users to select either a markdown file or a Google Sheet, extract a table from it, and randomly copy the content from a specified column to the clipboard. This is particularly useful for quickly accessing and using random email content stored in markdown tables or Google Sheets.

## Features

- **File Selection**: Users can select a markdown file containing a table.
- **Google Sheets Integration**: Users can input a Google Sheet URL and sheet name to access content from Google Sheets.
- **Random Content Selection**: The app extracts the table from the chosen source and randomly selects content from the 'Email Content' column.
- **Clipboard Copy**: The selected content is copied to the clipboard for easy pasting elsewhere.
- **Cell Location Information**: The app provides information about which cell (column and row) was selected.

## Requirements

- Python 3.x
- Required Python packages:
  - pandas
  - pyperclip
  - tkinter (usually included with Python)
  - gspread
  - oauth2client

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Install the required packages using pip:
   ```bash
   pip install pandas pyperclip gspread oauth2client
   ```

## Usage

1. Run the script:
   ```bash
   python randomcopycell.py
   ```
2. Choose between "Select Markdown File" or "Use Google Sheet":
   - For Markdown: Click "Select Markdown File" to choose a markdown file.
   - For Google Sheets: Click "Use Google Sheet" and enter the sheet URL and name when prompted.
3. Once a source is selected, click "Random Copy" to copy random content from the 'Email Content' column to the clipboard.
4. A message will confirm if the content was successfully copied and show the cell location.

## Google Sheets Setup

1. Create a Google Cloud project and enable the Google Sheets API.
2. Create a service account and download the JSON key file.
3. Rename the JSON key file to `random-cell-in-column-caam-aa1c8982cf34.json` and place it in the same directory as the script.
4. Share your Google Sheet with the email address in the service account JSON file.

## Error Handling

- If the required modules are not installed, the script will exit with an error message.
- If no table is found in the markdown file or Google Sheet, or if the 'Email Content' column is missing, an error message will be displayed.
- If the clipboard operation fails, a warning will be shown, and the content will be displayed in a message box.
- Permission errors for Google Sheets will be caught and displayed with instructions on how to resolve them.

## Code Structure

- **extract_table_from_md**: Reads a markdown file and extracts the first table found.
- **get_data_from_google_sheet**: Retrieves data from a specified Google Sheet.
- **select_random_email_content**: Selects random content from the 'Email Content' column and copies it to the clipboard.
- **RandomCopyApp**: The main Tkinter application class that handles the GUI and user interactions.

## Logging

The app now includes logging functionality. Logs are written to `randomcopycell.log` in the same directory as the script.

## License

This project is licensed under the MIT License.

## Acknowledgments

- The application uses the Tkinter library for the GUI.
- The pandas library is used for handling table data.
- The pyperclip library is used for clipboard operations.
- The gspread and oauth2client libraries are used for Google Sheets integration.
