import streamlit as st
from groq import Groq

def call_llm(messages):
    # Step 1: only keep user and assistant roles
    filtered = [m for m in messages if m["role"] in ["user", "assistant"]]

    # Step 2: must have at least one message
    if not filtered:
        filtered = [{"role": "user", "content": "Hello"}]

    # Step 3: fix alternating - merge consecutive same-role messages
    clean = []
    for m in filtered:
        if clean and clean[-1]["role"] == m["role"]:
            # merge content instead of dropping
            clean[-1]["content"] += "\n" + m["content"]
        else:
            clean.append({"role": m["role"], "content": m["content"]})

    # Step 4: must start with user
    if clean[0]["role"] != "user":
        clean.insert(0, {"role": "user", "content": "Hello"})

    # Step 5: get API key
    try:
        api_key = st.secrets["GROQ_API_KEY"]
    except Exception:
        return "❌ GROQ_API_KEY not found in Streamlit secrets."

    # Step 6: call Groq
    client = Groq(api_key=api_key)
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=clean
    )
    return response.choices[0].message.content