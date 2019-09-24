"""Tests for linked list."""

import pytest

from library import linked_list


def test_node_construct():
    """
    GIVEN value for node
    WHEN node is constructed with the value
    THEN the value is copied into the node and next_ is None.
    """
    value = "value 1"

    node = linked_list.Node(value)

    assert node.value == value
    assert node.next_ is None


def test_linked_list_construct():
    """
    GIVEN
    WHEN linked list is constructed
    THEN head is None.
    """
    list_ = linked_list.LinkedList()

    assert list_.head is None


def test_linked_list_add_empty():
    """
    GIVEN empty linked list value to add
    WHEN add is called with the value
    THEN head is replaced with a Node with value set to input value and next_ set to
        None.
    """
    list_ = linked_list.LinkedList()
    value = "value 1"

    list_.add(value)

    assert list_.head.value == value
    assert list_.head.next_ == None


@pytest.fixture
def single_list():
    """Linked list with single value."""
    list_ = linked_list.LinkedList()
    list_.add("value 1")
    return list_


def test_linked_list_add_single(single_list):
    """
    GIVEN linked list with single node and a value
    WHEN add is called with the value
    THEN head references a Node with the value and None for next_.
    """
    value = "value 2"

    single_list.add(value)

    assert single_list.head.next_ is not None
    assert single_list.head.next_.value == value
    assert single_list.head.next_.next_ is None


@pytest.fixture
def multiple_list():
    """Linked list with multiple values."""
    list_ = linked_list.LinkedList()
    for idx in range(2):
        list_.add(f"value {idx + 1}")
    return list_


def test_linked_list_add_multiple(multiple_list):
    """
    GIVEN linked list with multiple node and a value
    WHEN add is called with the value
    THEN the first element with None next_ property contains the value.
    """
    value = "value -1"

    multiple_list.add(value)

    counter = 0
    node = multiple_list.head
    while counter < 100 and node.next_ is not None:
        node = node.next_
        counter += 1
    assert node.value == value
