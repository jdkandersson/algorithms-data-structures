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
            value: The value to add to the set.

        """
        self._hash_map.set_(value, PRESENT)
