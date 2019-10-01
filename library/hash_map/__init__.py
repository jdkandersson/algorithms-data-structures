"""Hash map implementation in Python."""

import hashlib

from . import bucket


class HashMap:
    """Implements the has map data structure."""

    def __init__(self, capacity=16, source=None):
        """Construct."""
        # The number of buckets
        self._capacity = capacity
        # The number of elements
        self._size = 0
        # Buckets with values
        self._buckets = [bucket.Bucket() for _ in range(self._capacity)]
        # Adding initial values
        if source is None:
            return
        for element in source:
            self.set_(*element)

    @property
    def size(self):
        """Get the number of elements in the map."""
        return self._size

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
        if not self.exists(key):
            self._size += 1
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
        value = self._buckets[index].delete(key)
        self._size -= 1
        return value

    def __iter__(self):
        """Iterate over all elements in the map."""
        for bucket_ in self._buckets:
            yield from bucket_.__iter__()

    def clear(self):
        """Remove all elements from the map."""
        for bucket_ in self._buckets:
            bucket_.clear()
        self._size = 0
