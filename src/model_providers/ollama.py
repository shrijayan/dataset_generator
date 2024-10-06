def ollama(client, model_name, validation_prompt, questions):
    
    chat_response = ollama.chat(
        model=model_name, 
        messages=[
            {"role": "system", "content": validation_prompt},
            {"role": "user", "content": questions}
        ],
    )
    
    return chat_response['message']['content']