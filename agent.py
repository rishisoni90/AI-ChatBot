from llm import call_llm
from tools import calculator, search_places

class Agent:
    def __init__(self, memory):
        self.memory = memory

    def run(self, user_input):

        # store user input
        self.memory.add("user", user_input)

        # STEP 1: TOOL usage (check keywords first, no LLM needed)
        if "calculate" in user_input.lower():
            result = calculator(user_input.replace("calculate", "").strip())
            return f"🧮 Result: {result}"

        if "place" in user_input.lower():
            result = search_places("beach")
            return f"📍 Places: {result}"

        # STEP 2: NORMAL LLM response
        response = call_llm(self.memory.get())

        self.memory.add("assistant", response)

        return response