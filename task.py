class Task:
    def __init__(self, name, priority, order):
        self.name = name
        self.priority = priority
        self.order = order

    def __repr__(self):
        return f"{self.name} (Priority {self.priority})"

    def __lt__(self, other):
        if self.priority != other.priority:
            return self.priority < other.priority
        return self.order > other.order  # reverse for min comparison

    def __gt__(self, other):
        if self.priority != other.priority:
            return self.priority > other.priority
        return self.order < other.order