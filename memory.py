class Memory:
    def __init__(self):
        self.messages = [
            {"role": "user", "content": "You are a helpful AI assistant."},
            {"role": "assistant", "content": "I am a helpful AI assistant. How can I help you?"}
        ]

    def add(self, role, content):
        self.messages.append({"role": role, "content": content})

    def get(self):
        return self.messages