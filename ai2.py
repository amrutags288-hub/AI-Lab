
import heapq

GOAL = (1, 2, 3, 8, 0, 4, 7, 6, 5)

def heuristic(state):
    count = 0
    for i in range(9):
        if state[i] != 0 and state[i] != GOAL[i]:
            count += 1
    return count

def get_neighbors(state):
    neighbors = []
    blank = state.index(0)

    moves = [-3, 3, -1, 1]

    for move in moves:
        new = blank + move

        if 0 <= new < 9:
            if move == -1 and blank % 3 == 0:
                continue
            if move == 1 and blank % 3 == 2:
                continue

            board = list(state)
            board[blank], board[new] = board[new], board[blank]
            neighbors.append(tuple(board))

    return neighbors

def astar(start):
    queue = [(heuristic(start), 0, start, [])]
    visited = set()

    while queue:
        f, g, state, path = heapq.heappop(queue)

        if state == GOAL:
            return path + [state]

        if state in visited:
            continue

        visited.add(state)

        for next_state in get_neighbors(state):
            if next_state not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(next_state)

                heapq.heappush(queue, (
                    new_f, new_g, next_state, path + [state]
                ))

    return None

def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

start = (2, 8, 3, 1, 6, 4, 7, 0, 5)

solution = astar(start)

if solution:
    print("Solution found!")
    print("Moves:", len(solution) - 1)

    for step, state in enumerate(solution):
        print("Step", step)
        print_board(state)
else:
    print("No solution found")
