import os
from tqdm import tqdm

class FileProcessor():
    def __init__(self, question_generator):
        self.question_generator = question_generator

    def process_files(self, input_folder, output_folder):
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        input_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

        for file_name in tqdm(input_files, desc="Processing files"):
            print(f"Processing file: {file_name}")
            input_file_path = os.path.join(input_folder, file_name)
            output_file_path = os.path.join(output_folder, file_name)

            with open(input_file_path, 'r', encoding='utf-8') as file:
                text = file.read()

            questions = self.question_generator.generate_questions(text)

            if questions:
                with open(output_file_path, 'w', encoding='utf-8') as file:
                    file.write('\n\n'.join(questions))
    
    def save_questions(questions, output_folder):
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        for i, question in enumerate(questions):
            output_file_path = os.path.join(output_folder, f"question_{i}.txt")

            with open(output_file_path, 'w', encoding='utf-8') as file:
                file.write(question)