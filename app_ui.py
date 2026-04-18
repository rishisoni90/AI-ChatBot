import streamlit as st
from memory import Memory
from agent import Agent

memory = Memory()
agent = Agent(memory)

# --- Page Config ---
st.set_page_config(page_title="Rabbit AI", page_icon="🐇", layout="centered")

# --- Custom CSS ---
st.markdown("""
    <style>
        .rabbit-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            margin-bottom: 10px;
        }
        .title {
            text-align: center;
            font-size: 2rem;
            font-weight: bold;
        }
        .subtitle {
            text-align: center;
            color: gray;
            font-size: 0.9rem;
            margin-bottom: 20px;
        }
        .ai-bubble {
            background-color: #f0f0f0;
            border-radius: 15px;
            padding: 12px 18px;
            margin-top: 10px;
            font-size: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Rabbit GIF (idle by default) ---
rabbit_placeholder = st.empty()

# Show idle rabbit
with rabbit_placeholder.container():
    st.markdown('<div class="rabbit-container">', unsafe_allow_html=True)
    st.image("rabbit.gif", width=150)
    st.markdown('</div>', unsafe_allow_html=True)

# --- Title ---
st.markdown('<div class="title">Rabbit AI Assistant 🐇</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ask me anything, I\'ll hop right on it!</div>', unsafe_allow_html=True)

# --- Input ---
user_input = st.text_input("", placeholder="Type your question here...")

# --- Response ---
if user_input:
    # While thinking - swap to thinking gif if you have one
    # rabbit_placeholder.image("rabbit_think.gif", width=150)  # optional

    with st.spinner("🐇 Hopping through thoughts..."):
        response = agent.run(user_input)

    # Show response in a nice bubble
    st.markdown(f"""
        <div class="ai-bubble">
            🐇 <b>Rabbit AI:</b><br>{response}
        </div>
    """, unsafe_allow_html=True)