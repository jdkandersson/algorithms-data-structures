"""Hash map implementation in Python."""

import hashlib


class HashMap:
    """Implements the has map data structure."""

    def __init__(self, capacity=16):
        """Construct."""
        # The number of buckets
        self._capacity = capacity
        # The number of elements
        self._size = 0

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
