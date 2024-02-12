# path/filename: search_algorithms/bfs.py
from collections import deque
from utils.node import Node
from utils.search_utils import get_successors, find_positions, reconstruct_path


def bfs_search(maze):
    start, goal = find_positions(maze, "S"), find_positions(maze, "G")
    frontier = deque([Node(start)])
    explored = set()

    while frontier:
        current_node = frontier.popleft()  # FIFO
        if current_node.state == goal:
            return reconstruct_path(current_node), len(
                explored
            )  # Backtrack to get the path

        explored.add(current_node.state)

        for action, state in get_successors(maze, current_node.state):
            if state not in explored and maze[state[0]][state[1]] != "X":
                explored.add(state)  # Mark this state as explored
                frontier.append(Node(state, current_node, action))

    return None, len(explored)
