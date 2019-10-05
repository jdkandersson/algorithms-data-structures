"""Tests for hash set."""
# pylint: disable=protected-access

from library import hash_set


def test_construct():
    """
    GIVEN capacity
    WHEN HashSet is constricted with the capacity
    THEN the underlying HashMap is constructed with the capacity.
    """
    capacity = 32

    test_hash_set = hash_set.HashSet(capacity)

    assert test_hash_set._hash_map._capacity == capacity


def test_add():
    """
    GIVEN empty hash set and an element
    WHEN add is called with the element
    THEN the element exists in the underlying HashMap.
    """
    element = "element 1"
    test_hash_set = hash_set.HashSet()

    test_hash_set.add(element)

    assert test_hash_set._hash_map.exists(element)
