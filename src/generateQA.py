from .cleanHeader import HeaderFooterCleaner
from .openai import client

class GenerateQA:
    def generate_questions(self, text):
        try:
            model_max_tokens = 32000
            prompt_tokens = 3000
            max_chunk_size = model_max_tokens - prompt_tokens
            if len(text) > max_chunk_size:
                chunks = [text[i:i+max_chunk_size] for i in range(0, len(text), max_chunk_size)]
            else:
                chunks = [text]
            
            all_questions = []
            for chunk in chunks:
                chuck_qa = self.generate_chunk_questions(chunk)
                all_questions.append(chuck_qa)
                
            return '\n'.join(all_questions)
        
        except Exception as e:
            print(f"Error generating questions: {str(e)}")
            return None
    
    def generate_chunk_questions(self, content):
        with open('prompts/generateQA-sys_prompt.txt', 'r') as file:
            sys_prompt = file.read()
            
        response = client.query_model(content, sys_prompt)
        
        return response