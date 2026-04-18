import streamlit as st
from groq import Groq

def call_llm(messages):
    # filter out system messages if needed
    filtered = [m for m in messages if m["role"] in ["user", "assistant"]]
    
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=filtered
    )
    return response.choices[0].message.content