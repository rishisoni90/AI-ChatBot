import streamlit as st
from memory import Memory
from agent import Agent

# setup
memory = Memory()
agent = Agent(memory)

st.title("🐇 Rabbit...")

user_input = st.text_input("Ask something")

if user_input:
    with st.spinner("Thinking..."):
        response = agent.run(user_input)

    st.write("**AI:**", response)