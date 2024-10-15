import uuid
from datetime import datetime

def parse_prompts(prompts_text):
    """Parse the prompts text and return a list of dictionaries."""
    prompts = []
    entries = prompts_text.split('\n§§§\n')
    
    for prompt_id, entry in enumerate(entries, start=1):
        lines = entry.strip().split('\n')
        prompt = '\n'.join(lines)
        
        prompts.append({
            'description': 'User provided prompt',
            'prompt_id': str(prompt_id),
            'prompt': prompt,
            'ai_tool': 'Not specified',
            'date': datetime.now().strftime("%Y-%m-%d"),
            'link_to_result': f'#result-{prompt_id}',
            'error_description': '',
            'image_link': '',
            'code_snippet': ''
        })
    
    return prompts

def process_input(prompt, response, identifiers):
    """Process the input data and return a structured format."""
    if not prompt or not response:
        return None  # Prevent further processing if either field is empty

    prompts = parse_prompts(prompt)
    responses = response.split('\n§§§\n')  # Use the same separator for responses
    
    conversation = []
    
    # Ensure we have at least as many identifiers as responses
    while len(identifiers) < len(responses):
        identifiers.append(str(max(int(i) for i in identifiers)))

    for i, resp in enumerate(responses):
        prompt = prompts[i] if i < len(prompts) else prompts[-1]
        result_id = identifiers[i] if i < len(identifiers) else identifiers[-1]
        
        conversation.append({
            **prompt,
            'result': resp.strip(),
            'result_id': result_id,
            'link_to_result': f"#result-{result_id}",
            'link_to_prompt': f"#prompt-{prompt['prompt_id']}"
        })
    
    return conversation
