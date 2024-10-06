from openai import OpenAI
from src import GenerateQA, TextExtractor, OpenAIClient

if __name__ == '__main__':
    
    input_folder = "cleaned_data"
    output_folder = "question"

    openai_api_key = "YOUR_API_KEY"
    # openai_api_base = "http://10.132.3.11:8000/v1"
    openai_api_base = "http://10.132.3.11:8000/v1"
    model_name = "meta-llama/Meta-Llama-3-8B-Instruct"
    client = OpenAI(api_key=openai_api_key, base_url=openai_api_base)
    
    # Example usage for Ollama
    ollama_api_url = 'http://localhost:11434/v1'
    ollama_model_name = 'llama2'
    ollama_api_key = 'ollama'  # Required but not used
    ollama_system_message = "You are a helpful assistant."
    ollama_prompt = "Who won the world series in 2020?"

    # Initialize the client
    client = OpenAIClient(api_url="http://10.132.3.11:11434/v1", api_key="your_api_key")

    # Query the model
    response = client.query_model(prompt="Hello, how are you?", model_name="llama3.1")
    print(response)
    
    # Example usage
    # texts = TextExtractor(input_folder)
    # for text in texts:
    #     qa_pairs = GenerateQA(client, model_name, text)
    
    # validator = QuestionValidator(client, model_name)
    # question_generator = OpenAIQuestionGenerator(client, model_name, validator, max_retries=10)

    # # Process the files
    # file_processor = FileProcessor(question_generator)
    # file_processor.process_files(input_folder, output_folder)