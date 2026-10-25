
from collections import deque

def get_initial_state(num_disks):
    return (tuple(range(num_disks, 0, -1)), (), ())

def get_goal_state(num_disks):
    return ((), (), tuple(range(num_disks, 0, -1)))

def get_successors(state):
    successors = []

    for source in range(3):
        for target in range(3):
            if source == target:
                continue

            if not state[source]:
                continue

            disk = state[source][-1]

            if state[target] and state[target][-1] < disk:
                continue

            new_state = [list(peg) for peg in state]
            new_state[source].pop()
            new_state[target].append(disk)

            next_state = tuple(tuple(peg) for peg in new_state)
            action = (source, target)

            successors.append((next_state, action))

    return successors

def solve_hanoi_state_space(num_disks):
    start = get_initial_state(num_disks)
    goal = get_goal_state(num_disks)

    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        for next_state, action in get_successors(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [action]))

    return None

def print_solution(num_disks, path):
    if path is None:
        print("No solution found.")
        return

    print("Solved Tower of Hanoi for", num_disks, "disks")
    print("Minimum moves required:", len(path))

    peg_map = {0: "A", 1: "B", 2: "C"}

    for i, (src, dst) in enumerate(path, 1):
        print("Step", i, ": Move disk from",
              peg_map[src], "to", peg_map[dst])

# Run the program
disks = 3
solution = solve_hanoi_state_space(disks)
print_solution(disks, solution)
