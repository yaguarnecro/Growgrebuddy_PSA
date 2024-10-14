import os
import uuid
import re

def get_next_filename(base_name, folder_selected):
    """Get the next available filename by checking existing files in the directory.

    Args:
        base_name (str): The base name of the file (without extension).
        folder_selected (str): The folder where files will be saved.

    Returns:
        str: The next available filename.
    """
    existing_files = os.listdir(folder_selected)
    pattern = re.compile(rf"^{base_name}(\d+)?\.md$")
    max_number = 0

    for file in existing_files:
        match = pattern.match(file)
        if match:
            number = match.group(1)
            if number:
                max_number = max(max_number, int(number))
            else:
                # If there's a file without a number suffix, treat it as the highest
                max_number = max(max_number, 1)

    return f"{base_name}{max_number + 1}.md"

def save_markdown_files(prompts_md, results_md, folder_selected, project_stage):
    """Save the generated markdown files to the specified folder.

    Args:
        prompts_md (str): The markdown content for prompts.
        results_md (str): The markdown content for results.
        folder_selected (str): The folder where files will be saved.
        project_stage (str): The current stage of the project.

    Returns:
        tuple: Paths of the saved prompts and results markdown files.
    """
    prompts_base_name = "prompts"
    results_base_name = "results"

    prompts_file_name = get_next_filename(prompts_base_name, folder_selected)
    results_file_name = get_next_filename(results_base_name, folder_selected)

    prompts_file_path = os.path.join(folder_selected, prompts_file_name)
    results_file_path = os.path.join(folder_selected, results_file_name)

    with open(prompts_file_path, 'w') as f:
        f.write(prompts_md)

    with open(results_file_path, 'w') as f:
        f.write(results_md)

    return prompts_file_path, results_file_path
