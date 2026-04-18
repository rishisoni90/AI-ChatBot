import streamlit as st
from groq import Groq

def call_llm(messages):
    # Only keep user and assistant messages
    filtered = [m for m in messages if m["role"] in ["user", "assistant"]]

    # Must have at least one message
    if not filtered:
        filtered = [{"role": "user", "content": "Hello"}]

    # Remove consecutive duplicate roles
    clean = []
    for m in filtered:
        if clean and clean[-1]["role"] == m["role"]:
            continue
        clean.append(m)

    # Must start with user
    if clean[0]["role"] != "user":
        clean.insert(0, {"role": "user", "content": "Hello"})

    try:
        api_key = st.secrets["GROQ_API_KEY"]
    except Exception:
        return "❌ ERROR: GROQ_API_KEY not found in Streamlit secrets. Please add it in Settings → Secrets."

    client = Groq(api_key=api_key)
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=clean
    )
    return response.choices[0].message.content