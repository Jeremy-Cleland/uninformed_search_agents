# path/filename: search_algorithms/dfs.py
from utils.node import Node
from utils.search_utils import get_successors, find_positions, reconstruct_path


def dfs_search(maze):
    """
    Performs Depth-First Search (DFS) to find a path through the maze from start ('S') to goal ('G').

    Parameters
    ----------
    maze : list of list of str
        A 2D numpy array representing the maze, with 'S' for start, 'G' for goal, '.' for open paths, and 'X' for obstacles.

    Returns
    -------
    list of tuple
        The path from the start to the goal as a list of (x, y) tuples, if a path is found, otherwise None.

        The number of nodes expanded during the search.

    """
    start, goal = find_positions(maze, "S"), find_positions(maze, "G")
    frontier = [Node(start)]
    explored = set()

    while frontier:
        current_node = frontier.pop()  # LIFO
        if current_node.state == goal:
            return (
                reconstruct_path(current_node),
                len(explored),
            )  # Backtrack to get the path
        explored.add(current_node.state)

        for action, state in get_successors(maze, current_node.state):
            if state not in explored and maze[state] != "X":
                frontier.append(Node(state, current_node, action))

    return None, len(explored)
