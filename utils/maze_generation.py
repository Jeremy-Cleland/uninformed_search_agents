"""
Necessary imports:
- random
- numpy as np
"""

import random
import numpy as np


def generate_maze(size=10, density=0.2):
    """
    Generates a random maze of a given size and obstacle density, with random start and goal positions.

    Parameters:
    - size (int): The size of the maze (size x size), defaults to 10.
    - density (float): The density of obstacles in the maze, between 0 and 1, defaults to 0.2.

    Returns:
    - np.array: A 2D numpy array representing the maze, where '.' denotes open cells,
      'X' denotes obstacles, 'S' denotes the start, and 'G' denotes the goal.
    """
    # Create an empty maze
    maze = np.full((size, size), ".")

    # Randomly place obstacles in the maze
    for row in range(size):
        for col in range(size):
            if random.random() < density:
                maze[row, col] = "X"

    # Randomly place the start and goal positions
    start, goal = (0, 0), (size - 1, size - 1)
    while start == goal or maze[start] == "X" or maze[goal] == "X":
        start = (random.randint(0, size - 1), random.randint(0, size - 1))
        goal = (random.randint(0, size - 1), random.randint(0, size - 1))

    maze[start] = "S"
    maze[goal] = "G"

    return maze


maze = generate_maze()
print(maze)
