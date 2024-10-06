import os
from dotenv import load_dotenv
from src import GenerateQA, TextExtractor, OpenAIClient

# Load environment variables from .env file
load_dotenv()
    
input_folder = "input_data"
texts = TextExtractor.extract_text_from_folder(input_folder)

for text in texts:
    qa_pairs = GenerateQA(text)
    qa_pairs.generate_questions()