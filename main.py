from dotenv import load_dotenv
from src import GenerateQA, TextExtractor
from src import FileProcessor
from src import QuestionValidator
from src import HeaderFooterCleaner

# Load environment variables from .env file
load_dotenv()
    
input_folder = "input_data"
extractor = TextExtractor()
texts = extractor.extract_text_from_folder(input_folder)

for text in texts:
    qa_pairs = GenerateQA()
    all_questions = qa_pairs.generate_questions(text)
    
    # validator = QuestionValidator()
    # validator.validate_questions(all_questions)
    
    cleaner = HeaderFooterCleaner()
    cleaned_text = cleaner.remove_unwanted_lines(all_questions)
    
    file_procssing = FileProcessor()
    file_procssing.save_questions(cleaned_text)