import streamlit as st
from memory import Memory
from agent import Agent

# --- Page Config ---
st.set_page_config(page_title="Rabbit AI", page_icon="🐇", layout="centered")

# --- Init session state ---
if "memory" not in st.session_state:
    st.session_state.memory = Memory()
    st.session_state.agent = Agent(st.session_state.memory)
    st.session_state.chat_history = []
if "input_key" not in st.session_state:
    st.session_state.input_key = 0

# --- Full Custom CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap');

/* === GLOBAL === */
html, body, [class*="css"] {
    font-family: 'Nunito', sans-serif !important;
    background-color: #0f0f1a !important;
    color: #f0f0f0 !important;
}

/* Hide streamlit default elements */
#MainMenu, footer, header { visibility: hidden; }
.block-container {
    padding-top: 1rem !important;
    padding-bottom: 1rem !important;
    max-width: 750px !important;
}

/* === HEADER === */
.header-wrap {
    text-align: center;
    padding: 10px 0 5px 0;
}
.header-wrap img {
    border-radius: 50%;
    border: 3px solid #7c5cbf;
    box-shadow: 0 0 30px #7c5cbf88;
}
.app-title {
    font-size: 2.2rem;
    font-weight: 800;
    background: linear-gradient(90deg, #c084fc, #818cf8, #38bdf8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 8px 0 2px 0;
}
.app-subtitle {
    color: #888;
    font-size: 0.95rem;
    margin-bottom: 15px;
}

/* === CHAT AREA === */
.chat-area {
    background: #16162a;
    border-radius: 18px;
    padding: 18px;
    margin-bottom: 16px;
    min-height: 80px;
    border: 1px solid #2a2a45;
    box-shadow: 0 4px 30px rgba(0,0,0,0.4);
}
.empty-state {
    text-align: center;
    color: #444;
    padding: 30px 0;
    font-size: 1rem;
}

/* === BUBBLES === */
.user-row {
    display: flex;
    justify-content: flex-end;
    margin: 10px 0;
}
.ai-row {
    display: flex;
    justify-content: flex-start;
    margin: 10px 0;
    align-items: flex-start;
    gap: 8px;
}
.user-bubble {
    background: linear-gradient(135deg, #7c3aed, #4f46e5);
    color: white;
    border-radius: 18px 18px 4px 18px;
    padding: 10px 16px;
    max-width: 75%;
    font-size: 0.95rem;
    box-shadow: 0 2px 10px rgba(124,58,237,0.4);
    line-height: 1.5;
}
.ai-bubble {
    background: #1e1e35;
    color: #e8e8f0;
    border-radius: 18px 18px 18px 4px;
    padding: 10px 16px;
    max-width: 75%;
    font-size: 0.95rem;
    border: 1px solid #2e2e50;
    line-height: 1.5;
}
.ai-avatar {
    font-size: 1.4rem;
    margin-top: 2px;
}

/* === INPUT AREA === */
.input-wrap {
    background: #16162a;
    border-radius: 14px;
    border: 1px solid #2e2e55;
    padding: 6px 12px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
}
.stTextInput > div > div > input {
    background: transparent !important;
    border: none !important;
    color: #f0f0f0 !important;
    font-family: 'Nunito', sans-serif !important;
    font-size: 1rem !important;
    box-shadow: none !important;
    padding: 8px 4px !important;
}
.stTextInput > div > div > input::placeholder {
    color: #555 !important;
}
.stTextInput > div {
    border: none !important;
    box-shadow: none !important;
}
label[data-testid="stWidgetLabel"] {
    display: none !important;
}

/* === DIVIDER === */
hr {
    border-color: #2a2a45 !important;
    margin: 10px 0 !important;
}
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
<div class="header-wrap">
    <img src="https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif" width="110"/>
    <div class="app-title">Rabbit AI 🐇</div>
    <div class="app-subtitle">Ask me anything — I'll hop right on it!</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- CHAT HISTORY ---
st.markdown('<div class="chat-area">', unsafe_allow_html=True)

if not st.session_state.chat_history:
    st.markdown('<div class="empty-state">🐇 &nbsp; Say something to get started...</div>', unsafe_allow_html=True)
else:
    for user_msg, ai_msg in st.session_state.chat_history:
        # User bubble (right side)
        st.markdown(f"""
        <div class="user-row">
            <div class="user-bubble">{user_msg}</div>
        </div>
        """, unsafe_allow_html=True)
        # AI bubble (left side)
        st.markdown(f"""
        <div class="ai-row">
            <div class="ai-avatar">🐇</div>
            <div class="ai-bubble">{ai_msg}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --- INPUT AT BOTTOM ---
st.markdown('<div class="input-wrap">', unsafe_allow_html=True)
user_input = st.text_input(
    "msg",
    placeholder="💬  Type your message and press Enter...",
    key=f"input_{st.session_state.input_key}",
    label_visibility="collapsed"
)
st.markdown('</div>', unsafe_allow_html=True)

# --- HANDLE INPUT ---
if user_input:
    with st.spinner("🐇 Thinking..."):
        response = st.session_state.agent.run(user_input)

    st.session_state.chat_history.append((user_input, response))
    st.session_state.input_key += 1
    st.rerun()