from openai import OpenAI
from src import GenerateQA, TextExtractor, OpenAIClient

if __name__ == '__main__':
    
    input_folder = "cleaned_data"
    output_folder = "question"

    # Initialize the client
    client = OpenAIClient(api_url="http://10.132.3.11:11434/v1", api_key="your_api_key", model_name="llama3.1")

    # Query the model
    response = client.query_model(prompt="Hello, how are you?")
    
    texts = TextExtractor(input_folder)
    for text in texts:
        qa_pairs = GenerateQA(client, model_name, text)
    
    # validator = QuestionValidator(client, model_name)
    # question_generator = OpenAIQuestionGenerator(client, model_name, validator, max_retries=10)

    # # Process the files
    # file_processor = FileProcessor(question_generator)
    # file_processor.process_files(input_folder, output_folder)