import time
import os
import pandas as pd
from algorithms.dfs import dfs_search
from algorithms.bfs import bfs_search
from algorithms.a_star import a_star_search
from utils.maze_generation import generate_maze
from visualization.animate_search import (
    animate_search_process,
)  # Ensure this import is correct

output_folder = "search_videos"


def run_search_algorithms(runs, size, density, visualize, save_animation):
    """
    Runs multiple search algorithms on randomly generated mazes and returns the results as a pandas DataFrame.

    Parameters:
    - runs (int): The number of runs to perform. Defaults to 10.
    - size (int): The size of the maze (size x size). Defaults to 10.
    - density (float): The density of obstacles in the maze, between 0 and 1. Defaults to 0.2.
    - visualize (bool): Whether to visualize the search process. Defaults to True.
    - save_animation (bool): Whether to save the animation as a video file. Defaults to True.

    Returns:
    - pd.DataFrame: A DataFrame containing the results of each run and algorithm, including the run number, algorithm name, solution path length, number of nodes expanded, execution time, and status.

    The 'run_search_algorithms' function runs multiple search algorithms on randomly generated mazes. It takes the number of runs, maze size, obstacle density, visualization flag, and save animation flag as input parameters. The function returns the results of each run and algorithm as a pandas DataFrame.

    For each run, the function generates a random maze using the 'generate_maze' function. It then iterates over a dictionary of algorithms, which includes the names and corresponding functions. For each algorithm, it measures the execution time and number of nodes expanded during the search. If the visualization flag is set to True, it calls the 'animate_search_process' function to visualize the search process and save the animation if the save animation flag is also True. The results of each run and algorithm are appended to a list, which is then converted to a pandas DataFrame and returned.

    Example usage:
    results = run_search_algorithms(runs=5, size=20, density=0.3, visualize=True, save_animation=True)
    print(results)
    """
    results = []
    for run_number in range(1, runs + 1):
        maze = generate_maze(size, density)

        algorithms = {
            "DFS": dfs_search,
            "BFS": bfs_search,
            "A*": a_star_search,
        }

        for name, algorithm in algorithms.items():
            start_time = time.time()
            solution, nodes_expanded, steps = algorithm(maze)
            execution_time = time.time() - start_time
            status = "Pass" if solution else "Fail"
            solution_path_length = len(solution) if solution else 0
            solution, nodes_expanded, steps = algorithm(maze)

            if visualize:
                animation_filename = f"{name}_search_animation_run_{run_number}.mp4"
                animate_search_process(
                    steps,
                    name,
                    save_animation=False,
                    filename=animation_filename,
                )

            if visualize and save_animation:
                # Construct the filename including the path to the output folder
                filename = os.path.join(
                    output_folder, f"{name}_search_run_{run_number}.mp4"
                )

                # Call the function to animate and save the search process
                animate_search_process(
                    steps, algorithm, save_animation=True, filename=filename
                )

            results.append(
                {
                    "Run": run_number,
                    "Algorithm": name,
                    "Solution Path Length": solution_path_length,
                    "Nodes Expanded": nodes_expanded,
                    "Execution Time": execution_time,
                    "Status": status,
                }
            )

    return pd.DataFrame(results)


import pandas as pd


def summarize_results(results_df):
    # Calculate average metrics for each algorithm
    summary_avg = (
        results_df.groupby("Algorithm")
        .agg(
            {
                "Solution Path Length": "mean",
                "Nodes Expanded": "mean",
                "Execution Time": "mean",
            }
        )
        .reset_index()
    )

    # Calculate total fails for each algorithm
    fails_summary = (
        results_df[results_df["Status"] == "Fail"]
        .groupby("Algorithm")
        .size()
        .reset_index(name="Total Fails")
    )

    # Merge average metrics with total fails
    summary = pd.merge(summary_avg, fails_summary, on="Algorithm", how="left")
    summary["Total Fails"] = summary["Total Fails"].fillna(
        0
    )  # Replace NaNs with 0 for algorithms with no fails

    # Append the summary to the original results DataFrame
    final_results = pd.concat([results_df, summary], ignore_index=True, sort=False)

    # Correctly handle the dtype warning by explicitly converting "Run" to object type if necessary
    if final_results["Run"].dtype != "object":
        final_results["Run"] = final_results["Run"].astype("object")
    final_results.loc[final_results["Run"].isnull(), "Run"] = "Average"

    # Handle inplace operation warning by directly assigning the filled values
    final_results["Status"] = final_results["Status"].fillna("-")

    return final_results


def save_results_to_csv(results_df, filename="search_results.csv"):
    """
    Saves the summarized results of the search algorithms to a CSV file.

    Parameters
    ----------
    results_df : pd.DataFrame
        The DataFrame containing the summarized results.
    filename : str, optional
        The filename for the CSV file.
    """
    results_df.to_csv(filename, index=False)
    print(f"Results saved to {filename}")


# Example usage:
# Assuming results_df is the DataFrame returned by your search algorithm runs
