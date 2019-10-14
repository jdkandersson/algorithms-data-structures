"""Heap implementation based on a list."""


class Heap:
    """Heap implementation based on a list."""

    def __init__(self):
        """Construct."""
        self._list = []

    @staticmethod
    def left_child(index):
        """
        Calculate the left child of an element.

        Args:
            index: The index to compute the left child for.

        Returns:
            The index of the left child.

        """
        return 2 * index + 1

    def _sift_down(self, start, end):
        """
        Move an element down the heap until it is in the right place.

        Args:
            start: The index to start at.
            end: The index to stop at.

        """
        root = start

        while self.left_child(root) <= end:
            swap = root
            left_child = self.left_child(root)
            right_child = self.left_child(root) + 1

            if self._list[swap] < self._list[left_child]:
                swap = left_child
            if right_child <= end and self._list[swap] < self._list[right_child]:
                swap = right_child
            if swap == root:
                return
            root_value = self._list[root]
            self._list[root] = self._list[swap]
            self._list[swap] = root_value
            root = swap
