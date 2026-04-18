from groq import Groq

def call_llm(messages):
    client = Groq(api_key="your_groq_api_key_here")  # paste your key
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=messages
    )
    return response.choices[0].message.content