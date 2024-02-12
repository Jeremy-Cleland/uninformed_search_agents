from collections import deque
import numpy as np
from utils.node import Node
from utils.search_utils import get_successors, find_positions


def bfs_search(maze):
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
    start, goal = find_positions(maze, "S"), find_positions(maze, "G")
    frontier = deque([Node(start)])
    explored = set()
    start_node = Node(start)  # Create a Node object for the start position
    steps = [create_maze_state(maze, explored, start_node, None)]  # Use start_node here

    while frontier:
        current_node = frontier.popleft()
        if current_node.state == goal:
            steps.append(
                create_maze_state(maze, explored, goal, goal)
            )  # Final visualization step
            return [node.state for node in current_node.path()], len(explored), steps

        explored.add(current_node.state)
        steps.append(
            create_maze_state(maze, explored, current_node.state, goal)
        )  # Visualization at current step

        for action, next_state in get_successors(maze, current_node.state):
            if (
                next_state not in explored
                and maze[next_state] != "X"
                and all(next_state != node.state for node in frontier)
            ):
                child = Node(next_state, current_node, action)
                frontier.append(child)

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
