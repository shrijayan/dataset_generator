from .cleanHeader import HeaderFooterCleaner
from .openai import client
from .tokenCounter import TokenCounter
import textwrap 

class GenerateQA:
    def __init__(self):
        self.tokenCounter = TokenCounter()
        
        with open('prompts/generateQA-sys_prompt.txt', 'r') as file:
            self.sys_prompt = file.read()
            
    def generate_questions(self, text):
        try:
            model_max_tokens = 32000
            sys_prompt_tokens = self.tokenCounter.get_token_size(self.sys_prompt)
            chunk_size_limit = model_max_tokens - sys_prompt_tokens
            
            chunks = textwrap.wrap(text, width=chunk_size_limit, break_long_words=False, replace_whitespace=False)
            
            all_questions = [question for chunk in chunks for question in self.generate_chunk_questions(chunk)]
            
            # Return all questions combined as a string
            return ''.join(all_questions)
        
        except Exception as e:
            # Handle and log the exception (e.g., logging module)
            print(f"Error generating questions: {str(e)}")
            return ""

        
        except Exception as e:
            print(f"Error generating questions: {str(e)}")
            return None
    
    def generate_chunk_questions(self, content):
        response = client.query_model(content, self.sys_prompt)
        
        return response