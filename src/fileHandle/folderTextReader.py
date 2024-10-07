import os

class FolderTextReader:
    def extract_text_from_folder(self, folder_path):
        num_files = len([name for name in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, name)) and name.endswith('.txt')])
        
        extracted_texts = []
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            
            if file_path.lower().endswith('.txt'):
                if os.path.isfile(file_path):
                    with open(file_path, 'r') as file:
                        content = file.read()
                        file_name_without_extension = os.path.splitext(file_name)[0]
                        extracted_texts.append((content, file_name_without_extension))
                else:
                    print(f"Skipping non-file: {file_path}")
        
        return extracted_texts, num_files