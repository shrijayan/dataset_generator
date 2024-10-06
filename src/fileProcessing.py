import os
from tqdm import tqdm

class FileProcessor():
    def save_questions(questions, output_folder="generated_questions"):
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        for i, question in enumerate(questions):
            output_file_path = os.path.join(output_folder, f"question_{i}.txt")

            with open(output_file_path, 'w', encoding='utf-8') as file:
                file.write(question)