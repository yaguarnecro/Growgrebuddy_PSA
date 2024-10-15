import unittest
import os
import sys

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from file_operations import save_markdown_files, get_next_filename

class TestFileOperations(unittest.TestCase):

    def setUp(self):
        self.folder_selected = "test_folder"
        if not os.path.exists(self.folder_selected):
            os.makedirs(self.folder_selected)

    def tearDown(self):
        for file in os.listdir(self.folder_selected):
            os.remove(os.path.join(self.folder_selected, file))
        os.rmdir(self.folder_selected)

    def test_get_next_filename_no_files(self):
        base_name = "test_file"
        next_filename = get_next_filename(base_name, self.folder_selected)
        self.assertEqual(next_filename, "test_file1.md")

    def test_get_next_filename_with_existing_files(self):
        with open(os.path.join(self.folder_selected, "test_file1.md"), 'w') as f:
            f.write("Test")
        with open(os.path.join(self.folder_selected, "test_file2.md"), 'w') as f:
            f.write("Test")
        
        base_name = "test_file"
        next_filename = get_next_filename(base_name, self.folder_selected)
        self.assertEqual(next_filename, "test_file3.md")

    def test_save_markdown_files(self):
        prompts_md = "# Test Prompts\n"
        results_md = "# Test Results\n"
        project_stage = "Test Stage"

        prompts_file_path, results_file_path = save_markdown_files(prompts_md, results_md, self.folder_selected, project_stage)

        self.assertTrue(os.path.exists(prompts_file_path))
        self.assertTrue(os.path.exists(results_file_path))

if __name__ == '__main__':
    unittest.main()
