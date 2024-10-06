from .fileProcessing import FileProcessor
class GenerateQA:
    def __init__(self, client, text):
        self.client = client
        self.text = text

    def generate_questions(self):
        try:
            model_max_tokens = 32000
            prompt_tokens = 3000
            max_chunk_size = model_max_tokens - prompt_tokens
            if len(self.text) > max_chunk_size:
                chunks = [self.text[i:i+max_chunk_size] for i in range(0, len(self.text), max_chunk_size)]
            else:
                chunks = [self.text]
            
            all_questions = []

            for chunk in chunks:
            #     validated = False
            #     attempts = 0
                chuck_qa = self.generate_chunk_questions(chunk)
                all_questions.append(chuck_qa)

                # while not validated and attempts < self.max_retries:
                #     attempts += 1
                #     clean_content = self.generate_chunk_questions(chunk)
                    
                #     if self.validator.validate_questions(f"Original content:\n{clean_content}\n\nPlease respond with either 'YES' or 'NO'."):
                #         print(f"Validation successful for chunk on attempt {attempts}")
                #         all_questions.append(clean_content)
                #         validated = True
                #     else:
                #         if attempts < self.max_retries:
                #             print(f"Validation failed for chunk on attempt {attempts}. Retrying...")
                #         else:
                #             print(f"Validation failed for chunk after {self.max_retries} attempts. Moving to next chunk.")
                FileProcessor.save_questions(all_questions)
            return all_questions
        except Exception as e:
            print(f"Error generating questions: {str(e)}")
            return None
    
    def generate_chunk_questions(self, content):
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
        
        response = self.client.query_model(content, sys_prompt)
        
        return response
        # return self.clean_up_questions(response_content)