class Task:
    def __init__(self, name, priority,order):
        self.name = name
        self.priority = priority
        self.order = order

    def __repr__(self):
        return f"{self.name} (Priority {self.priority})"

    def __lt__(self, other):
        return self.priority < other.priority

    def __gt__(self, other):
        return self.priority > other.priority