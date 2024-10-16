import os
import re
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def get_next_filename(base_name, folder):
    """Get the next available filename by checking existing files in the directory."""
    pattern = re.compile(rf"{base_name}(\d+)?\.md")
    existing_files = [f for f in os.listdir(folder) if pattern.match(f)]
    
    if not existing_files:
        return f"{base_name}1.md"
    
    numbers = [int(pattern.match(f).group(1) or 0) for f in existing_files]
    next_number = max(numbers) + 1
    return f"{base_name}{next_number}.md"

def save_markdown_files(prompts_md, results_md, folder_selected, project_stage, prompts_filename, results_filename):
    """Save the generated markdown files to the specified folder."""
    try:
        prompts_file_path = os.path.join(folder_selected, prompts_filename)
        results_file_path = os.path.join(folder_selected, results_filename)

        with open(prompts_file_path, 'w', encoding='utf-8') as f:
            f.write(prompts_md)
        logging.info(f"Saved prompts markdown to {prompts_file_path}")

        with open(results_file_path, 'w', encoding='utf-8') as f:
            f.write(results_md)
        logging.info(f"Saved results markdown to {results_file_path}")

        return prompts_file_path, results_file_path
    except Exception as e:
        logging.error(f"Error saving markdown files: {e}")
        raise
