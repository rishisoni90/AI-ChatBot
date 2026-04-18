import requests

def call_llm(messages):
    prompt = messages[-1]["content"]

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()

    if "response" in data:
        return data["response"]
    else:
        return str(data)