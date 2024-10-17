import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

def create_ui(root, process_input):
    input_text_prompts = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
    input_text_results = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
    output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)

    input_text_prompts.pack(pady=10)
    input_text_results.pack(pady=10)
    output_text.pack(pady=10)

    # Set output text area to read-only
    output_text.config(state=tk.DISABLED)

    # Create process button and set it to disabled by default
    process_button = tk.Button(root, text="Process", command=lambda: on_process_button_click(input_text_prompts, input_text_results, output_text, process_input))
    process_button.pack(pady=5)
    process_button.config(state=tk.DISABLED)  # Ensure button is disabled by default

    # Function to check if prompt and response fields are empty
    def check_fields(event=None):
        prompt_empty = not input_text_prompts.get("1.0", tk.END).strip()  # Check if prompt is empty
        response_empty = not input_text_results.get("1.0", tk.END).strip()  # Check if response is empty

        if not prompt_empty and not response_empty:
            process_button.config(state=tk.NORMAL)  # Enable button
        else:
            process_button.config(state=tk.DISABLED)  # Disable button

    # Bind the check_fields function to the key release event
    input_text_prompts.bind("<KeyRelease>", check_fields)
    input_text_results.bind("<KeyRelease>", check_fields)

    # Initial check to disable button if fields are empty
    check_fields()

    return input_text_prompts, input_text_results, output_text, process_button

def on_process_button_click(input_text_prompts, input_text_results, output_text, process_input):
    prompt = input_text_prompts.get("1.0", tk.END).strip()  # Get the prompt input from the UI
    response = input_text_results.get("1.0", tk.END).strip()  # Get the response input from the UI

    # Check if both fields are empty
    if not prompt and not response:
        messagebox.showerror("Input Error", "Both prompt and response fields must be filled.")
        return  # Prevent further processing

    # Check if prompt is empty
    if not prompt:
        messagebox.showerror("Input Error", "Prompt field must be filled.")
        return  # Prevent further processing

    # Check if response is empty
    if not response:
        messagebox.showerror("Input Error", "Response field must be filled.")
        return  # Prevent further processing

    # Proceed with processing if validation passes
    processed_data = process_input(prompt, response)
    if processed_data is None:
        messagebox.showerror("Processing Error", "An error occurred during processing.")
    else:
        output_text.config(state=tk.NORMAL)  # Enable output text area for updating
        output_text.delete("1.0", tk.END)  # Clear the output text box
        output_text.insert(tk.END, processed_data)  # Insert the processed data into the output text box
        output_text.config(state=tk.DISABLED)  # Disable it again to make it read-only

# Example of how to run the application
if __name__ == "__main__":
    root = tk.Tk()
    create_ui(root, lambda prompt, response: f"Processed: {prompt} | {response}")  # Example process_input function
    root.mainloop()
