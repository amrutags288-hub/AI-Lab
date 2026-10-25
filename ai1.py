
class SimpleReflexVacuumAgent:
    def __init__(self):
        self.location = "A"
        self.percept_sequence = []
        self.actions = []

    def add_percept(self, location, is_dirty):
        self.percept_sequence.append((location, is_dirty))

    def add_action(self, action):
        self.actions.append(action)

    def execute_actions(self):
        for action in self.actions:
            percept = self.percept_sequence.pop(0)
            print(f"Percept: {percept} - Action: {action}")

            if action == "Suck":
                print("Vacuuming dirt.")

            elif action == "MoveLeft":
                self.location = "A"
                print("Moving left to location A.")

            elif action == "MoveRight":
                self.location = "B"
                print("Moving right to location B.")

            elif action == "DoNothing":
                print("Doing nothing.")


def simple_reflex_vacuum_agent(percept_sequence):
    agent = SimpleReflexVacuumAgent()

    for percept in percept_sequence:
        location, is_dirty = percept
        agent.add_percept(location, is_dirty)

        if is_dirty:
            agent.add_action("Suck")
        else:
            if location == "A":
                agent.add_action("MoveRight")
            elif location == "B":
                agent.add_action("MoveLeft")

    return agent


# Example percept sequence
percept_sequence = [
    ("A", True),
    ("A", False),
    ("B", True),
    ("B", False)
]

# Create and run the agent
agent = simple_reflex_vacuum_agent(percept_sequence)
agent.execute_actions()
