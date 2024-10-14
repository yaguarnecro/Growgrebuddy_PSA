import unittest
from utils import parse_prompts

class TestUtils(unittest.TestCase):

    def test_parse_prompts(self):
        prompts_text = "Sample prompt"
        expected_output = [{'description': 'Sample description', 'prompt_id': '1', 'prompt': 'Sample prompt', 'ai_tool': 'Sample AI Tool', 'date': '2023-10-01'}]
        self.assertEqual(parse_prompts(prompts_text), expected_output)

if __name__ == '__main__':
    unittest.main()
