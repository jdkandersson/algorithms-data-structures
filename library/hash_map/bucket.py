"""Bucket implemented using linked list."""

from library import linked_list


class Bucket:
    """Class for buckets."""

    def __init__(self):
        """Construct."""
        self._list = linked_list.LinkedList()

    def insert(self, key, value):
        """
        Add or update key value pair to the bucket.

        Args:
            key: The key identifying the value.
            value: The data to store.

        """
        self._list.add_first((key, value))

    def get(self, key):
        """
        Get the value identifyied by the key.

        Raises KeyError if the key doesn't exist.

        Args:
            key: The key for the value to retrieve.

        Returns:
            The value for the key.

        """

    def exists(self, key):
        """
        Check whether the key is in the bucket.

        Args:
            key: The key to check for.

        Returns:
            Whether the key is in the bucket.

        """

    def remove(self, key):
        """
        Remove the key from the bucket.

        Raises KeyError if the key doesn't exist.

        Args:
            key: The key to remove.

        """

    def __iter__(self):
        """Iterate over each element in the bucket."""

    def clear(self):
        """Remove all elements from the bucket."""

    def is_empty(self):
        """
        Check whether the bucket is empty.

        Returns:
            Whether the bucket is empty.

        """
