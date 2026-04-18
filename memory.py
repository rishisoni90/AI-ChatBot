class Memory:
    def __init__(self):
        self.messages = []  # start empty, no fake messages

    def add(self, role, content):
        self.messages.append({"role": role, "content": content})

    def get(self):
        return self.messages