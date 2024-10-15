import unittest
import sys
import os
import logging
from unittest.mock import patch

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from markdown_generator import generate_prompts_md, generate_results_md  # Removed process_input

class TestMarkdownGenerator(unittest.TestCase):

    @patch('logging.info')
    def test_generate_prompts_md(self, mock_logging_info):
        conversation = [
            {
                'description': 'Test description',
                'prompt_id': '1',
                'prompt': 'Test prompt',
                'ai_tool': 'Test AI Tool',
                'date': '2023-10-01',
                'link_to_result': 'http://example.com/result'
            }
        ]
        project_stage = "Test Stage"
        expected_output = "# Prompts - [Test Stage]\n\n## Prompt 1\n"
        expected_output += "* **Description:** Test description\n"
        expected_output += "* **Prompt ID:** 1\n"
        expected_output += "* **Prompt Text:** Test prompt\n"
        expected_output += "* **AI Tool:** Test AI Tool\n"
        expected_output += "* **Date:** 2023-10-01\n"
        expected_output += "* **Result Link:** http://example.com/result\n\n"

        self.assertEqual(generate_prompts_md(conversation, project_stage), expected_output)
        mock_logging_info.assert_called_with("Generated prompts markdown.")

    def test_generate_prompts_md_missing_link(self):
        conversation = [
            {
                'description': 'Test description',
                'prompt_id': '1',
                'prompt': 'Test prompt',
                'ai_tool': 'Test AI',
                'date': '2023-10-01'
                # Missing 'link_to_result'
            }
        ]
        project_stage = "Test Stage"
        expected_output = "# Prompts - [Test Stage]\n\n## Prompt 1\n"
        expected_output += "* **Description:** Test description\n"
        expected_output += "* **Prompt ID:** 1\n"
        expected_output += "* **Prompt Text:** Test prompt\n"
        expected_output += "* **AI Tool:** Test AI\n"
        expected_output += "* **Date:** 2023-10-01\n"
        expected_output += "* **Result Link:** ---\n\n"  # Default value
        
        self.assertEqual(generate_prompts_md(conversation, project_stage), expected_output)

    def test_generate_results_md(self):
        conversation = [
            {
                'result_id': '1',
                'link_to_prompt': 'http://example.com',
                'result': 'Test result',
                'error_description': 'No error',
                'image_link': 'http://example.com/image.png',
                'code_snippet': 'print("Hello World")'
            }
        ]
        project_stage = "Test Stage"
        expected_output = "# Results - [Test Stage]\n\n## Result 1\n"
        expected_output += "* **Result ID:** 1\n"
        expected_output += "* **Link to Prompt:** http://example.com\n"
        expected_output += "* **Result Text:** Test result\n"
        expected_output += "* **Error Description:** No error\n"
        expected_output += "* **Image Link:** http://example.com/image.png\n"
        expected_output += "* **Code Snippet:** print(\"Hello World\")\n\n"
        
        self.assertEqual(generate_results_md(conversation, project_stage), expected_output)

    def test_generate_results_md_missing_link(self):
        conversation = [
            {
                'result_id': '1',
                'result': 'Test result',
                'error_description': 'No error',
                # Missing 'link_to_prompt'
                'image_link': 'http://example.com/image.png',
                'code_snippet': 'print("Hello World")'
            }
        ]
        project_stage = "Test Stage"
        expected_output = "# Results - [Test Stage]\n\n## Result 1\n"
        expected_output += "* **Result ID:** 1\n"
        expected_output += "* **Link to Prompt:** ---\n"  # Default value
        expected_output += "* **Result Text:** Test result\n"
        expected_output += "* **Error Description:** No error\n"
        expected_output += "* **Image Link:** http://example.com/image.png\n"
        expected_output += "* **Code Snippet:** print(\"Hello World\")\n\n"
        
        self.assertEqual(generate_results_md(conversation, project_stage), expected_output)

if __name__ == '__main__':
    unittest.main()
