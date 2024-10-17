import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def format_prompt_entry(entry):
    """Format a single prompt entry into markdown."""
    return (
        f"## Prompt\n"
        f"* **Description:** {entry.get('description', '---')}\n"
        f"* **Prompt ID:** {entry.get('prompt_id', '---')}\n"
        f"* **Prompt Text:** {entry.get('prompt', '---')}\n"
        f"* **AI Tool:** {entry.get('ai_tool', '---')}\n"
        f"* **Date:** {entry.get('date', '---')}\n"
        f"* **Result Link:** {entry.get('link_to_result', '---')}\n\n"
    )

def generate_prompts_md(conversation, project_name):
    """Generate markdown for prompts based on the conversation and project name."""
    md_content = f"# Prompts - [{project_name}]\n\n"
    for item in conversation:
        md_content += f"## Prompt {item['prompt_id']}\n"
        md_content += f"* **Description:** {item['description']}\n"
        md_content += f"* **Prompt ID:** {item['prompt_id']}\n"
        md_content += f"* **Prompt Text:** {item['prompt']}\n"
        md_content += f"* **AI Tool:** {item['ai_tool']}\n"
        md_content += f"* **Date:** {item['date']}\n"
        md_content += f"* **Result Link:** {item['link_to_result']}\n\n"
    logging.info("Generated prompts markdown.")
    return md_content

def format_result_entry(entry):
    """Format a single result entry into markdown."""
    return (
        f"## Result\n"
        f"* **Result ID:** {entry.get('result_id', '---')}\n"
        f"* **Link to Prompt:** {entry.get('link_to_prompt', '---')}\n"
        f"* **Result Text:** {entry.get('result', '---')}\n"
        f"* **Error Description:** {entry.get('error_description', '---')}\n"
        f"* **Image Link:** {entry.get('image_link', '---')}\n"
        f"* **Code Snippet:** {entry.get('code_snippet', '---')}\n\n"
    )

def generate_results_md(conversation, project_name):
    """Generate markdown for results based on the conversation and project name."""
    md_content = f"# Results - [{project_name}]\n\n"
    for item in conversation:
        md_content += f"## Result {item['result_id']}\n"
        md_content += f"* **Result ID:** {item['result_id']}\n"
        md_content += f"* **Link to Prompt:** {item['link_to_prompt']}\n"
        md_content += f"* **Result Text:** {item['result']}\n"
        md_content += f"* **Error Description:** {item['error_description']}\n"
        md_content += f"* **Image Link:** {item['image_link']}\n"
        md_content += f"* **Code Snippet:** {item['code_snippet']}\n\n"
    logging.info("Generated results markdown.")
    return md_content

def parse_prompts(prompts_text):
    # This function should parse the prompts_text and return a list of dictionaries
    # For now, return a dummy list for demonstration
    return [{
        'description': 'Sample description',
        'prompt_id': '1',
        'prompt': 'Sample prompt',
        'ai_tool': 'Sample AI Tool',
        'date': '2023-10-01',
        'link_to_result': 'http://example.com/result'  # Ensure this key is included
    }]

def process_input(prompt, response):
    """Process the input data and return a structured format."""
    if not prompt or not response:
        logging.error("Error: Both prompt and response fields must be filled.")  # Log error message
        return None  # Prevent further processing

    # Example processing logic
    processed_data = [{'description': response, 'prompt_id': '1', 'prompt': prompt}]
    logging.info("Processing input data...")
    return processed_data
