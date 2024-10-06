def vllm(client, model_name, validation_prompt, questions):
    
    chat_response = client.chat.completions.create(
                model=model_name,
                messages=[
                    {"role": "system", "content": validation_prompt},
                    {"role": "user", "content": questions}
                ],
            )
    
    return chat_response.choices[0].message.content