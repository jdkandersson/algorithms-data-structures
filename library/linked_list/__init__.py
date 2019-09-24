"""Implementation of a singly linked list with common operations."""

import typing


class Node:
    """Represents an node in the linked list."""

    def __init__(self, value, next_ = None):
        """
        Construct.

        Args:
            value: The value for the node.
            next_: The node to set to next.

        """
        self.value = value
        self.next_ = next_


class LinkedList:
    """Singly linked list."""

    def __init__(self):
        """
        Construct."""
        self.head = None

    def add_first(self, value):
        """
        Add value to the front of the list.

        Args:
            value: The value to add to the front.

        """
        self.head = Node(value, self.head)

    def add_last(self, value):
        """
        Add value to end of the linked list.

        Args:
            value: The value to add to the linked list.

        """
        # Checking for empty list
        if self.head is None:
            self.add_first(value)
            return

        # Add new node
        self._add_last(self.head, value)

    @classmethod
    def _add_last(cls, node, value):
        """
        Recursively add value. Could also be done as a while loop.

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
        cls._add_last(node.next_, value)

    def insert_after(self, key, value):
        """
        Insert a new value after a key.

        Args:
            key: The value after which to insert the new value.
            value: The new value to insert.

        """
        self._insert_after(self.head, key, value)


    @classmethod
    def _insert_after(cls, node, key, value):
        """
        Insert a new value after a key recursively.

        Args:
            node: The node to operate on. Can be None.
            key: The value after which to insert the new value.
            value: The new value to insert.

        """
        # End of list base case
        if node is None:
            return

        # Base case for key found
        if node.value == key:
            node.next_ = Node(value, node.next_)
            return

        # Recursive case
        cls._insert_after(node.next_, key, value)

    def insert_before(self, key, value):
        """
        Insert a new value before a key.

        Args:
            key: The value before which to insert the new value.
            value: The new value to insert.

        """
        # Iterating to node that has value
        node = self.head
        last_node = None
        while node is not None and node.value != key:
            last_node = node
            node = node.next_

        # Check if the node has been found
        if node is None:
            return

        # Checking whether head matched
        if last_node is None:
            self.add_first(value)
            return

        # Inserting new node
        last_node.next_ = Node(value, node)

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

    def search(self, value):
        """
        Check whether value is in list.

        Args:
            value: The value to search for.

        """
        return self._search(self.head, value)

    @classmethod
    def _search(cls, node, value):
        """
        Check whether value is in list using recursion.

        If node is None return False.
        If node value is equal to value return True.
        Else recursively call on next_ property.

        Args:
            value: The value to search for.

        """
        if node is None:
            return False

        if node.value == value:
            return True

        return cls._search(node.next_, value)

    def __iter__(self):
        """Iterate over list."""
        node = self.head
        while node is not None:
            yield node.value
            node = node.next_
