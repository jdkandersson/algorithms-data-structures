"""Implementation of a singly linked list with common operations."""

import typing


class Node:
    """Represents an node in the linked list."""

    def __init__(self, value):
        """
        Construct.

        Args:
            value: The value for the node.

        """
        self.value = value
        self.next_ = None


class LinkedList:
    """Singly linked list."""

    def __init__(self):
        """
        Construct."""
        self.head = None

    def add(self, value):
        """
        Add value to linked list.

        Args:
            value: The value to add to the linked list.

        """
        # Checking for empty list
        if self.head is None:
            self.head = Node(value)
            return

        # Add new node
        self._add(self.head, value)

    @classmethod
    def _add(cls, node, value):
        """
        Recursively add value.

        Checks if the node next_ property is None. if it is, it creates a new Node and
        sets it to the next_ property.

        Args:
            node: The node to operate on.
            value: The value to add to the list.

        """
        # Check if element is the last element
        if node.next_ is None:
            node.next_ = Node(value)
            return

        # Recursively go to next node
        cls._add(node.next_, value)

    def traverse(self, func):
        """
        Call function on each value in the list.

        Args:
            func: The function to call each value with.

        """
        self._traverse(self.head, func)

    @classmethod
    def _traverse(cls, node, func):
        """
        Call function with the value of the node.

        If the node is NOne the function is not called.

        Args:
            node: The node to call the function with.
            func: The function to call.

        """
        # Checking for last node
        if node is None:
            return

        func(node.value)
        cls._traverse(node.next_, func)
