import streamlit as st
import time
from memory import Memory
from agent import Agent

# --- Page Config ---
st.set_page_config(
    page_title="Rabbit AI",
    page_icon="🐇",
    layout="centered"
)

# --- Animated dots CSS (Claude-style thinking) ---
st.markdown("""
<style>
@keyframes blink {
    0%, 80%, 100% { opacity: 0; transform: scale(0.8); }
    40% { opacity: 1; transform: scale(1.2); }
}
.thinking-dots {
    display: flex;
    align-items: center;
    gap: 5px;
    padding: 4px 0;
}
.thinking-dots span {
    width: 8px;
    height: 8px;
    background-color: #a78bfa;
    border-radius: 50%;
    display: inline-block;
    animation: blink 1.4s infinite ease-in-out;
}
.thinking-dots span:nth-child(2) { animation-delay: 0.2s; }
.thinking-dots span:nth-child(3) { animation-delay: 0.4s; }
</style>
""", unsafe_allow_html=True)

# --- Init session state ---
if "memory" not in st.session_state:
    st.session_state.memory = Memory()
    st.session_state.agent = Agent(st.session_state.memory)
    st.session_state.chat_history = []

# --- Title ---
st.title(" VJNA AI")

# --- Chat History ---
for user_msg, ai_msg in st.session_state.chat_history:
    with st.chat_message("user"):
        st.write(user_msg)
    with st.chat_message("assistant", avatar="🐇"):
        st.write(ai_msg)

# --- Input ---
user_input = st.chat_input("Message VJNA AI...")

if user_input:
    # Show user message
    with st.chat_message("user"):
        st.write(user_input)

    # Show animated dots while thinking
    with st.chat_message("assistant", avatar="🐇"):
        dot_placeholder = st.empty()
        dot_placeholder.markdown("""
        <div class="thinking-dots">
            <span></span><span></span><span></span>
        </div>
        """, unsafe_allow_html=True)

        # Get response
        response = st.session_state.agent.run(user_input)

        # Replace dots with actual response
        dot_placeholder.empty()
        st.write(response)

    st.session_state.chat_history.append((user_input, response))