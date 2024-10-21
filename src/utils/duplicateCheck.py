import os
import json
import chromadb
import random

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

class duplicateCheck:
    def __init__(self):
        if not os.path.exists(config.get('chroma_db_path')):
            os.makedirs(config.get('chroma_db_path'))
        self.chroma_client = chromadb.PersistentClient(path=config.get('chroma_db_path'))
        
        self.collection = self.chroma_client.get_or_create_collection(name=config.get('chroma_collection_name'))
        
    def check_duplicate(self, question):
        similarity = self.collection.query(query_texts=[question], n_results=1)
        if similarity['documents'][0]:
            if similarity['distances'][0][0] > config.get('duplicate_threshold'):
                return True
            else:
                return False
        return True
            
    def add_to_chroma_db(self, question):
        if self.check_duplicate(question):
            self.collection.add(documents=[question], ids=[str(random.randint(0, 999999999))])
            return True
        else:
            return False
    
    def process_jsonl_files(self, folder_path):
        for filename in os.listdir(folder_path):
            if filename.endswith('.jsonl'):
                file_path = os.path.join(folder_path, filename)
                with open(file_path, 'r+') as file:
                    lines = [line.strip() for line in file if line.strip()]
                    
                    non_duplicate_lines = []
                    for line in lines:
                        json_data = json.loads(line)
                        question = json_data['question']
                        if self.add_to_chroma_db(question):
                            non_duplicate_lines.append(line)
                    
                    file.seek(0)
                    file.writelines(f"{line}\n" for line in non_duplicate_lines)
                    file.truncate()
        
if __name__ == '__main__':
    folder_path = config.get('output_folder')
    duplicateJsonLines = duplicateCheck()
    duplicateJsonLines.process_jsonl_files(folder_path)