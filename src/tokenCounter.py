import tiktoken
class TokenCounter:
    def get_token_size(self, text, model_name="gpt-4"):
        # Load the tokenizer for the specified model
        encoding = tiktoken.encoding_for_model(model_name)
        
        # Tokenize the input text
        tokens = encoding.encode(text)
        
        # Return the number of tokens
        return len(tokens)

if __name__ == "__main__":
    text = "This is an example text to calculate the token size using GPT-4."
    tokenCounter = TokenCounter()
    token_size = tokenCounter.get_token_size(text)
    print(f"Token size: {token_size}")