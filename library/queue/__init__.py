"""Queue implemented using linked list."""


class QueueEmptyError(Exception):
    """Raised when an operation fails because the queue is empty."""


class QueueFullError(Exception):
    """Raised when an operation fails because the queue is full."""


class Queue:
    """Queue implemented using a linked list."""

    def __init__(self, length=10):
        """
        Construct.

        Args:
            length: The length of the queue.

        """
        self.length = length
        self.size = 0
        self._list = [None for _ in range(length)]
        self.front = 0
        self.back = -1

    def _increment_position(self, position):
        """
        Increment position to the next one.

        Args:
            position: The position to increment.

        Returns:
            The position incremented by one with wrapping.

        """
        return (position + 1) % self.length

    def enqueue(self, value):
        """
        Add value to back of queue.

        Raises QueueFullError is the queue is full.

        Args:
            value: The value to add to the queue.

        """
        self._check_full()

        new_back = self._increment_position(self.back)
        self.back = new_back
        self._list[self.back] = value
        self.size += 1

    def dequeue(self):
        """
        Remove and return value from front of queue.

        Returns:
            The value from the front of the queue.

        """
        self._check_empty()

        value = self._list[self.front]
        self.front = self._increment_position(self.front)
        self.size -= 1
        return value

    def get_front(self):
        """
        Return the value from the front of the queue without dequeueing it.

        Returns:
            The value at the front of the queue.

        """
        self._check_empty()
        return self._list[self.front]

    def is_empty(self):
        """
        Check whether the queue is empty.

        Returns:
            Whether the queue is empty.

        """
        return self.size == 0

    def _check_empty(self):
        """Raise QueueEmptyError if the queue is empty."""
        if self.is_empty():
            raise QueueEmptyError

    def _check_full(self):
        """Raise QueueFullError if the queue isfFull."""
        if self.size == self.length:
            raise QueueFullError

    def clear(self):
        """Remove all elements from the queue."""
        self.front = 0
        self.back = -1
        self.size = 0
