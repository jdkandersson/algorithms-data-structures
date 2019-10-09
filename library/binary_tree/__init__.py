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

    def get_smallest(self):
        """
        Get the smallest value in the subtree starting with the node as root.

        Returns:
            The smallest value in the subtree.

        """
        if self.left is None:
            return self.value
        return self.left.get_smallest()

    def is_leaf(self):
        """
        Check whether the node is a leaf.

        Returns:
            Whether the node is a leaf.

        """
        return self.left is None and self.right is None

    def __iter__(self):
        """Iterate over values."""
        if self.left is not None:
            yield from self.left.__iter__()
        yield self.value
        if self.right is not None:
            yield from self.right.__iter__()

    def delete(self, value):
        """
        Delete the value out of the sub tree with the node as root.

        Args:
            value: The value to delete.

        Returns:
            The new root node.

        """
        if value == self.value:
            if self.is_leaf():
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            # Getting the smallest value in the right subtree
            smallest_in_right = self.right.get_smallest()
            self.value = smallest_in_right
            self.right = self.right.delete(smallest_in_right)
            return self
        if self.is_leaf():
            raise ValueError(f"{value} not found in the tree")
        if value < self.value:
            self.left = self.left.delete(value)
            return self
        self.right = self.right.delete(value)
        return self


class BinaryTree:
    """Implementation of a binary tree."""

    def __init__(self, root=None):
        """Construct."""
        self.root = root

    def insert(self, value):
        """
        Insert value into the binary tree.

        Args:
            value: The value to insert.

        """
        if self.root is None:
            self.root = Node(value)
            return
        self.root.insert(value)

    def __iter__(self):
        """Iterate over values in the tree in order."""
        if self.root is not None:
            yield from self.root.__iter__()

    def search(self, value):
        """
        Search for the value in the tree.

        Args:
            value: The value to search for.

        Returns:
            The value if found or None.

        """
        if self.root is None:
            return None
        return self.root.search(value)

    def delete(self, value):
        """
        Delete value from the tree.

        Raises ValueError if the value is not in the tree.

        Args:
            value: The value to delete.

        """
        if self.root is None:
            raise ValueError(f"{value} not found in the tree")
        self.root = self.root.delete(value)
