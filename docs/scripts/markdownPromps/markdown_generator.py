def generate_prompts_md(conversation, project_stage):
    """Generate markdown for prompts based on the conversation and project stage.

    Args:
        conversation (list): A list of dictionaries containing prompt details.
        project_stage (str): The current stage of the project.

    Returns:
        str: A formatted markdown string for the prompts.
    """
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

def generate_results_md(conversation, project_stage):
    """Generate markdown for results based on the conversation and project stage.

    Args:
        conversation (list): A list of dictionaries containing result details.
        project_stage (str): The current stage of the project.

    Returns:
        str: A formatted markdown string for the results.
    """
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
