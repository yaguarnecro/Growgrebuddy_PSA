import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox, ttk
import os
import uuid

# Define placeholders for templates
prompt_placeholders = [
    "[Project Stage]", "[prompt description]", "[Prompt text]", "[AI Tool used]", "[Date the prompt was executed]", "[Link to Result]"
]
result_placeholders = [
    "[Error description]", "[Link to Prompt]", "[result text]", "[Extra info]", "[Image link]", "[Code snippet]"
]

# Initialize the main window
root = tk.Tk()
root.title("Markdown Generator")

# Initialize UI elements
input_text_prompts = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
input_text_results = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)

# Function to parse prompts (dummy implementation)
def parse_prompts(prompts_text):
    # This function should parse the prompts_text and return a list of dictionaries
    # For now, return a dummy list for demonstration
    return [{'description': 'Sample description', 'prompt_id': '1', 'prompt': 'Sample prompt', 'ai_tool': 'Sample AI Tool', 'date': '2023-10-01'}]

# Function to generate prompts markdown
def generate_prompts_md(conversation, project_stage):
    prompts_md = f"# Prompts - [{project_stage}]\n\n"
    for i, entry in enumerate(conversation, start=1):
        prompts_md += f"## Prompt {i}\n"
        prompts_md += f"* **Description:** {entry.get('description', '---')}\n"
        prompts_md += f"* **Prompt ID:** {entry.get('prompt_id', '---')}\n"
        prompts_md += f"* **Prompt Text:** {entry.get('prompt', '---')}\n"
        prompts_md += f"* **AI Tool:** {entry.get('ai_tool', '---')}\n"
        prompts_md += f"* **Date:** {entry.get('date', '---')}\n"
        prompts_md += f"* **Result Link:** {entry.get('link_to_result', '---')}\n\n"
    return prompts_md

# Function to generate results markdown
def generate_results_md(conversation, project_stage):
    results_md = f"# Results - [{project_stage}]\n\n"
    for i, entry in enumerate(conversation, start=1):
        results_md += f"## Result {i}\n"
        results_md += f"* **Result ID:** {entry.get('result_id', '---')}\n"
        results_md += f"* **Link to Prompt:** {entry.get('link_to_prompt', '---')}\n"
        results_md += f"* **Result Text:** {entry.get('result', '---')}\n"
        results_md += f"* **Error Description:** {entry.get('error_description', '---')}\n"
        results_md += f"* **Image Link:** {entry.get('image_link', '---')}\n"
        results_md += f"* **Code Snippet:** {entry.get('code_snippet', '---')}\n\n"
    return results_md

# Function to process input
def process_input():
    # Disable the UI
    process_button.config(state=tk.DISABLED)
    input_text_prompts.config(state=tk.DISABLED)
    input_text_results.config(state=tk.DISABLED)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, "Processing text...\n")

    # Initialize variables
    prompts_text = input_text_prompts.get("1.0", tk.END).strip()
    results_text = input_text_results.get("1.0", tk.END).strip()
    found_values_prompts = []
    not_found_values_prompts = []
    found_values_results = []
    not_found_values_results = []

    # Ask user to select a folder
    folder_selected = filedialog.askdirectory()
    if not folder_selected:
        messagebox.showerror("Error", "No folder selected.")
        return

    # Define the template placeholders
    prompt_placeholders = ["[Prompt text]"]
    result_placeholders = ["[result text]"]

    # Check if the input is empty
    if not prompts_text or not results_text:
        output_text.insert(tk.END, "Error: Prompts or Results cannot be empty.\n", 'red')
        return

    # Example logic to determine found and not found values
    if "[Prompt text]" in prompts_text:
        found_values_prompts.append("[Prompt text]")
    else:
        not_found_values_prompts.extend(prompt_placeholders)

    if "[result text]" in results_text:
        found_values_results.append("[result text]")
    else:
        not_found_values_results.extend(result_placeholders)

    # Assign values to variables
    project_stage = os.path.basename(folder_selected)
    link_to_result = f"{project_stage}_t_prompts.md"
    prompt_text = prompts_text if "[Prompt text]" in prompts_text else "---"
    result_text = results_text if "[result text]" in results_text else "---"

    # Generate markdown content
    prompts_md = generate_prompts_md(parse_prompts(prompts_text), project_stage)
    results_md = generate_results_md(parse_prompts(results_text), project_stage)

    # Save markdown files with unique identifiers
    prompts_file_path = os.path.join(folder_selected, f"{project_stage}_t_prompts_{uuid.uuid4().hex[:8]}.md")
    results_file_path = os.path.join(folder_selected, f"{project_stage}_t_promptsresults_{uuid.uuid4().hex[:8]}.md")

    with open(prompts_file_path, 'w') as f:
        f.write(prompts_md)

    with open(results_file_path, 'w') as f:
        f.write(results_md)

    # Log the found values
    output_text.insert(tk.END, "\n**Values Found in Prompts:**\n", 'bold')
    for value in found_values_prompts:
        output_text.insert(tk.END, f"- {value}\n", 'green')

    output_text.insert(tk.END, "\n**Values Not Found in Prompts:**\n", 'bold')
    for value in not_found_values_prompts:
        output_text.insert(tk.END, f"- {value}\n", 'red')

    output_text.insert(tk.END, "\n**Values Found in Results:**\n", 'bold')
    for value in found_values_results:
        output_text.insert(tk.END, f"- {value}\n", 'green')

    output_text.insert(tk.END, "\n**Values Not Found in Results:**\n", 'bold')
    for value in not_found_values_results:
        output_text.insert(tk.END, f"- {value}\n", 'red')

    # Log file save locations
    output_text.insert(tk.END, f"\nPrompts saved to {prompts_file_path}\n", 'blue')
    output_text.insert(tk.END, f"Results saved to {results_file_path}\n", 'blue')

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
