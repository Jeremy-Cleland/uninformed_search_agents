from data_collection.collect_metrics import run_search_algorithms, summarize_results


def main():
    """
    Runs multiple search algorithms on randomly generated mazes and prints the summarized results.

    Parameters:
    - None

    Returns:
    - None

    The 'main' function is the entry point of the program. It calls the 'run_search_algorithms' function to run multiple search algorithms on randomly generated mazes and obtain the results as a DataFrame. It then calls the 'summarize_results' function to calculate the average metrics for each algorithm and prints the summarized results.

    Example usage:
    main()
    """
    results_df = run_search_algorithms(
        runs=10, size=10, density=0.2, visualize=True, save_animation=True
    )
    final_report = summarize_results(results_df)
    print(final_report)


if __name__ == "__main__":
    main()
