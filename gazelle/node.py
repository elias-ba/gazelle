class Node:
    def __init__(self, state):
        self.state = state
        self.sons = []

    def add_sons(self, new_sons):
        self.sons.extend(new_sons)
        return self

    def __repr__(self):
        return f"Node{self.state, self.sons}"

    def __str__(self):
        return f"Node{self.state, self.sons}"