import unittest
from markdown_generator import generate_prompts_md, generate_results_md

class TestMarkdownGenerator(unittest.TestCase):

    def test_generate_prompts_md(self):
        conversation = [
            {
                'description': 'Test description',
                'prompt_id': '1',
                'prompt': 'Test prompt',
                'ai_tool': 'Test AI',
                'date': '2023-10-01',
                'link_to_result': 'http://example.com'
            }
        ]
        project_stage = "Test Stage"
        expected_output = "# Prompts - [Test Stage]\n\n## Prompt 1\n* **Description:** Test description\n* **Prompt ID:** 1\n* **Prompt Text:** Test prompt\n* **AI Tool:** Test AI\n* **Date:** 2023-10-01\n* **Result Link:** http://example.com\n\n"
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
        expected_output = "# Results - [Test Stage]\n\n## Result 1\n* **Result ID:** 1\n* **Link to Prompt:** http://example.com\n* **Result Text:** Test result\n* **Error Description:** No error\n* **Image Link:** http://example.com/image.png\n* **Code Snippet:** print(\"Hello World\")\n\n"
        self.assertEqual(generate_results_md(conversation, project_stage), expected_output)

if __name__ == '__main__':
    unittest.main()
