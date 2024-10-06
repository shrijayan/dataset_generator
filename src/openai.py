import os
from openai import OpenAI

class OpenAIClient:
    def __init__(self, api_url, api_key, model_name):
        self.api_url = api_url
        self.api_key = api_key
        self.model_name = model_name
        self.client = OpenAI(
            base_url=self.api_url,
            api_key=self.api_key  # Some servers might not require this, like Ollama
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

# Initialize the client
client = OpenAIClient(api_url=os.getenv("API_URL"), 
                        api_key=os.getenv("API_KEY"), 
                        model_name="llama3.1",
                        )