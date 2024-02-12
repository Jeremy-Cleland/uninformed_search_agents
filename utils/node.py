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
        self.id = next(count())

    def __lt__(self, other):
        """
        Compares two nodes based on their cost.
        """
        return self.cost < other.cost

    def __repr__(self):
        """
        Returns a string representation of the node for debugging.
        """
        return f"Node(state={self.state}, cost={self.cost})"
