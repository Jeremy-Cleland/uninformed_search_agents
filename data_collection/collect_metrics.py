import time
import pandas as pd
from algorithms.dfs import dfs_search
from algorithms.bfs import bfs_search
from algorithms.a_star import a_star_search
from utils.maze_generation import generate_maze


def run_search_algorithms(runs=10, size=10, density=0.2):
    results = []

    for i in range(runs):
        maze = generate_maze(
            size=10, density=0.2
        )  # Assuming this function is already implemented
        algorithms = {"DFS": dfs_search, "BFS": bfs_search, "A*": a_star_search}

        for name, algorithm in algorithms.items():
            start_time = time.time()
            solution, nodes_expanded = algorithm(maze)

            execution_time = time.time() - start_time
            status = "Pass" if solution else "Fail"
            solution_path_length = len(solution) if solution else 0

            results.append(
                {
                    "Run": i + 1,
                    "Algorithm": name,
                    "Solution Path Length": solution_path_length,
                    "Nodes Expanded": nodes_expanded,
                    "Execution Time": execution_time,
                    "Status": status,
                }
            )

    return pd.DataFrame(results)


def summarize_results(results_df):
    summary = (
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

    summary["Run"] = "Avg"
    summary["Status"] = "-"
    return pd.concat([results_df, summary], ignore_index=True)


results_df = run_search_algorithms()
final_report = summarize_results(results_df)
print(final_report)
