import json
import multiprocessing
from tqdm import tqdm
from dotenv import load_dotenv
from src import GenerateQA, TextExtractor, FileProcessor, HeaderFooterCleaner, FolderTextReader
from src.fileHandle import duplicateCheck

# Load environment variables from .env file
load_dotenv()

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

def process_file(text_and_filename):
    text, input_file_name = text_and_filename
    qa_pairs = GenerateQA()
    all_questions = qa_pairs.generate_questions(text)
    
    cleaner = HeaderFooterCleaner()
    cleaned_text = cleaner.remove_unwanted_lines(all_questions)
    
    file_processing = FileProcessor()
    file_processing.save_file(cleaned_text, input_file_name)

if __name__ == "__main__":
    text_extractor = TextExtractor()
    text_extractor.process_folder(config.get('input_folder'))
    
    extractor = FolderTextReader()
    texts, num_files = extractor.extract_text_from_folder(config.get('input_folder'))
    
    if config.get('inference_engine').lower() == 'vllm':
        # Create a pool of worker processes
        num_processes = multiprocessing.cpu_count()
        pool = multiprocessing.Pool(processes=num_processes)

        # Use tqdm to create a progress bar
        with tqdm(total=num_files, desc="Processed files") as pbar:
            for _ in pool.imap_unordered(process_file, texts):
                pbar.update()

        # Close the pool of worker processes
        pool.close()
        pool.join()
    
    else:
        for text in texts:
            process_file(text)

    duplicateremover = duplicateCheck()
    duplicateremover.process_jsonl_files(config.get('output_folder'))