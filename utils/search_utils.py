# utils/search_utils.py


def get_successors(maze, state):
    directions = [
        ("UP", (0, -1)),
        ("DOWN", (0, 1)),
        ("LEFT", (-1, 0)),
        ("RIGHT", (1, 0)),
    ]
    successors = []
    for action, (dx, dy) in directions:
        next_state = (state[0] + dx, state[1] + dy)
        if is_valid(maze, next_state):
            successors.append((action, next_state))
    return successors


def is_valid(maze, state):
    x, y = state
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != "X"


def find_positions(maze, symbol):
    for x, row in enumerate(maze):
        for y, cell in enumerate(row):
            if cell == symbol:
                return (x, y)


def reconstruct_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]  # Reverse the path to start from the beginning
