from llm import call_llm
from tools import calculator, search_places

class Agent:
    def __init__(self, memory):
        self.memory = memory

    def run(self, user_input):

        # store user input
        self.memory.add("user", user_input)

        # STEP 1: simple decision logic
        decision = call_llm([
            {"role": "system", "content": "Decide: tool or final answer"},
            {"role": "user", "content": user_input}
        ])

        decision = decision.lower()

        # STEP 2: TOOL usage
        if "calculate" in user_input:
            result = calculator(user_input.replace("calculate", "").strip())
            return f"🧮 Result: {result}"

        if "place" in user_input:
            result = search_places("beach")
            return f"📍 Places: {result}"

        # STEP 3: NORMAL LLM response
        response = call_llm(self.memory.get())

        self.memory.add("assistant", response)

        return response