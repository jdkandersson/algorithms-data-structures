"""Tests for linked list."""

import pytest
from unittest import mock

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


@pytest.fixture
def empty_list():
    """Linked list with empty value."""
    list_ = linked_list.LinkedList()
    return list_


def test_linked_list_add_empty(empty_list):
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
def single_list(empty_list):
    """Linked list with single value."""
    empty_list.add("value 1")
    return empty_list


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
def multiple_list(single_list):
    """Linked list with multiple values."""
    single_list.add("value 2")
    return single_list


def test_linked_list_add_multiple(multiple_list):
    """
    GIVEN linked list with two nodes and a value
    WHEN add is called with the value
    THEN the second node has the value.
    """
    value = "value 3"

    multiple_list.add(value)

    assert multiple_list.head.next_.next_.value == value


def test_linked_list_traverse_empty(empty_list):
    """
    GIVEN empty list and mock function
    WHEN traverse is called with the mock function
    THEN the mock function is not called.
    """
    func = mock.MagicMock()

    empty_list.traverse(func)

    func.assert_not_called()


def test_linked_list_traverse_single(single_list):
    """
    GIVEN single list and mock function
    WHEN traverse is called with the mock function
    THEN the mock function is called with a single value.
    """
    func = mock.MagicMock()

    single_list.traverse(func)

    func.assert_called_once_with("value 1")


def test_linked_list_traverse_multiple(multiple_list):
    """
    GIVEN multiple list and mock function
    WHEN traverse is called with the mock function
    THEN the mock function is called with all values.
    """
    func = mock.MagicMock()

    multiple_list.traverse(func)

    assert func.call_count == 2
    func.assert_any_call("value 1")
    func.assert_called_with("value 2")
