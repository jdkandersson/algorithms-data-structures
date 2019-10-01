"""Hash map implementation in Python."""

import hashlib

from . import bucket


class HashMap:
    """Implements the has map data structure."""

    def __init__(self, capacity=16):
        """Construct."""
        # The number of buckets
        self._capacity = capacity
        # The number of elements
        self._size = 0
        # Buckets with values
        self._buckets = [bucket.Bucket() for _ in range(self._capacity)]

    def _calculate_index(self, key):
        """
        Calculate the index for the bucket that stores the key.

        Args:
            key: The key for the value. Can be an integer, float or string.

        Returns:
            The index as an integer where the key is stored.

        """
        str_key = str(key)
        bin_key = str_key.encode("utf-8")
        message = hashlib.sha256()
        message.update(bin_key)
        return int(message.hexdigest(), 16) % self._capacity

    def set_(self, key, value):
        """
        Set the value for the key.

        Args:
            jey: The identifier for the value.
            value: The value to associate with the key.

        """
        index = self._calculate_index(key)
        self._buckets[index].insert(key, value)

    def get(self, key):
        """
        Get the value for the key.

        Raises KeyError if the key does not exist.

        Args:
            key: The key identifying the value.

        Returns:
            The value associated with the key.

        """
        index = self._calculate_index(key)
        return self._buckets[index].get(key)

    def exists(self, key):
        """
        Check whether the key exists.

        Args:
            key: The key to check for.

        Returns:
            Whether the key exists.

        """
        index = self._calculate_index(key)
        return self._buckets[index].exists(key)

    def delete(self, key):
        """
        Remove key.

        Args:
            key: The key to remove.

        """
        index = self._calculate_index(key)
        return self._buckets[index].delete(key)
