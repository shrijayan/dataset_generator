import os
from openai import OpenAI, AzureOpenAI
import json
from dotenv import load_dotenv

load_dotenv()

# Load configuration
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

class LLM:
    def __init__(self, api_url=None, api_key=None, model_name=None):
        self.model_name = model_name or config.get('model_name')
        inference_engine = config.get('inference_engine', 'openai').lower()

        if inference_engine == 'azure':
            self.client = AzureOpenAI(
                api_key=api_key or os.getenv("AZURE_OPENAI_API_KEY"),
                api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
                azure_endpoint=api_url or os.getenv("AZURE_OPENAI_ENDPOINT")
            )
        else:
            self.client = OpenAI(
                base_url=api_url or os.getenv("API_URL"),
                api_key=api_key or os.getenv("API_KEY")
            )

    def query_model(self, prompt, system_message=None):
        # Prepare the chat messages
        messages = [
            {"role": "user", "content": prompt}
        ]
        if system_message:
            messages.insert(0, {"role": "system", "content": system_message})

        # Call the model and generate a response
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages
        )

        # Return the result
        return response.choices[0].message.content

# Initialize a single client based on configuration
client = LLM(
    api_url=os.getenv("AZURE_OPENAI_ENDPOINT" if config.get('inference_engine') == 'azure' else "API_URL"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY" if config.get('inference_engine') == 'azure' else "API_KEY"),
    model_name=os.getenv("AZURE_OPENAI_MODEL_NAME" if config.get('inference_engine') == 'azure' else "MODEL_NAME")
)

if __name__ == "__main__":
    user_prompt = "Hello, how are you?"
    response = client.query_model(user_prompt)
    print(response)