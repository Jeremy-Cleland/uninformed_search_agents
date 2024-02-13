import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import FFMpegWriter

plt.rcParams["animation.ffmpeg_path"] = "/opt/homebrew/bin/ffmpeg"


def animate_search_process(
    steps, algorithm, save_animation=True, filename="search_animation.mp4"
):
    """
    Animate the search process on a grid.

    Parameters:
    - steps (list): A list of grid states representing each step of the search process.
    - save_animation (bool, optional): Whether to save the animation as a video file. Default is True.
    - filename (str, optional): The name of the video file to save. Default is "search_animation.mp4".

    Returns:
    None

    The 'animate_search_process' function takes a list of grid states and animates the search process on a grid. Each grid state is represented by a 2D array where each element corresponds to a cell in the grid. The function maps custom markings to numeric values and visualizes the grid using matplotlib. The animation shows the progression of the search process, highlighting the explored cells and the final path.

    If save_animation is True, the animation is saved as a video file with the specified filename using the FFMpegWriter. If save_animation is False, the animation is displayed using matplotlib.

    Example usage:
    Define the grid states
    steps = [ [[".", ".", ".", ".", "."], [".", ".", ".", ".", "."], [".", ".", ".", ".", "."], [".", ".", ".", ".", "."], [".", ".", ".", ".", "."]],

    [[".", ".", ".", ".", "."],
     [".", ".", ".", ".", "."],
     [".", ".", ".", ".", "."],
     [".", ".", ".", ".", "."],
     [".", ".", ".", ".", "."]],

    [[".", ".", ".", ".", "."],
     [".", ".", ".", ".", "."],
     [".", ".", ".", ".", "."],
     [".", ".", ".", ".", "."],
     [".", ".", ".", ".", "."]],

    [[".", ".", ".", ".", "."],
     [".", ".", ".", ".", "."],
     [".", ".", ".", ".", "."],
     [".", ".", ".", ".", "."],
     [".", ".", ".", ".", "."]],

    [[".", ".", ".", ".", "."],
     [".", ".", ".", ".", "."],
     [".", ".", ".", ".", "."],
     [".", ".", ".", ".", "."],
     [".", ".", ".", ".", "."]]
    ]

    Animate the search process and save the animation

    animate_search_process(steps, save_animation=True, filename="search_animation.mp4")
    """
    # Define a mapping from custom markings to numeric values
    marking_to_numeric = {
        ".": 0,  # Open path
        "X": 1,  # Obstacle
        "S": 2,  # Start
        "G": 3,  # Goal
        "E": 4,  # Explored
        "P": 5,  # Path
    }

    fig, ax = plt.subplots(figsize=(5, 5))

    def update(frame):
        def marking_to_numeric_value(key):
            return marking_to_numeric.get(key, 0)  # Default to 0 for unmapped keys

        numeric_state = np.vectorize(marking_to_numeric_value)(steps[frame])
        ax.clear()
        ax.imshow(numeric_state, cmap=plt.cm.Dark2, interpolation="nearest")
        ax.set_title(f"Algo:{algorithm}Step: {frame + 1}")
        ax.set_xticks([])
        ax.set_yticks([])

    anim = FuncAnimation(fig, update, frames=len(steps), interval=200, repeat=False)

    if save_animation:
        writer = FFMpegWriter(fps=5)
        anim.save(filename, writer=writer)
    else:
        plt.show()
    plt.close(fig)
