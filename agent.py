from llm import call_llm
from tools import calculator, search_places

class Agent:
    def __init__(self, memory):
        self.memory = memory
        # Add system instruction as first user message once
        self.memory.add("user", "You are a helpful AI assistant. Answer clearly and helpfully.")
        self.memory.add("assistant", "Understood! I am ready to help you.")

    def run(self, user_input):

        # STEP 1: TOOL usage (no LLM needed)
        if "calculate" in user_input.lower():
            result = calculator(user_input.replace("calculate", "").strip())
            return f"🧮 Result: {result}"

        if "place" in user_input.lower():
            result = search_places("beach")
            return f"📍 Places: {result}"

        # STEP 2: store user input
        self.memory.add("user", user_input)

        # STEP 3: get LLM response
        response = call_llm(self.memory.get())

        # STEP 4: store assistant response
        self.memory.add("assistant", response)

        return response