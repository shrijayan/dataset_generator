# openai.py
from openai import OpenAI

class OpenAIClient:
    def __init__(self, api_url, api_key):
        self.api_url = api_url
        self.api_key = api_key
        self.client = OpenAI(
            base_url=self.api_url,
            api_key=self.api_key  # Some servers might not require this, like Ollama
        )

    def query_model(self, prompt, model_name, system_message=None):
        # Prepare the chat messages
        messages = [
            {"role": "user", "content": prompt}
        ]
        
        if system_message:
            messages.insert(0, {"role": "system", "content": system_message})

        # Call the model and generate a response
        response = self.client.chat.completions.create(
            model=model_name,
            messages=messages
        )
        
        # Return the result
        return response.choices[0].message.content