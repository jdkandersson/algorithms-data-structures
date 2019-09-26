"""Stack implemented using a linked list."""


class _Node:
    """Node for the linked list."""

    def __init__(self, value, next_ = None):
        """
        Construct.

        Args:
            value: The value for the node.
            next_: The next node in the linked list.

        """
        self.value = value
        self.next_ = next_


class StackEmptyError(Exception):
    """Raised when pop is called on an empty stack."""


class _LinkedList:
    """Linked list for the stack."""

    def __init__(self):
        """Construct."""
        self.head = None

    def add_first(self, value):
        """
        Add new value to front of the linked list.

        Args:
            value: The value to add to the linked list.

        """
        self.head = _Node(value, self.head)

    def remove_first(self):
        """
        Remove the first node from the list and return the value.

        Raises StackEmptyError if the list is empty.

        Returns:
            The value of the first node.

        """
        self.raise_empty()

        node = self.head
        self.head = self.head.next_
        return node.value

    def raise_empty(self):
        """Raise StackEmptyError if the stack is empty."""
        if self.head is None:
            raise StackEmptyError


class Stack:
    """Implementation of a stack."""

    def __init__(self):
        """Construct."""
        self._list = _LinkedList()

    def push(self, value):
        """
        Add a new value to the stack.

        Args:
            value: The value to add to the stack.

        """
        self._list.add_first(value)

    def pop(self):
        """
        Remove the most recently added value from the list and return it.

        Raises StackEmptyError if the stack is empty.

        Returns:
            The most recently added value.

        """
        return self._list.remove_first()

    def peek(self):
        """
        Return the value at the top of the stack without popping it.

        Raises StackEmptyError if the stack is empty.

        Returns:
            The top value.

        """
        self._list.raise_empty()
        return self._list.head.value

    def is_empty(self):
        """
        Check whether the stack is empty.

        Returns:
            Whether the stack is empty.

        """
        return self._list.head is None
