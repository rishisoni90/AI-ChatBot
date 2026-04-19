import streamlit as st
from memory import Memory
from agent import Agent

# --- Page Config ---
st.set_page_config(
    page_title="Rabbit AI",
    page_icon="🐇",
    layout="centered"
)

# --- Init session state ---
if "memory" not in st.session_state:
    st.session_state.memory = Memory()
    st.session_state.agent = Agent(st.session_state.memory)
    st.session_state.chat_history = []

# --- Title (just text, no gif) ---
st.title("🐇 Rabbit AI")

# --- Chat History ---
for user_msg, ai_msg in st.session_state.chat_history:
    with st.chat_message("user"):
        st.write(user_msg)
    with st.chat_message("assistant", avatar="🐇"):
        st.write(ai_msg)

# --- Input fixed at bottom ---
user_input = st.chat_input("Message Rabbit AI...")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant", avatar="🐇"):
        with st.spinner(""):
            response = st.session_state.agent.run(user_input)
        st.write(response)

    st.session_state.chat_history.append((user_input, response))