import os

class FileProcessor():
    def save_questions(self, questions, input_file_name, output_folder="generated_questions"):
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        output_file_path = os.path.join(output_folder, f"{input_file_name}.jsonl")

        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(questions)
        
        