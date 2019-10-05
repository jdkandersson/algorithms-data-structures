"""Implementation of hash set in python."""

from library import hash_map

PRESENT = True


class HashSet:
    """Implements HashSet based on HashMap."""

    def __init__(self, capacity=16, source=None):
        """Construct."""
        if source is not None:
            self._hash_map = hash_map.HashMap(
                capacity, ((element, PRESENT) for element in source)
            )
        else:
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

    def __iter__(self):
        """Iterate over elements in the hash set."""
        for key, _ in iter(self._hash_map):
            yield key

    @property
    def size(self):
        """
        Get the number of elements in the set.

        Returns:
            The number of elements in the set.

        """
        return self._hash_map.size
