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

    @staticmethod
    def parent(index):
        """
        Calculate the parent of an element.

        Args:
            index: The index to compute the parent for.

        Returns:
            The index of the parent.

        """
        return int((index - 1) / 2)

    def _sift_down(self, start, end):
        """
        Move an element at start down the heap until it is in the right place.

        Assume that the heap rooted at the element's children is valid.

        Args:
            start: The left boundary of the heap.
            end: The right boundary of the heap.

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

    def _sift_up(self, start, end):
        """
        Move an element at end up the heap until it is in the right place.

        Assume the heap rooted at start and ending at end is valid except for the
        element at end.

        Args:
            start: The left boundary of the heap.
            end: The right boundary of the heap.

        """
        child = end
        parent = self.parent(child)

        while parent >= start:
            if self._list[child] > self._list[parent]:
                parent_value = self._list[parent]
                self._list[parent] = self._list[child]
                self._list[child] = parent_value

                child = parent
                parent = self.parent(child)
            else:
                return
