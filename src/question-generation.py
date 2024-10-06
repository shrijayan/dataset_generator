import os
from tqdm import tqdm
from openai import OpenAI
from model_providers import vllm, ollama
from abc import ABC, abstractmethod

class IQuestionGenerator(ABC):
    @abstractmethod
    def generate_questions(self, text):
        pass

class IQuestionValidator(ABC):
    @abstractmethod
    def validate_questions(self, questions):
        pass

class IFileProcessor(ABC):
    @abstractmethod
    def process_files(self, input_folder, output_folder):
        pass

class OpenAIQuestionGenerator(IQuestionGenerator):
    def __init__(self, client, model_name, validator, max_retries=10):
        self.client = client
        self.model_name = model_name
        self.validator = validator
        self.max_retries = max_retries

    def clean_up_questions(self, text):
        first_line_remove_words = ['Here', 'I']
        last_line_remove_words = ['Let', 'Note:', 'Please', 'If', '(Note:']
        lines = text.split('\n')
        if any(lines[0].startswith(word) for word in first_line_remove_words):
            lines = lines[1:]
        if any(lines[-1].startswith(word) for word in last_line_remove_words):
            lines = lines[:-1]
        return '\n'.join(lines)

    def generate_chunk_questions(self, chunk):
        sys_prompt = '''You are the meaningful factual Question and Answer generation bot specializing in the banking domain. Generate the question in customer point of view, which will be answered by the customer care agent. Your objective is to generate detailed questions based on provided content, incorporating specific product details. For instance, generate a question such as:

        <question>  What is the Savings Bank interest? </question>
        <answer> <question>  Is there any cost for applying Commercial Credit Card? And how to apply it? </question>
        <answer> The benefits of an add-on card include a shared credit limit with the primary card, minimum documentation requirements, zero cost and zero annual fee, a consolidated statement for all cards, and the ability to earn Axis eDGE Rewards points on select cards. To apply for an add-on card, you can SMS "ADDON" to 5676782 or submit a duly filled application form with self-attested KYC documents at your nearest branch.  </answer>
        <question>  Is there any cost for applying Commercial Credit Card? And how to apply it? </question>
        <answer> The benefits of an add-on card include a shared credit limit with the primary card, minimum documentation requirements, zero cost and zero annual fee, a consolidated statement for all cards, and the ability to earn Axis eDGE Rewards points on select cards. To apply for an add-on card, you can SMS "ADDON" to 5676782 or submit a duly filled application form with self-attested KYC documents at your nearest branch. </answer>
        <question> What are the Options for paying Axis Bank Credit Card bill? </question>
        <answer> There are four methods for paying Axis Bank Credit Card bill: SMS Payment Option, Offline Payment Options, IMPS Payment Option, Pay at ATMs </answer>
        <question> I have a fixed deposit of 10 Lakhs how much is my eligibility amount? </question>
        <answer> The overdraft amount is based on the fixed deposit amount, with a maximum of 85 percent of the deposit value. You'll only pay interest on the amount you utilize, not on the entire limit. </answer>
        <question> What if I withdraw less than the eligible amount for Overdraft Against Fixed Deposit? </question>
        <answer> For Example if you're eligible for an overdraft of Rs 85,000 but withdraw only Rs 50,000, you'll be charged interest only on Rs 50,000. </answer>
        <question> I have account in some other bank can I enrol ECS from that account? </question>
        <answer> Yes, you can enroll ECS and pay your bill from any other bank account by downloading the ECS forms and sending them to the address mentioned on the form. </answer>'''
        
        response_content = vllm(self.client, self.model_name, sys_prompt, chunk)
        
        return self.clean_up_questions(response_content)

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
                validated = False
                attempts = 0

                while not validated and attempts < self.max_retries:
                    attempts += 1
                    clean_content = self.generate_chunk_questions(chunk)
                    
                    if self.validator.validate_questions(f"Original content:\n{clean_content}\n\nPlease respond with either 'YES' or 'NO'."):
                        print(f"Validation successful for chunk on attempt {attempts}")
                        all_questions.append(clean_content)
                        validated = True
                    else:
                        if attempts < self.max_retries:
                            print(f"Validation failed for chunk on attempt {attempts}. Retrying...")
                        else:
                            print(f"Validation failed for chunk after {self.max_retries} attempts. Moving to next chunk.")
            
            return all_questions
        except Exception as e:
            print(f"Error generating questions: {str(e)}")
            return None

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

class FileProcessor(IFileProcessor):
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

if __name__ == '__main__':
    # Define the input and output folders
    input_folder = "cleaned_data"
    output_folder = "question"

    # Initialize generator and validator
    openai_api_key = "YOUR_API_KEY"
    openai_api_base = "http://10.132.3.11:8000/v1"
    model_name = "meta-llama/Meta-Llama-3-8B-Instruct"
    client = OpenAI(api_key=openai_api_key, base_url=openai_api_base)
    
    validator = QuestionValidator(client, model_name)
    question_generator = OpenAIQuestionGenerator(client, model_name, validator, max_retries=10)

    # Process the files
    file_processor = FileProcessor(question_generator)
    file_processor.process_files(input_folder, output_folder)