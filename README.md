# AI-ChatBot-LLM---OLLAMA

# 🤖 Agentic AI Chatbot — Powered by Groq + Streamlit

A fully working AI chatbot agent built with Python, deployed free on Streamlit Cloud, using the Groq API (free tier) to run Llama 3 — no paid API, no local GPU needed.

---

## 🌐 Live Demo

👉 [Demo](https://placebo.streamlit.app/)

---

## 🧠 What Did I Actually Build?

Think of this like a **smart restaurant.**

Most people think AI apps are just "you type something, AI replies." But there's a lot more happening behind the scenes. In this project, there are **5 separate parts**, each doing a specific job — just like a restaurant has a counter, a waiter, a chef, a notebook, and kitchen machines.

Here's the analogy:

| File | Real Role | Restaurant Analogy |
|---|---|---|
| `app_ui.py` | Web interface | 🏪 Front counter where customer orders |
| `agent.py` | Decision maker | 🧑‍💼 Waiter who decides what to do |
| `llm.py` | AI brain | 👨‍🍳 Head chef who generates the answer |
| `memory.py` | Chat history | 📒 Waiter's notebook |
| `tools.py` | Extra abilities | 🔧 Kitchen machines (calculator, search) |

---

## 📁 Project Structure

```
agentic-agent/
│
├── app_ui.py        # Streamlit web UI (run this)
├── agent.py         # Agent brain — decision logic
├── llm.py           # Groq API connection
├── memory.py        # Conversation memory
├── tools.py         # Calculator + place search tools
└── requirements.txt # Python dependencies
```

---

## 🔄 Full Flow — How It Works Step by Step

```
User types a message
        ↓
🏪 app_ui.py receives it
        ↓
🧑‍💼 agent.py decides what to do
        ↓
    ┌─────────────────────────────┐
    │  Does it need a tool?        │
    │  "calculate 5+5" → 🔧 tool  │
    │  "find a place" → 🔧 tool   │
    │  anything else → 👨‍🍳 LLM    │
    └─────────────────────────────┘
        ↓
👨‍🍳 llm.py sends message to Groq API
        ↓
📒 memory.py stores the conversation
        ↓
Answer returned to UI and shown to user
```

---

## 🏪 1. `app_ui.py` — The Front Counter

This is what the user sees. Built with **Streamlit** — a Python library that turns your script into a website with zero HTML or CSS.

```python
user_input = st.text_input("Ask something")

if user_input:
    response = agent.run(user_input)
    st.write("AI:", response)
```

**What it does:**
- Shows a text box for the user to type in
- Sends whatever they typed to the Agent
- Displays the final answer back on screen

**Restaurant analogy:**
> The customer walks up to the counter, places an order, and the counter staff passes it to the waiter. The customer just waits and receives the food — they never see what happens in the kitchen.

---

## 🧑‍💼 2. `agent.py` — The Waiter (The Brain)

This is the most important file. The agent is the **decision maker**. It reads the user's message and decides:

- Is this a math question? → use the calculator tool
- Is this asking about places? → use the search tool
- Anything else? → ask the LLM (Groq AI)

```python
if "calculate" in user_input.lower():
    result = calculator(...)
    return f"🧮 Result: {result}"

if "place" in user_input.lower():
    result = search_places("beach")
    return f"📍 Places: {result}"

# otherwise, ask the AI
response = call_llm(self.memory.get())
```

**Restaurant analogy:**
> The waiter listens to the customer's order. If they want a drink → goes to the drinks machine. If they want a dessert → checks the fridge. If they want a full meal → tells the head chef. The waiter uses judgment so the chef doesn't have to handle everything.

---

## 👨‍🍳 3. `llm.py` — The Head Chef (Groq AI)

This file connects to the **Groq API** and sends messages to the **Llama 3** AI model hosted on Groq's servers.

```python
client = Groq(api_key=st.secrets["GROQ_API_KEY"])
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=clean
)
return response.choices[0].message.content
```

**What it does:**
- Takes the full conversation history
- Sends it to Groq's cloud servers
- Gets back an AI-generated reply

**Why Groq?** It runs Llama 3 (Meta's open-source AI) for **free**, with no credit card needed, and it's extremely fast.

**Restaurant analogy:**
> The head chef receives the order from the waiter, uses their skill and knowledge to prepare the perfect dish, and hands it back. The chef doesn't talk to the customer directly — the waiter handles that.

---

## 📒 4. `memory.py` — The Notebook

Without memory, the AI forgets every message as soon as it replies. This file stores the full conversation so the AI has **context** — just like how ChatGPT remembers what you said earlier in a chat.

```python
class Memory:
    def __init__(self):
        self.messages = []

    def add(self, role, content):
        self.messages.append({"role": role, "content": content})

    def get(self):
        return self.messages
```

**What it does:**
- Stores every message (user + AI) in a list
- That list is sent to Groq with every new request
- So the AI always knows the full context of the conversation

**Restaurant analogy:**
> The waiter's notebook. Every order, every request, every special instruction is written down. When the chef needs context ("what did this table order before?"), the waiter reads from the notebook.

---

## 🔧 5. `tools.py` — The Kitchen Machines

These are extra abilities the agent can use without asking the AI — faster and more accurate for specific tasks.

```python
def calculator(expression):
    try:
        return eval(expression)
    except:
        return "Invalid expression"

def search_places(query):
    data = {
        "beach": ["Miami Beach", "Clearwater Beach"],
        "nature": ["Everglades", "Blue Spring"],
        "city": ["New York", "Los Angeles"]
    }
    return data.get(query, ["No results found"])
```

**What it does:**
- `calculator` — evaluates any math expression instantly
- `search_places` — returns a hardcoded list of places by category

**Restaurant analogy:**
> The kitchen machines. The waiter doesn't ask the chef to squeeze juice — they just use the juicer machine. Faster, simpler, no chef needed for simple tasks.

---

## 🚀 Tech Stack

| Technology | Purpose | Cost |
|---|---|---|
| **Python** | Main language | Free |
| **Streamlit** | Web UI | Free |
| **Groq API** | Run Llama 3 AI | Free tier |
| **Llama 3.3 70B** | AI model | Free via Groq |
| **Streamlit Cloud** | Deployment/hosting | Free |

**Total cost: $0** 💰

---

## 🛠️ How to Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/agentic-agent.git
cd agentic-agent
```

### 2. Install dependencies
```bash
pip install streamlit groq
```

### 3. Add your Groq API key
Get your free key at [console.groq.com](https://console.groq.com)

Create a file `.streamlit/secrets.toml`:
```toml
GROQ_API_KEY = "gsk_your_key_here"
```

### 4. Run the app
```bash
streamlit run app_ui.py
```

---

## ☁️ How to Deploy Free on Streamlit Cloud

1. Push this repo to GitHub
2. Go to [share.streamlit.io]([https://share.streamlit.io](https://placebo.streamlit.app/))
3. Connect your GitHub account
4. Select this repo, set main file to `app_ui.py`
5. Go to **Settings → Secrets** and add:
```toml
GROQ_API_KEY = "gsk_your_key_here"
```
6. Click **Deploy** — live in 2 minutes ✅

---

## 💡 What I Learned Building This

- How an **AI agent** works (it's not just one file — it's a system)
- The difference between an **LLM** (the brain) and an **agent** (the decision maker)
- How **memory/context** makes AI feel like a real conversation
- How to connect to a **real AI API** (Groq)
- How to **deploy a Python app** online for free

---

## 🔥 What Could Be Added Next

- 💬 Chat bubble UI (like real ChatGPT)
- 🧠 Long-term memory using a vector database
- 🌐 Web search tool (like Perplexity AI)
- 🤖 Multi-agent system (planner + executor agents)
- 📄 Upload and read PDF files

---

## 👤 Author

Built by **[RISHI SONI]** — learning AI engineering one project at a time.

> ⭐ If you found this useful, give it a star on GitHub!
