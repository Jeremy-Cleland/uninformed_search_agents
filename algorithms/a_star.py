# path/filename: search_algorithms/a_star.py
import heapq
import numpy as np
from utils.node import Node
from utils.search_utils import get_successors, find_positions


def a_star_search(maze):
    """
    Performs A* search algorithm to find the shortest path from the start position to the goal position in a given maze.

    Parameters:
    - maze (list of lists): The maze represented as a 2D list, where each element represents a cell in the maze. The maze can contain the following symbols:
        - " ": Empty cell
        - "X": Obstacle cell
        - "S": Start cell
        - "G": Goal cell

    Returns:
    - path (list): A list of tuples representing the coordinates of the cells in the shortest path from the start position to the goal position.
    - num_explored (int): The number of nodes explored during the search process.
    - steps (list): A list of maze states representing the search process. Each maze state is a 2D list with the same dimensions as the input maze, where each element represents a cell in the maze. The maze states show the progression of the search, with the following symbols:
        - " ": Empty cell
        - "X": Obstacle cell
        - "S": Start cell
        - "G": Goal cell
        - "E": Explored cell
        - "P": Path cell

    Example:
    >>> maze = [
    ...     [" ", " ", " ", " ", " "],
    ...     [" ", "X", "X", " ", " "],
    ...     [" ", " ", " ", "X", " "],
    ...     [" ", "X", " ", " ", " "],
    ...     [" ", " ", " ", " ", " "]
    ... ]
    >>> path, num_explored, steps = a_star_search(maze)
    >>> print(path)
    [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
    >>> print(num_explored)
    9
    >>> print(steps)
    [
        [
            ["S", " ", " ", " ", " "],
            [" ", "X", "X", " ", " "],
            [" ", " ", " ", "X", " "],
            [" ", "X", " ", " ", " "],
            [" ", " ", " ", " ", " "]
        ],
        ...
        [
            ["P", "P", "P", "P", "P"],
            [" ", "X", "X", " ", " "],
            [" ", " ", " ", "X", " "],
            [" ", "X", " ", " ", " "],
            [" ", " ", " ", " ", "G"]
        ]
    ]

    Note:
    - The A* search algorithm uses a priority queue (frontier) to explore the nodes with the lowest cost first.
    - The cost of a node is the sum of the cost to reach that node from the start position (g-score) and the estimated cost to reach the goal position from that node (h-score).
    - The g-score is the number of steps taken to reach the current node from the start position.
    - The h-score is the Manhattan distance between the current node and the goal position.
    - The search process stops when the goal position is reached or when there are no more nodes to explore.
    - The function returns the shortest path from the start position to the goal position, the number of nodes explored, and the maze states representing the search process.
    """
    start, goal = find_positions(maze, "S"), find_positions(maze, "G")
    frontier = []
    start_node = Node(start)
    heapq.heappush(
        frontier, (0, next(Node.id_generator), start_node)
    )  # Start node with initial cost 0
    explored = set()
    g_scores = {start: 0}  # Dictionary to keep track of the lowest cost to reach a node
    steps = [create_maze_state(maze, explored, start_node, goal)]

    while frontier:
        current_f, _, current_node = heapq.heappop(frontier)

        if current_node.state == goal:
            # Optional: Record final state for visualization
            steps.append(create_maze_state(maze, explored, current_node, goal))
            return [node.state for node in current_node.path()], len(explored), steps

        explored.add(current_node)
        # Optional: Record current state for visualization
        steps.append(create_maze_state(maze, explored, current_node, goal))

        for action, state in get_successors(maze, current_node.state):
            if state not in explored or state not in [
                node.state for _, _, node in frontier
            ]:
                g = (
                    g_scores[current_node.state] + 1
                )  # Assuming uniform cost for simplicity
                h = manhattan_distance(state, goal)
                f = g + h

                if state not in g_scores or g < g_scores[state]:
                    g_scores[state] = g
                    heapq.heappush(
                        frontier,
                        (
                            f,
                            next(Node.id_generator),
                            Node(state, current_node, action, g),
                        ),
                    )

    return None, len(explored), steps


def manhattan_distance(a, b):
    """
    Calculates the Manhattan distance between two points in a 2D grid.

    Parameters:
    - a (tuple): The coordinates of the first point in the grid.
    - b (tuple): The coordinates of the second point in the grid.

    Returns:
    - distance (int): The Manhattan distance between the two points.

    Example:
    >>> point1 = (0, 0)
    >>> point2 = (3, 4)
    >>> manhattan_distance(point1, point2)
    7

    Note:
    The Manhattan distance is the sum of the absolute differences between the x-coordinates and the y-coordinates of the two points. It represents the minimum number of moves required to reach one point from the other, considering only horizontal and vertical movements.
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def create_maze_state(maze, explored, current_node, goal):
    """
    Creates a new maze state by marking the explored nodes, the current node, and the goal position.

    Parameters:
    - maze (list of lists): The maze represented as a 2D list.
    - explored (set): A set of tuples representing the positions of the explored nodes.
    - current_node (Node or tuple): The current node or position.
    - goal (tuple): The goal position.

    Returns:
    - maze_state (numpy array): The updated maze state with the explored nodes, current node, and goal marked.

    Notes:
    - The function modifies the original maze state by marking the explored nodes as "E", the current node as "C", and the goal position as "G".
    - The function returns the updated maze state as a numpy array.

    """
    maze_state = np.array(
        maze, dtype="object"
    )  # Copy the maze to avoid altering the original
    for node in explored:
        maze_state[node.state] = "E"  # Mark explored nodes
    path = [node.state for node in current_node.path()]
    for state in path:
        maze_state[state] = "P"  # Mark path nodes
    maze_state[goal] = "G"  # Ensure the goal is always marked
    return maze_state
