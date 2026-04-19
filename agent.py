# agent.py
import json
from llm import call_llm
from tools import calculator, search_places, TOOLS

# map tool names to actual functions
TOOL_MAP = {
    "calculator":    calculator,
    "search_places": search_places
}

class Agent:
    def __init__(self, memory):
        self.memory = memory
        self.memory.add("user", "You are a helpful AI assistant.")
        self.memory.add("assistant", "Understood! How can I help?")

    def run(self, user_input):
        self.memory.add("user", user_input)

        # STEP 1: Ask Llama 3 — should I use a tool or answer directly?
        response = call_llm(self.memory.get(), tools=TOOLS)

        # STEP 2: Did Llama 3 decide to use a tool?
        if response["type"] == "tool_call":
            tool_name = response["tool"]        # e.g. "calculator"
            tool_args = response["args"]        # e.g. {"expression": "5+5"}

            # STEP 3: Run the actual tool function
            tool_fn = TOOL_MAP.get(tool_name)
            if tool_fn:
                result = tool_fn(**tool_args)
            else:
                result = "Tool not found"

            # STEP 4: Send tool result back to Llama 3 for final answer
            self.memory.add("user", f"Tool result: {result}")
            final = call_llm(self.memory.get())
            self.memory.add("assistant", final["text"])
            return f"🔧 [{tool_name}] → {result}\n\n{final['text']}"

        # STEP 5: No tool needed — just return Llama 3's answer
        self.memory.add("assistant", response["text"])
        return response["text"]