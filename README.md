# Dataset Generator for Fine-Tuning
This repository contains a system for generating question-answer pairs for `FINE-TUNING LLMs` from the data you have. The system leverages various modules to extract text, generate questions using a language model, and save the generated questions.

## Latest Update
- Added a feature to prcoess HTML as input files.
- Added a feature to remove duplicate and similar questions.
- Simplified the JSONL ouput format cleaning process.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Supported Inference Engine
1. VLLM
2. OpenAI API
3. Azure OpenAI API
4. Ollama

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
    "inference_engine": "azure", # Enter your inference engine here
    "model_name": "llama3.1", # Enter your model name here
    "model_max_tokens": 10000, # Enter your model's max tokens here
    "input_folder": "input_data",
    "output_folder": "generated_questions",
    "chroma_db_path": "chromadb",
    "chroma_collection_name": "questions",
    "duplicate_threshold": 0.1
}
```

## Usage

1. Place your input files in the `input_data` folder.

2. To run the question generation process, execute the main.py script:
```sh
python main.py
```

## Prompts

- The system prompt for generating question-answer pairs is located in the `prompts` folder as `generateQA-sys_prompt.txt`

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License
This project is licensed under the **Apache-2.0 license**. See the LICENSE file for details.
