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
            if self.right is None:
                self.right = Node(value)
                return
            self.right.insert(value)
            return
        if self.left is None:
            self.left = Node(value)
            return
        self.left.insert(value)

    def search(self, value):
        """
        Search for a value in the subtree with the node as the head.

        Args:
            value: The value to search for.

        Returns:
            The value if it was found or None if it was not.

        """
        if value == self.value:
            return self.value
        if value > self.value:
            if self.right is None:
                return None
            return self.right.search(value)
        if self.left is None:
            return None
        return self.left.search(value)
