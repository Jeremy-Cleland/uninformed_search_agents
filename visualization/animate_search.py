# import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import plotly.graph_objects as go


def animate_search_process(maze, steps):
    """
    Animates the step-by-step exploration process of a search algorithm.

    Args:
        maze (np.array): The initial state of the maze.
        steps (list): A list of maze states showing the exploration over time.
    """
    fig, ax = plt.subplots()

    def update(frame):
        ax.clear()
        ax.imshow(steps[frame], cmap=plt.cm.Dark2)
        # Redraw grid and labels as in visualize_maze

    anim = FuncAnimation(fig, update, frames=len(steps), interval=200, repeat=False)
    plt.show()


def performance_dashboard(metrics):
    """
    Creates an interactive dashboard comparing algorithm performance.

    Args:
        metrics (dict): A dictionary containing performance metrics for each algorithm.
    """
    fig = go.Figure()

    for algo, data in metrics.items():
        fig.add_trace(go.Bar(x=list(data.keys()), y=list(data.values()), name=algo))

    fig.update_layout(
        title="Search Algorithm Performance Comparison",
        xaxis_title="Metric",
        yaxis_title="Value",
        barmode="group",
    )
    fig.show()
