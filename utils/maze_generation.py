# path/filename: search_algorithms/maze_generation.py
import random
import numpy as np


def generate_maze(size=10, density=0.2):
    """
    Generates a random maze of a given size and obstacle density.

    Parameters
    ----------
    size : int, optional
        The size of the maze (size x size), by default 10.
    density : float, optional
        The density of obstacles in the maze, between 0 and 1, by default 0.2.

    Returns
    -------
    np.array
        A 2D numpy array representing the maze, where '.' denotes open cells,
        'X' denotes obstacles, 'S' denotes the start, and 'G' denotes the goal.
    """
    # Create an empty maze with all open cells
    maze = np.full((size, size), ".")

    # Randomly fill the maze with obstacles based on the specified density
    for row in range(size):
        for col in range(size):
            if random.random() < density:
                maze[row, col] = "X"

    # Set start and goal positions
    start, goal = (0, 0), (size - 1, size - 1)
    maze[start] = "S"
    maze[goal] = "G"

    return maze


# Example usage
maze = generate_maze()
print(maze)
