from .openai import client

class QuestionValidator():
    def __init__(self):
        self.sys_prompt = '''Verify if the provided content exclusively consists of question and answer pairs, ensuring that both a question and an answer are present for each pair. Also verify the questions are meaningful. Respond with 'YES' if all pairs meet this criterion, otherwise respond with 'NO'.'''

    def validate_questions(self, questions):
        try:    
            response_content = client.query_model(questions, self.sys_prompt)            
            return True if "YES" in response_content else False
        except Exception as e:
            return False