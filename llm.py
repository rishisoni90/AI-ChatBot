# llm.py
import streamlit as st
from groq import Groq
import json

def call_llm(messages, tools=None):
    filtered = [m for m in messages if m["role"] in ["user", "assistant"]]

    if not filtered:
        filtered = [{"role": "user", "content": "Hello"}]

    # fix alternating roles
    clean = []
    for m in filtered:
        if clean and clean[-1]["role"] == m["role"]:
            clean[-1]["content"] += "\n" + m["content"]
        else:
            clean.append({"role": m["role"], "content": m["content"]})

    if clean[0]["role"] != "user":
        clean.insert(0, {"role": "user", "content": "Hello"})

    try:
        api_key = st.secrets["GROQ_API_KEY"]
    except:
        return {"type": "text", "text": "❌ GROQ_API_KEY not found"}

    client = Groq(api_key=api_key)

    # Pass tools to Groq — Llama 3 now decides
    kwargs = {"model": "llama-3.3-70b-versatile", "messages": clean}
    if tools:
        kwargs["tools"] = tools  # ← this is the MCP-style change

    response = client.chat.completions.create(**kwargs)
    message = response.choices[0].message

    # Did Llama 3 call a tool?
    if message.tool_calls:
        tool_call = message.tool_calls[0]
        return {
            "type": "tool_call",
            "tool": tool_call.function.name,
            "args": json.loads(tool_call.function.arguments)
        }

    # Regular text answer
    return {
        "type": "text",
        "text": message.content
    }