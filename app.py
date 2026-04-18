from memory import Memory
from agent import Agent

memory = Memory()
agent = Agent(memory)

print("Agent started (type 'exit' to stop)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = agent.run(user_input)
    print("AI:", response)