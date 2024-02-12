from utils.maze_generation import generate_maze
from data_collection.collect_metrics import run_search_algorithms, summarize_results
from visualization.visualize_maze import visualize_maze


def main():
    # Parameters for maze generation and analysis
    maze_size = 10
    obstacle_density = 0.2
    runs = 10  # Number of mazes to generate and analyze

    # Run search algorithms and collect metrics
    results_df = run_search_algorithms(runs)

    # Summarize and print the results
    final_report = summarize_results(results_df)
    print(final_report)

    # Optionally, visualize the last maze and its solutions
    # This could be expanded to visualize each maze in the runs
    last_maze = generate_maze(maze_size, obstacle_density)
    visualize_maze(last_maze)
    # Implement visualization of the solution path if desired


if __name__ == "__main__":
    main()
