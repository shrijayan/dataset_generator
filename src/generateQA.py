from .llm import client
from .tokenCounter import TokenCounter
import textwrap
import json

class GenerateQA:
    def __init__(self):
        self.tokenCounter = TokenCounter()
        with open('prompts/generateQA-sys_prompt.txt', 'r') as file:
            self.sys_prompt = file.read()
        with open('config.json', 'r') as config_file:
            self.config = json.load(config_file)
    
    def generate_chunk_questions(self, content):
        response = client.query_model(content, self.sys_prompt)
        return response
            
    def generate_questions(self, text):
        try:
            model_max_tokens = self.config.get('model_max_tokens')
            sys_prompt_tokens = self.tokenCounter.get_token_size(self.sys_prompt)
            chunk_size_limit = model_max_tokens - sys_prompt_tokens
            
            chunks = textwrap.wrap(text, width=chunk_size_limit, break_long_words=False, replace_whitespace=False)
            all_questions = [question for chunk in chunks for question in self.generate_chunk_questions(chunk)]
            
            return ''.join(all_questions)
        
        except Exception as e:
            print(f"Error generating questions: {str(e)}")
            return None