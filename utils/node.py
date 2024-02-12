from itertools import count


class Node:
    """
    A class to represent a node in a search space for maze navigation.

    Attributes:
        state (tuple): The state represented by the node, typically a tuple indicating (x, y) position in the maze.
        parent (Node): The node that generated this node, used to reconstruct the path.
        action (any): The action taken to generate this node from its parent.
        cost (int): The cost of the path from the initial state to this node, often representing the number of steps.
    """

    id_generator = count(0)  # Use the class-level id_generator for unique IDs

    def __init__(self, state, parent=None, action=None, cost=0):
        """
        Initializes a new instance of the Node class.

        Args:
            state (tuple): The state represented by the node.
            parent (Node, optional): The node's parent. Defaults to None.
            action (any, optional): The action taken to generate this node. Defaults to None.
            cost (int, optional): The cost of the path from the initial state to this node. Defaults to 0.
        """
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost

    def expand(self, problem):
        """
        Expands the node by generating successor nodes.

        Args:
            problem (Problem): The problem to solve.

        Returns:
            list: A list of successor nodes.
        """
        return [
            self.child_node(problem, action) for action in problem.actions(self.state)
        ]

    def child_node(self, problem, action):
        """
        Creates a child node from the current node.

        Args:
            problem (Problem): The problem to solve.
            action (any): The action to take.

        Returns:
            Node: A new node representing the child state.
        """
        next_state = problem.result(self.state, action)
        next_cost = self.cost + problem.step_cost(self.state, action)
        return Node(next_state, self, action, next_cost)

    def solution(self):
        """
        Returns the sequence of actions to go from the root to this node.

        Returns:
            list: A list of actions.
        """
        return [node.action for node in self.path()[1:]]

    def path(self):
        """
        Returns the sequence of nodes to go from the root to this node.

        Returns:
            list: A list of nodes.
        """
        node, p = self, []
        while node:
            p.append(node)
            node = node.parent
        return list(reversed(p))

    def __eq__(self, other):
        """
        Compares two nodes based on their state.

        Args:
            other (Node): The other node to compare.

        Returns:
            bool: True if the nodes are equal, False otherwise.
        """
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        """
        Returns the hash value of the node based on its state.

        Returns:
            int: The hash value.
        """
        return hash(self.state)

    def __lt__(self, other):
        """
        Compares two nodes based on their cost.

        Args:
            other (Node): The other node to compare.

        Returns:
            bool: True if this node has a lower cost than the other node, False otherwise.
        """
        return self.cost < other.cost

    def __repr__(self):
        """
        Returns a string representation of the node for debugging.

        Returns:
            str: The string representation of the node.
        """
        return f"Node(state={self.state}, cost={self.cost})"
