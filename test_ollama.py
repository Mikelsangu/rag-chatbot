import ollama

response = ollama.chat(
    model='llama3.1:8b',
    messages=[
        {'role': 'user', 'content': '¿Quién eres?'}
    ]
)

print(response['message']['content'])