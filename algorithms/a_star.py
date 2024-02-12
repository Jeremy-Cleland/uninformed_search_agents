# path/filename: search_algorithms/a_star.py
import heapq

from utils.node import Node
from utils.search_utils import get_successors, find_positions, reconstruct_path


def a_star_search(maze):
    start, goal = find_positions(maze, "S"), find_positions(maze, "G")
    frontier = []
    heapq.heappush(frontier, (0, Node(start, None, None, 0)))  # (priority, node)
    explored = set()
    g_scores = {start: 0}  # Cost from start to n

    while frontier:
        _, current_node = heapq.heappop(frontier)
        if current_node.state == goal:
            return reconstruct_path(current_node), len(explored)

        explored.add(current_node.state)

        for action, state in get_successors(maze, current_node.state):
            if state not in explored:
                g = g_scores[current_node.state] + 1  # Assuming cost = 1 per move
                h = manhattan_distance(state, goal)
                f = g + h

                if (
                    state not in g_scores or g < g_scores[state]
                ):  # Check for a better path
                    g_scores[state] = g
                    heapq.heappush(frontier, (f, Node(state, current_node, action, g)))

    return None, len(explored)


def manhattan_distance(a, b):

    return abs(a[0] - b[0]) + abs(a[1] - b[1])
