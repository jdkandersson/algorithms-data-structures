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
        for element in self._list:
            element_key, element_value = element
            if element_key == key:
                return element_value
        raise KeyError

    def exists(self, key):
        """
        Check whether the key is in the bucket.

        Args:
            key: The key to check for.

        Returns:
            Whether the key is in the bucket.

        """
        for element in self._list:
            element_key, _ = element
            if element_key == key:
                return True
        return False

    def delete(self, key):
        """
        Delete the key from the bucket.

        Raises KeyError if the key doesn't exist.

        Args:
            key: The key to delete.

        """
        value = self.get(key)
        self._list.delete((key, value))

    def __iter__(self):
        """Iterate over each element in the bucket."""
        return self._list.__iter__()

    def clear(self):
        """Remove all elements from the bucket."""
        self._list.clear()

    def is_empty(self):
        """
        Check whether the bucket is empty.

        Returns:
            Whether the bucket is empty.

        """
        return self._list.is_empty()
