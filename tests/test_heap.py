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


@pytest.mark.parametrize(
    "initial, start, end, expected",
    [
        ([], 0, -1, []),
        ([0], 0, 0, [0]),
        ([1, 0], 0, 1, [1, 0]),
        ([0, 1], 0, 1, [1, 0]),
        ([2, 1, 0], 0, 1, [2, 1, 0]),
        ([2, 1, 0], 0, 2, [2, 1, 0]),
        ([1, 2, 0], 0, 1, [2, 1, 0]),
        ([0, 1, 2], 0, 2, [2, 1, 0]),
        ([6, 3, 4, 5, 2, 1, 0], 0, 3, [6, 5, 4, 3, 2, 1, 0]),
        ([5, 3, 4, 6, 2, 1, 0], 0, 3, [6, 5, 4, 3, 2, 1, 0]),
        ([5, 3, 4, 6, 2, 1, 0], 1, 3, [5, 6, 4, 3, 2, 1, 0]),
        ([6, 5, 0, 3, 2, 1, 4], 0, 6, [6, 5, 4, 3, 2, 1, 0]),
        ([5, 4, 1, 3, 2, 0, 6], 0, 6, [6, 4, 5, 3, 2, 0, 1]),
        ([0, 5, 4, 3, 2, 1, 6], 2, 6, [0, 5, 6, 3, 2, 1, 4]),
    ],
    ids=[
        "empty",
        "single",
        "two right order",
        "two wrong order",
        "three right order left",
        "three right order right",
        "three wrong order left",
        "three wrong order right",
        "seven wrong order sub tree child leftmost child",
        "seven wrong order leftmost child",
        "seven wrong order sub tree boundary leftmost child",
        "seven wrong order sub child root rightmost child",
        "seven wrong order rightmost child",
        "seven wrong order sub tree boundary rightmost child",
    ],
)
def test_sift_up(initial, start, end, expected):
    """
    GIVEN initial elements for the list of a heap that satisfy the heap property except
        for possibly the element at end and the start and the end
    WHEN _sift up is called with the start and the end
    THEN the final list is equal to the expected list.
    """
    test_heap = heap.Heap()
    test_heap._list = initial

    test_heap._sift_up(start, end)

    assert test_heap._list == expected


@pytest.mark.parametrize(
    "initial, expected",
    [
        ([], []),
        ([0], [0]),
        ([1, 0], [1, 0]),
        ([0, 1], [1, 0]),
        ([2, 1, 0], [2, 1, 0]),
        ([0, 1, 2], [2, 1, 0]),
        ([0, 1, 2, 3, 4, 5, 6], [6, 4, 5, 3, 1, 0, 2]),
    ],
    ids=[
        "empty",
        "single",
        "two right order",
        "two wrong order",
        "three right order",
        "three wrong order",
        "many",
    ],
)
def test_heapify(initial, expected):
    """
    GIVEN initial elements
    WHEN heapify is called
    THEN the elements are in the expected order.
    """
    test_heap = heap.Heap()
    test_heap._list = initial

    test_heap.heapify()

    assert test_heap._list == expected
