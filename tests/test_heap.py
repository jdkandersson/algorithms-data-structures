"""Tests for the heap."""
# pylint: disable=protected-access

import pytest

from library import heap


@pytest.mark.heap
@pytest.mark.parametrize(
    "initial, start, end, expected",
    [
        ([], 0, -1, []),
        ([0], 0, 0, [0]),
        ([1, 0], 0, 1, [1, 0]),
        ([0, 1], 0, 1, [1, 0]),
        ([2, 1, 0], 0, 2, [2, 1, 0]),
        ([1, 2, 0], 0, 2, [2, 1, 0]),
        ([1, 0, 2], 0, 2, [2, 0, 1]),
        ([0, 1, 2], 0, 2, [2, 1, 0]),
        ([6, 5, 4, 3, 2, 1, 0], 0, 6, [6, 5, 4, 3, 2, 1, 0]),
        ([3, 2, 6, 0, 1, 5, 4], 0, 6, [6, 2, 5, 0, 1, 3, 4]),
        ([3, 2, 5, 0, 1, 6, 4], 2, 6, [3, 2, 6, 0, 1, 5, 4]),
        ([3, 6, 2, 5, 4, 0, 1], 0, 6, [6, 5, 2, 3, 4, 0, 1]),
        ([3, 4, 2, 5, 6, 0, 1], 1, 6, [3, 6, 2, 5, 4, 0, 1]),
    ],
    ids=[
        "empty",
        "single",
        "two right order",
        "two wrong order",
        "three right order",
        "three left child larger",
        "three right child larger",
        "three both children larger",
        "seven right order",
        "seven left tree",
        "seven left sub tree",
        "seven right tree",
        "seven right sub tree",
    ],
)
def test_sift_down(initial, start, end, expected):
    """
    GIVEN initial elements for the list of a heap that satisfy the heap property
        except for possibly the start and the start and the end
    WHEN _sift down is called with the start and the end
    THEN the final list is equal to the expected list.
    """
    test_heap = heap.Heap()
    test_heap._list = initial

    test_heap._sift_down(start, end)

    assert test_heap._list == expected
