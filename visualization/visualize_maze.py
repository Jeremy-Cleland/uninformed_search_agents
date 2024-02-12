import matplotlib.pyplot as plt
import numpy as np


def visualize_maze(maze):
    """
    Visualizes the maze grid.

    Args:
        maze (np.array): A 2D numpy array representing the maze.

    returns:
       shiws the maze grid
    """
    maze_mapping = {".": 0, "X": 1, "S": 2, "G": 3}
    numeric_maze = np.array([[maze_mapping[char] for char in row] for row in maze])

    fig, ax = plt.subplots()
    cax = ax.imshow(
        numeric_maze, cmap=plt.cm.Dark2
    )  # Choose a colormap that differentiates the elements clearly
    plt.colorbar(
        cax, ticks=range(len(maze_mapping))
    )  # Optional: Add a colorbar for reference
    plt.show()
