"""Implementation of hash set in python."""

from library import hash_map

PRESENT = True


class HashSet:
    """Implements HashSet based on HashMap."""

    def __init__(self, capacity=16):
        """Construct."""
        self._hash_map = hash_map.HashMap(capacity)

    def add(self, value):
        """
        Add value to the set.

        Args:
            value: The value to add.

        """
        self._hash_map.set_(value, PRESENT)

    def delete(self, value):
        """
        Delete value from the set.

        Args:
            value: The value to delete.

        """
        self._hash_map.delete(value)

    def contains(self, value):
        """
        Check whether the set contains the value.

        Args:
            value: The value to check for.

        """
        return self._hash_map.exists(value)
