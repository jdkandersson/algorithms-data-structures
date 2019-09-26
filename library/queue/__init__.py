"""Queue implemented using linked list."""


class _Node:
    """Node for the linked list."""

    def __init__(self, value, next_ = None):
        """Construct."""
        self.value = value
        self.next_ = next_


class QueueEmptyError(Exception):
    """Raised when an operation fails because the queue is empty."""


class _LinkedList:
    """Linked list for the queue."""

    def __init__(self):
        """Construct."""

        self.head = None
        self.tail = None

    def add_last(self, value):
        """
        Add value to the end of the linked list.

        Args:
            value: The value to add.

        """
        # Checking for empty list
        if self.head is None:
            self.head = _Node(value)
            self.tail = self.head
            return

        self.tail.next_ = _Node(value)
        self.tail = self.tail.next_

    def remove_first(self):
        """
        Remove value from the front of the list and return it.

        Raises QueueEmptyError when queue is empty.

        Returns:
            The first value in the list.

        """
        self.raise_empty()

        value = self.head.value
        self.head = self.head.next_
        if self.head is None:
            self.tail = self.head
        return value

    def raise_empty(self):
        """Raise QueueEmptyError when the queue is empty."""
        if self.head is None:
            raise QueueEmptyError


class Queue:
    """Queue implemented using a linked list."""

    def __init__(self):
        """"Construct."""
        self._list = _LinkedList()

    def enqueue(self, value):
        """
        Add value to back of queue.

        Args:
            value: The value to add to the queue.

        """
        self._list.add_last(value)

    def dequeue(self):
        """
        Remove and return value from front of queue.

        Returns:
            The value from the front of the queue.

        """
        return self._list.remove_first()

    def peek(self):
        """
        Return the value from the front of the queue without dequeueing it.

        Returns:
            The value at the front of the queue.

        """
        self._list.raise_empty()
        return self._list.head.value

    def is_empty(self):
        """
        Check whether the queue is empty.

        Returns:
            Whether the queue is empty.

        """
        return self._list.head is None
