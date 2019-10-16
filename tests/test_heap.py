"""Tests for the heap."""
# pylint: disable=protected-access

import random

import pytest

from library import heap


@pytest.mark.parametrize(
    "source, expected_list",
    [(None, []), ([0, 1, 2], [2, 1, 0])],
    ids=["source none", "source list"],
)
@pytest.mark.heap
def test_construct(source, expected_list):
    """
    GIVEN source for construction and expected list
    WHEN the Heap is constructed with the source
    THEN the underlying list is set to the expected list.
    """
    test_heap = heap.Heap(source)

    assert test_heap._list == expected_list


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
@pytest.mark.heap
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
@pytest.mark.heap
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
@pytest.mark.heap
def test_heapify(initial, expected):
    """
    GIVEN initial elements
    WHEN _heapify is called
    THEN the elements are in the expected order.
    """
    test_heap = heap.Heap()
    test_heap._list = initial

    test_heap._heapify()

    assert test_heap._list == expected


@pytest.mark.parametrize(
    "source, expected",
    [
        ([], []),
        ([0], [0]),
        ([0, 1], [1, 0]),
        ([1, 0], [1, 0]),
        ([0, 1, 2], [2, 1, 0]),
        ([0, 2, 1], [2, 1, 0]),
        ([1, 0, 2], [2, 1, 0]),
        ([1, 2, 0], [2, 1, 0]),
        ([2, 0, 1], [2, 1, 0]),
        ([2, 1, 0], [2, 1, 0]),
    ],
    ids=[
        "empty",
        "single",
        "two unsorted",
        "two sorted",
        "three unsorted 1",
        "three unsorted 2",
        "three unsorted 3",
        "three unsorted 4",
        "three unsorted 5",
        "three sorted",
    ],
)
@pytest.mark.heap
def test_sorted(source, expected):
    """
    GIVEN source of elements and expected sorted elements
    WHEN the heap is constructed with the source and sorted is called
    THEN an iterator is returned with the elements in the expected order.
    """
    test_heap = heap.Heap(source)

    returned = list(test_heap.sorted())

    assert returned == expected


@pytest.fixture(params=[idx + 1 for idx in range(10)])
def random_list(request):
    """Generate list with random integers."""
    yield [random.randint(0, 100) for _ in range(request.param)]


@pytest.mark.heap
def test_sort_random(random_list):  # pylint: disable=redefined-outer-name
    """
    GIVEN random list
    WHEN a heap is constructed with the list as the source and sorted is called
    THEN a sorted list of elements is returned.
    """
    test_heap = heap.Heap(random_list)

    returned = test_heap.sorted()

    previous = next(returned)
    element_count = 1
    for current in returned:
        assert current <= previous
        element_count += 1

    assert element_count == len(random_list)


@pytest.mark.parametrize(
    "source, value, expected",
    [
        ([], 0, [0]),
        ([0], 1, [1, 0]),
        ([0], 0, [0, 0]),
        ([0], 1, [1, 0]),
        ([2, 0], 3, [3, 0, 2]),
        ([2, 0], 1, [2, 0, 1]),
        ([2, 0], -1, [2, 0, -1]),
    ],
    ids=[
        "empty source",
        "single element source value larger",
        "single element source value equal",
        "single element source value smaller",
        "two elememt source value larger",
        "two elememt source value between",
        "two elememt source value smaller",
    ],
)
@pytest.mark.heap
def test_insert(source, value, expected):
    """
    GIVEN source, value to insert and expected final list
    WHEN the heap is constructed with the source and insert is called with the value
    THEN the underlying list contains the expected elements in the expected order.
    """
    test_heap = heap.Heap(source)

    test_heap.insert(value)

    assert test_heap._list == expected
