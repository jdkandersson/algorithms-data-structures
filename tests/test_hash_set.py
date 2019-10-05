"""Tests for hash set."""
# pylint: disable=protected-access,redefined-outer-name

import pytest

from library import hash_set


def test_construct_capacity():
    """
    GIVEN capacity
    WHEN HashSet is constricted with the capacity
    THEN the underlying HashMap is constructed with the capacity.
    """
    capacity = 32

    test_hash_set = hash_set.HashSet(capacity)

    assert test_hash_set._hash_map._capacity == capacity


@pytest.mark.parametrize(
    "elements",
    [[], ["element 1"], ["element 1", "element 2"]],
    ids=["empty", "single", "multiple"],
)
def test_construct_source(elements):
    """
    GIVEN elements
    WHEN HashMap is constructed with the elements as the source
    THEN each element is contained in the underlying data structure.
    """
    test_hash_set = hash_set.HashSet(source=elements)

    for element in elements:
        assert test_hash_set._hash_map.exists(element)


@pytest.fixture
def empty_set():
    """Return empty HashSet."""
    return hash_set.HashSet()


def test_add(empty_set):
    """
    GIVEN empty hash set and an element
    WHEN add is called with the element
    THEN the element exists in the underlying HashMap.
    """
    element = "element 1"

    empty_set.add(element)

    assert empty_set._hash_map.exists(element)


@pytest.fixture
def single_set(empty_set):
    """Return single item HashSet."""
    empty_set.add("element 1")
    return empty_set


def test_delete(single_set):
    """
    GIVEN HashSet with single element
    WHEN delete is called with the element
    THEN the element is no longer in the underlying HashMap.
    """
    element = "element 1"

    single_set.delete(element)

    assert not single_set._hash_map.exists(element)


@pytest.mark.parametrize(
    "element, expected_result",
    [("element 1", True), ("element 2", False)],
    ids=["in set", "not in set"],
)
def test_contains(element, expected_result, single_set):
    """
    GIVEN HashSet with single element, element to check for and expected result
    WHEN contains is called with the element
    THEN the expected result is returned.
    """
    result = single_set.contains(element)

    assert result == expected_result


@pytest.mark.parametrize(
    "elements",
    [[], ["element 1"], ["element 1", "element 2"]],
    ids=["empty", "single", "multiple"],
)
def test_iter(elements):
    """
    GIVEN elements
    WHEN the hash set is constructed with the elements and iterated over
    THEN the elements are returned.
    """
    test_hash_set = hash_set.HashSet(source=elements)

    element_set = set(iter(test_hash_set))
    assert len(element_set) == len(elements)
    for element in elements:
        assert element in element_set


def test_size(single_set):
    """
    GIVEN HashSet with single element
    WHEN
    THEN the size is 1.
    """
    assert single_set.size == 1


def test_clear(single_set):
    """
    GIVEN HashSet with single element
    WHEN clear is called
    THEN the size is 0.
    """
    single_set.clear()

    assert single_set.size == 0
