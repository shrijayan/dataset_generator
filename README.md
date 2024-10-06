# Question Generation
This repository contains a system for generating and validating question-answer pairs from text data. The system leverages various modules to extract text, clean headers and footers, generate questions using a language model, and save the generated questions.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)


## Installation
1. Clone the repository:
```
git clone https://github.com/yourusername/question-generation.git
cd question-generation
```

2. Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required dependencies:
```
pip install -r requirements.txt
```

4. Copy the example environment file and configure it:
```
cp .env.example .env
```

5. Update the .env file with your API URL and API Key.

## Configuration
The configuration for the model is specified in the config.json file. You can update the model name or other parameters as needed:
```
{
    "model_name": "meta-llama/Llama-3.1-8B-Instruct"
}
```

## Usage

To run the question generation process, execute the main.py script:
```
python main.py
```

This script will:
1. Load environment variables.
2. Extract text from files in the input_data folder.
3. Generate question-answer pairs from the extracted text.
4. Clean the generated questions.
5. Save the cleaned questions to the generated_questions folder.

## Project Structure
```
.DS_Store
.env
.env.example
.gitignore
config.json
main.py
README.md
requirements.txt
src/
    __init__.py
    __pycache__/
    cleanHeader.py
    fileProcessing.py
    generateQA.py
    openai.py
    questionValidator.py
    textExtract.py
input_data/
    content.txt
generated_questions/
    generated_questions.jsonl
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License
This project is licensed under the **GNU AFFERO GENERAL PUBLIC LICENSE**. See the LICENSE file for details.