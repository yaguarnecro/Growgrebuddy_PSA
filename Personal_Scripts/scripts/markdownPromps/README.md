# Markdown Generator

## Description
Markdown Generator is a Python-based GUI application that allows users to generate structured markdown files from prompts and responses. It's designed to help users document AI conversations and outputs in a consistent format.

## Features
- User-friendly graphical interface
- Support for single and multiple entry modes
- AI tool selection dropdown
- Automatic file naming and organization
- Progress tracking and logging
- Dark mode interface for reduced eye strain

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/markdown-generator.git
   cd markdown-generator
   ```
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the application:
   ```
   python main.py
   ```
2. Select an AI tool from the dropdown menu.
3. Choose between Single Entry or Multiple Entry tabs.
4. Enter your prompts and responses in the respective text areas.
5. Click the "Process" button to generate markdown files.
6. Select an output folder when prompted.
7. View the generated files in the selected folder.

## File Structure
- `main.py`: Main application file containing the GUI implementation
- `utils.py`: Utility functions for processing input and parsing prompts
- `markdown_generator.py`: Functions for generating markdown content
- `file_operations.py`: Functions for file handling and naming

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add some feature'`)
5. Push to the branch (`git push origin feature/your-feature-name`)
6. Create a new Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Thanks to all contributors who have helped shape this project.
- Inspired by the need for efficient documentation of AI conversations.

