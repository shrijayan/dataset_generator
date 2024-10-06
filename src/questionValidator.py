class QuestionValidator(IQuestionValidator):
    def __init__(self, client, model_name):
        self.client = client
        self.model_name = model_name

    def validate_questions(self, questions):
        try:
            validation_prompt = '''Verify if the provided content exclusively consists of question and answer pairs, ensuring that both a question and an answer are present for each pair. Also verify the questions are meaningful. Respond with 'YES' if all pairs meet this criterion, otherwise respond with 'NO'.'''
            
            response_content = vllm(self.client, self.model_name, validation_prompt, questions)
            
            print(f"Validation response:\n{response_content}")
            return True if "YES" in response_content else False
        except Exception as e:
            print(f"Error validating questions: {str(e)}")
            return False