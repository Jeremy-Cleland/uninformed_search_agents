def get_successors(maze, state):
    """
    Return the valid successors of a given state in a maze.

    Parameters:
    - maze (list of lists): The maze represented as a 2D list.
    - state (tuple): The current state represented as a tuple of coordinates (x, y).

    Returns:
    - successors (list of tuples): A list of valid successors, where each successor is represented as a tuple of an action and the next state.

    Example:
    >>> maze = [
    ...     [" ", " ", " ", " ", " "],
    ...     [" ", "X", "X", " ", " "],
    ...     [" ", " ", " ", "X", " "],
    ...     [" ", "X", " ", " ", " "],
    ...     [" ", " ", " ", " ", " "]
    ... ]
    >>> state = (2, 2)
    >>> get_successors(maze, state)
    [("UP", (1, 2)), ("DOWN", (3, 2)), ("LEFT", (2, 1)), ("RIGHT", (2, 3))]

    Note:
    - The maze is represented as a 2D list, where each element represents a cell in the maze.
    - The state is represented as a tuple of coordinates (x, y), where (0, 0) is the top-left corner of the maze.
    - The successors are determined by checking the validity of the next state after applying each action in the directions list.
    - A successor is considered valid if the next state is within the boundaries of the maze and the corresponding cell is not marked as "X".
    """
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
    """
    Check if a given state is valid in a maze.

    Parameters:
    - maze (list of lists): The maze represented as a 2D list.
    - state (tuple): The current state represented as a tuple of coordinates (x, y).

    Returns:
    - valid (bool): True if the state is valid, False otherwise.

    Example:
    >>> maze = [
    ...     [" ", " ", " ", " ", " "],
    ...     [" ", "X", "X", " ", " "],
    ...     [" ", " ", " ", " ", " "]
    ... ]
    >>> state = (2, 2)
    >>> is_valid(maze, state)
    True

    Note:
    - The maze is represented as a 2D list, where each element represents a cell in the maze.
    - The state is represented as a tuple of coordinates (x, y), where (0, 0) is the top-left corner of the maze.
    - A state is considered valid if it is within the boundaries of the maze and the corresponding cell is not marked as "X".
    """

    x, y = state
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != "X"


def find_positions(maze, symbol):
    """
    Check if a given state is valid in a maze.

    Parameters:
    - maze (list of lists): The maze represented as a 2D list.
    - state (tuple): The current state represented as a tuple of coordinates (x, y).

    Returns:
    - valid (bool): True if the state is valid, False otherwise.

    Example:
    >>> maze = [
    ...     [" ", " ", " ", " ", " "],
    ...     [" ", "X", "X", " ", " "],
    ...     [" ", " ", " ", " ", " "]
    ... ]
    >>> state = (2, 2)
    >>> is_valid(maze, state)
    True

    Note:
    - The maze is represented as a 2D list, where each element represents a cell in the maze.
    - The state is represented as a tuple of coordinates (x, y), where (0, 0) is the top-left corner of the maze.
    - A state is considered valid if it is within the boundaries of the maze and the corresponding cell is not marked as "X".
    """
    for x, row in enumerate(maze):
        for y, cell in enumerate(row):
            if cell == symbol:
                return (x, y)


def reconstruct_path(node):
    """
    Reconstructs the path from a given node to the starting node.

    Parameters:
        node (Node): The node from which to start reconstructing the path.

    Returns:
        list: The reconstructed path as a list of states, starting from the beginning.

    Example:
        >>> node = Node(state=3, parent=Node(state=2, parent=Node(state=1, parent=None)))
        >>> reconstruct_path(node)
        [1, 2, 3]
    """
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]  # Reverse the path to start from the beginning
