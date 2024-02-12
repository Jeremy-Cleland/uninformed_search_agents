import matplotlib.pyplot as plt
import numpy as np


def visualize_maze(maze):
    """
    Visualizes the maze grid.

    Args:
        maze (np.array): A 2D numpy array representing the maze.
    """
    fig, ax = plt.subplots()
    ax.imshow(maze, cmap=plt.cm.Dark2)
    ax.grid(which="major", axis="both", linestyle="-", color="k", linewidth=2)
    ax.set_xticks(np.arange(-0.5, maze.shape[1], 1))
    ax.set_yticks(np.arange(-0.5, maze.shape[0], 1))

    # Label start and goal
    start = np.where(maze == "S")
    goal = np.where(maze == "G")
    ax.text(start[1], start[0], "S", va="center", ha="center", color="white")
    ax.text(goal[1], goal[0], "G", va="center", ha="center", color="white")

    plt.show()
