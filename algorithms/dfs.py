import numpy as np

from utils.node import Node
from utils.search_utils import get_successors, find_positions


def dfs_search(maze):
    """
    Performs a depth-first search (DFS) on a maze to find a path from the start position to the goal position.

    Parameters:
    - maze (list of lists): The maze represented as a 2D list, where each element represents a cell in the maze.

    Returns:
    - path (list): A list of tuples representing the sequence of positions from the start to the goal.
    - num_explored (int): The number of nodes explored during the search.
    - steps (list): A list of numpy arrays representing the maze state at each step of the search.

    Notes:
    - The start position in the maze should be marked as "S" and the goal position should be marked as "G".
    - The maze can contain walls marked as "X" and empty spaces marked as " ".
    - The search algorithm uses a stack (LIFO) to keep track of the frontier of nodes to explore.
    - The search algorithm explores nodes until the goal position is reached or there are no more nodes to explore.
    - At each step of the search, the current maze state is visualized by marking the explored nodes as "E" and the current node as "C".
    - The function returns the path from the start to the goal, the number of nodes explored, and the maze state at each step of the search.
    """
    start, goal = find_positions(maze, "S"), find_positions(maze, "G")
    frontier = [Node(start)]
    start_node = Node(start)
    explored = set()
    steps = [create_maze_state(maze, explored, start_node, goal)]

    while frontier:
        current_node = frontier.pop()  # LIFO
        explored.add(current_node.state)

        if current_node.state == goal:
            path = [node.state for node in current_node.path()]
            steps.append(
                create_maze_state(maze, explored, goal, None)
            )  # Visualization of the final path
            return path, len(explored), steps

        for action, state in get_successors(maze, current_node.state):
            if state not in explored and maze[state] != "X":
                child = Node(state, current_node, action)
                frontier.append(child)
                # Visualization at this step before exploring the child node
                steps.append(
                    create_maze_state(maze, explored.union({state}), child, None)
                )

    return None, len(explored), steps


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
    maze_state = np.array(maze, dtype="object")
    for state in explored:
        maze_state[state] = "E"  # Mark explored nodes
    if current_node:
        # Check if current_node is a Node object or a tuple and act accordingly
        current_pos = (
            current_node.state if isinstance(current_node, Node) else current_node
        )
        maze_state[current_pos] = "C"  # Mark the current node
    if goal:
        maze_state[goal] = "G"  # Ensure the goal is always marked
    return maze_state
