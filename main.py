from openai import OpenAI

if __name__ == '__main__':
    # Define the input and output folders
    input_folder = "cleaned_data"
    output_folder = "question"

    # Initialize generator and validator
    openai_api_key = "YOUR_API_KEY"
    openai_api_base = "http://10.132.3.11:8000/v1"
    model_name = "meta-llama/Meta-Llama-3-8B-Instruct"
    client = OpenAI(api_key=openai_api_key, base_url=openai_api_base)
    
    validator = QuestionValidator(client, model_name)
    question_generator = OpenAIQuestionGenerator(client, model_name, validator, max_retries=10)

    # Process the files
    file_processor = FileProcessor(question_generator)
    file_processor.process_files(input_folder, output_folder)