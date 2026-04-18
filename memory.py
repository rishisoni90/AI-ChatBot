class Memory:
    def __init__(self):
        # Use user role instead of system to avoid Groq compatibility issues
        self.messages = [
            {"role": "user", "content": "You are a helpful AI assistant. Remember this for our conversation."},
            {"role": "assistant", "content": "Understood! I am a helpful AI assistant. How can I help you today?"}
        ]

    def add(self, role, content):
        self.messages.append({"role": role, "content": content})

    def get(self):
        return self.messages