import os
from tqdm import tqdm

class FileProcessor():
    def save_questions(self, questions, output_folder="generated_questions"):
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        output_file_path = os.path.join(output_folder, f"question.jsonl")

        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(questions)