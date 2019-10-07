"""Binary search tree."""


class Node:
    """A node in the binary search tree."""

    def __init__(self, value, left=None, right=None):
        """Construct."""
        self.value = value
        self.left = left
        self.right = right

    def insert(self, value):
        """
        Insert value into the sub tree with the node as the root.

        Args:
            value: The value to insert.

        """
        if value > self.value:
            print("right")
            if self.right is None:
                print("new node")
                self.right = Node(value)
                return
            print("existing node")
            self.right.insert(value)
            return
        print("left")
        if self.left is None:
            print("new node")
            self.left = Node(value)
            return
        print("existing node")
        self.left.insert(value)
