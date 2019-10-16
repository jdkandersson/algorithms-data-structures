"""Heap implementation based on a list."""


class Heap:
    """Heap implementation based on a list."""

    def __init__(self, source=None):
        """
        Construct.

        Args:
            source: The elements to initialize the heap with.

        """
        if source is None:
            self._list = []
            return

        self._list = [value for value in source]
        self._heapify()

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

    def _heapify(self):
        """Turn the underlying list into a heap."""
        start = self.parent(len(self._list) - 1)
        while start >= 0:
            self._sift_down(start, len(self._list) - 1)
            start -= 1

    def sorted(self):
        """
        Sort the elements in the heap.

        Assume that the heap already satisfies the heap property.

        Returns:
            Iterator over the heap where elements are returned in sorted order.

        """
        start = 0
        end = len(self._list) - 1

        # Sorting
        while end > 0:
            root_value = self._list[0]
            self._list[0] = self._list[end]
            self._list[end] = root_value
            end -= 1
            self._sift_down(start, end)

        # Reversing the order
        start = 0
        end = len(self._list) - 1
        while start < end:
            end_value = self._list[end]
            self._list[end] = self._list[start]
            self._list[start] = end_value

            start += 1
            end -= 1

        return iter(self._list)

    def insert(self, value):
        """
        Add the value to the heap.

        Assume the heap is already a valid heap.

        Args:
            value: The value top insert.

        """
        self._list.append(value)
        self._sift_up(0, len(self._list) - 1)
