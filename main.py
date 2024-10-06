import os
from dotenv import load_dotenv
from src import GenerateQA, TextExtractor, OpenAIClient

# Load environment variables from .env file
load_dotenv()
    
input_folder = "input_data"

# Initialize the client
client = OpenAIClient(api_url=os.getenv("API_URL"), 
                        api_key=os.getenv("API_KEY"), 
                        model_name="llama3.1",
                        )

# Query the model
response = client.query_model(prompt="Hello, how are you?")

extractor = TextExtractor(input_folder)
texts = extractor.extract_text_from_folder()
for text in texts:
    qa_pairs = GenerateQA(client, text)
    qa_pairs.generate_questions()