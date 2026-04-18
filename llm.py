import streamlit as st
from groq import Groq

def call_llm(messages):
    # Keep system messages but ensure at least one user message exists
    filtered = []
    for m in messages:
        if m["role"] == "system":
            # Convert system to user message for Groq compatibility
            filtered.append({"role": "user", "content": m["content"]})
        elif m["role"] in ["user", "assistant"]:
            filtered.append(m)

    # Safety check - must have at least one message
    if not filtered:
        filtered = [{"role": "user", "content": "Hello"}]

    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=filtered
    )
    return response.choices[0].message.content