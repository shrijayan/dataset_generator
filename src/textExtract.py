import os

class TextExtractor:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        
    def extract_text_from_folder(self):
        extracted_texts = []
        
        # List all files in the folder
        for file_name in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, file_name)
            
            # Check if it's a file
            if os.path.isfile(file_path):
                with open(file_path, 'r') as file:
                    content = file.read()
                    extracted_texts.append(content)
            else:
                print(f"Skipping non-file: {file_path}")
        
        return extracted_texts