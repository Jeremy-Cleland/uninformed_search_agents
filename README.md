# Maze Search Algorithms Comparison

## Project Overview

This project implements and compares three fundamental search algorithms - Depth-First Search (DFS), Breadth-First Search (BFS), and A* Search - in navigating and solving mazes. The objective is to analyze the algorithms' performance across various metrics, including solution path length, nodes expanded, and execution time, within procedurally generated mazes. This comparison aims to provide insights into each algorithm's efficiency and suitability for maze navigation tasks.

## Project Structure

maze_search_project/
│
├── algorithms/
│   ├── __init__.py
│   ├── dfs.py
│   ├── bfs.py
│   └── a_star.py
│
├── visualization/
│   ├── __init__.py
│   ├── visualize_maze.py
│   └── animate_search.py
│
├── data_collection/
│   ├── __init__.py
│   └── collect_metrics.py
│
├── utils/
│   ├── __init__.py
│   └── maze_generation.py
│
└── main.py


## Features

- **Maze Generation:** Generates random mazes with customizable sizes and obstacle densities.
- **Algorithm Implementation:** Includes Python-based implementations of DFS, BFS, and A* search algorithms.
- **Performance Analysis:** Collects and summarizes performance data for each algorithm across multiple maze configurations.
- **Visualization:** Offers visualization tools for maze exploration processes and algorithm performance comparison.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Required Python packages: `numpy`, `matplotlib`, `plotly`, `networkx`, `pandas`

### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/yourgithubusername/maze-search-project.git
cd maze-search-project

```

### Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Running the Project

To run the project and generate the algorithm comparison report:

``` bash
python main.py

```

## Usage

- Modify the main.py script to customize the maze generation parameters and the number of runs for the analysis.
- Use the visualization scripts in the visualization/ directory to visually inspect the maze-solving processes and the algorithms' exploration patterns.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the issues page for open issues or to open a new issue.

## License

Distributed under the MIT License. See LICENSE for more information.