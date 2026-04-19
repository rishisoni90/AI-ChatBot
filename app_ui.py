import streamlit as st
from memory import Memory
from agent import Agent

# --- Page Config ---
st.set_page_config(
    page_title="VJNA AI",
    page_icon="🐇",
    layout="centered"
)

# --- CSS ---
st.markdown("""
<style>

/* === THINKING DOTS === */
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

/* === ANIMATED TITLE === */
@keyframes colorShift {
    0%   { color: #ff6b6b; }
    16%  { color: #ffa94d; }
    33%  { color: #ffe066; }
    50%  { color: #69db7c; }
    66%  { color: #4dabf7; }
    83%  { color: #cc5de8; }
    100% { color: #ff6b6b; }
}
.vjna-title {
    font-size: 2.2rem;
    font-weight: 800;
    animation: colorShift 3s infinite ease-in-out;
    display: inline-block;
}

</style>
""", unsafe_allow_html=True)

# --- Init session state ---
if "memory" not in st.session_state:
    st.session_state.memory = Memory()
    st.session_state.agent = Agent(st.session_state.memory)
    st.session_state.chat_history = []

# --- Animated Title ---
st.markdown('<span class="vjna-title">VJNA AI 🐇</span>', unsafe_allow_html=True)

# --- Chat History ---
for user_msg, ai_msg in st.session_state.chat_history:
    with st.chat_message("user"):
        st.write(user_msg)
    with st.chat_message("assistant", avatar="🤖"):
        st.write(ai_msg)

# --- Input ---
user_input = st.chat_input("Message VJNA AI...")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant", avatar="🤖"):
        dot_placeholder = st.empty()
        dot_placeholder.markdown("""
        <div class="thinking-dots">
            <span></span><span></span><span></span>
        </div>
        """, unsafe_allow_html=True)

        response = st.session_state.agent.run(user_input)

        dot_placeholder.empty()
        st.write(response)

    st.session_state.chat_history.append((user_input, response))