# Question Generation for Fine-Tuning
This repository contains a system for generating question-answer pairs for `FINE-TUNING LLMs` from text data. The system leverages various modules to extract text, clean headers and footers, generate questions using a language model, and save the generated questions.

## Latest Update
- Added a feature to remove duplicate and similar questions.
- Simplified the JSONL ouput format cleaning process.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)


## Installation
1. Clone the repository:
```sh
git clone https://github.com/yourusername/question-generation.git
cd question-generation
```

2. Create a virtual environment and activate it:
```sh
python3.11 -m venv .venv
source .venv/bin/activate # On Windows use `venv\Scripts\activate`
```

3. Install the required dependencies:
```sh
pip install -r requirements.txt
```

4. Copy the example environment file and configure it:
```sh
cp .env.example .env
```

5. Update the .env file with your API URL and API Key.

## Configuration
The configuration for the model is specified in the config.json file. You can update the model name or other parameters as needed:
```json
{
    "model_name": "meta-llama/Llama-3.1-8B-Instruct",
    "model_max_tokens": 32000,
    "input_folder": "input_data"
}
```

## Usage

1. Place your input files in the `input_data` folder.

2. To run the question generation process, execute the main.py script:
```sh
python main.py
```

This script will:
1. Load environment variables.
2. Extract text from files in the input_data folder.
3. Generate question-answer pairs from the extracted text.
4. Clean the generated questions.
5. Save the cleaned questions to the generated_questions folder.

## Prompts

- The system prompt for generating question-answer pairs is located in the `prompts` folder as `generateQA-sys_prompt.txt`

## Project Structure
```plaintext
prompt/
    generateQA-sys_prompt.txt
src/
    __init__.py
    fileHandler/
        __init__.py
        cleanHeader.py
        fileProcessing.py
        textExtract.py
    generateQA.py
    openai.py
    questionValidator.py
input_data/
    content.txt
generated_questions/
    generated_questions.jsonl
.env
.env.example
.gitignore
config.json
main.py
README.md
requirements.txt
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License
This project is licensed under the **GNU AFFERO GENERAL PUBLIC LICENSE**. See the LICENSE file for details.
