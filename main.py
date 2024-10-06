from openai import OpenAI
from src import GenerateQA, TextExtractor, OpenAIClient
    
input_folder = "cleaned_data"

# Initialize the client
client = OpenAIClient(api_url="http://10.132.3.11:11434/v1", 
                        api_key="your_api_key", 
                        model_name="llama3.1",
                        )

# Query the model
response = client.query_model(prompt="Hello, how are you?")

extractor = TextExtractor(input_folder)
texts = extractor.extract_text_from_folder()
for text in texts:
    qa_pairs = GenerateQA(client, text)
    qa_pairs.generate_questions()