import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
import threading

# Function to generate prompts markdown
def generate_prompts_md(conversation):
    prompts_md = "# Prompts - [Project Stage]\n\n"
    for i, entry in enumerate(conversation, start=1):
        prompts_md += f"## Prompt {i}\n"
        prompts_md += f"* {entry['description']}\n"
        prompts_md += f"* **Prompt:** \n* {entry['prompt']}\n"
        prompts_md += f"* **AI:** {entry['ai_tool']}\n"
        prompts_md += f"* **Date:** {entry['date']}\n"
        prompts_md += f"* **Result:** [Link to Result](path/to/t_promptresults.md#result-title-{i})\n\n"
    return prompts_md

# Function to generate results markdown
def generate_results_md(conversation):
    results_md = "# Results - [Project Stage]\n\n"
    for i, entry in enumerate(conversation, start=1):
        results_md += f"## Result {i}\n"
        results_md += f"* [Error description]\n"
        results_md += f"* **Prompt:**  [Link to Prompt](path/to/t_prompts.md#prompt-title-{i})\n"
        results_md += f"* **result:** \n* {entry['result']}\n"
        results_md += f"* **Extra info**\n* [Image link]\n* [Code snippet]\n\n"
    return results_md

# Function to process the input text
def process_input():
    # Disable the UI
    process_button.config(state=tk.DISABLED)
    input_text.config(state=tk.DISABLED)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, "Processing...\n")

    # Get the input text
    text = input_text.get("1.0", tk.END).strip()
    conversation = []

    # Ask for output directory
    output_directory = filedialog.askdirectory(title="Select Output Directory")
    if not output_directory:
        output_text.insert(tk.END, "No output directory selected. Process aborted.\n")
        process_button.config(state=tk.NORMAL)
        input_text.config(state=tk.NORMAL)
        return

    # Simulate processing the input text
    try:
        # Here you would parse the input text into the conversation structure
        lines = text.splitlines()
        for line in lines:
            if line.strip():  # Skip empty lines
                conversation.append({
                    "description": "Description of the result or its significance.",
                    "prompt": line.strip(),
                    "ai_tool": "ChatGPT",
                    "date": "2023-10-01",
                    "result": f"Processed result for: {line.strip()}"
                })

        # Generate markdown
        prompts_markdown = generate_prompts_md(conversation)
        results_markdown = generate_results_md(conversation)

        # Write to files in the selected output directory
        with open(f'{output_directory}/t_prompts.md', 'w') as f:
            f.write(prompts_markdown)

        with open(f'{output_directory}/t_promptsresults.md', 'w') as f:
            f.write(results_markdown)

        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Markdown files generated successfully.\n")

    except Exception as e:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"Error: {str(e)}\n")

    finally:
        # Re-enable the UI
        process_button.config(state=tk.NORMAL)
        input_text.config(state=tk.NORMAL)

# Create the main window
root = tk.Tk()
root.title("AI Conversation Markdown Generator")

# Create a text area for input
input_text = scrolledtext.ScrolledText(root, width=60, height=10)
input_text.pack(pady=10)

# Create a process button
process_button = tk.Button(root, text="Process", command=lambda: threading.Thread(target=process_input).start())
process_button.pack(pady=5)

# Create a text area for output
output_text = scrolledtext.ScrolledText(root, width=60, height=10)
output_text.pack(pady=10)

# Start the GUI event loop
root.mainloop()