import streamlit as st
from memory import Memory
from agent import Agent

# --- Page Config ---
st.set_page_config(page_title="Rabbit AI", page_icon="🐇", layout="centered")

# --- Init session state ---
if "memory" not in st.session_state:
    st.session_state.memory = Memory()
    st.session_state.agent = Agent(st.session_state.memory)
    st.session_state.chat_history = []  # list of (user, ai) tuples
if "input_key" not in st.session_state:
    st.session_state.input_key = 0  # used to clear the text box

# --- Custom CSS ---
st.markdown("""
    <style>
        .rabbit-container { text-align: center; }
        .title { text-align: center; font-size: 2rem; font-weight: bold; }
        .subtitle { text-align: center; color: gray; font-size: 0.9rem; margin-bottom: 20px; }
        .user-bubble {
            background-color: #DCF8C6;
            border-radius: 15px;
            padding: 10px 15px;
            margin: 6px 0;
            text-align: right;
        }
        .ai-bubble {
            background-color: #F0F0F0;
            border-radius: 15px;
            padding: 10px 15px;
            margin: 6px 0;
            text-align: left;
        }
    </style>
""", unsafe_allow_html=True)

# --- Rabbit GIF ---
st.markdown('<div class="rabbit-container">', unsafe_allow_html=True)
st.image("https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif", width=130)
st.markdown('</div>', unsafe_allow_html=True)

# --- Title ---
st.markdown('<div class="title">Rabbit AI Assistant 🐇</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ask me anything, I\'ll hop right on it!</div>', unsafe_allow_html=True)

st.divider()

# --- Chat History (shown above input) ---
for user_msg, ai_msg in st.session_state.chat_history:
    st.markdown(f'<div class="user-bubble">🧑 <b>You:</b> {user_msg}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="ai-bubble">🐇 <b>Rabbit AI:</b> {ai_msg}</div>', unsafe_allow_html=True)

st.divider()

# --- Input at BOTTOM + auto-clear using key trick ---
user_input = st.text_input(
    "Your message",
    placeholder="Type your question and press Enter...",
    key=f"input_{st.session_state.input_key}"  # changing key = clears the box
)

if user_input:
    with st.spinner("🐇 Hopping through thoughts..."):
        response = st.session_state.agent.run(user_input)

    # Save to chat history
    st.session_state.chat_history.append((user_input, response))

    # Clear text box by incrementing key
    st.session_state.input_key += 1

    # Rerun to refresh UI
    st.rerun()