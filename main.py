from dotenv import load_dotenv
from src import GenerateQA, TextExtractor
from src import FileProcessor

# Load environment variables from .env file
load_dotenv()
    
input_folder = "input_data"
extractor = TextExtractor()
texts = extractor.extract_text_from_folder(input_folder)

for text in texts:
    qa_pairs = GenerateQA(text)
    all_questions = qa_pairs.generate_questions()
    file_procssing = FileProcessor()
    file_procssing.save_questions(all_questions)