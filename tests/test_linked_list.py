"""Tests for linked list."""

import pytest
from unittest import mock

from library import linked_list


@pytest.fixture
def empty_list():
    """Linked list with empty value."""
    list_ = linked_list.LinkedList()
    return list_


@pytest.fixture
def single_list(empty_list):
    """Linked list with single value."""
    empty_list.add_last("value 1")
    return empty_list


@pytest.fixture
def multiple_list(single_list):
    """Linked list with multiple values."""
    single_list.add_last("value 2")
    return single_list


def test_node_construct_no_next():
    """
    GIVEN value for node
    WHEN node is constructed with the value
    THEN the value is copied into the node and next_ is None.
    """
    value = "value 1"

    node = linked_list.Node(value)

    assert node.value == value
    assert node.next_ is None


def test_node_construct_with_next():
    """
    GIVEN value for node and next node
    WHEN node is constructed with the value and the next node
    THEN the value is copied into the node and next_ is the next node.
    """
    next_node = linked_list.Node("value 1")
    value = "value 2"

    node = linked_list.Node(value, next_node)

    assert node.value == value
    assert node.next_  is not linked_list.Node
    assert node.next_ .value == "value 1"


def test_linked_list_construct():
    """
    GIVEN
    WHEN linked list is constructed
    THEN head is None.
    """
    list_ = linked_list.LinkedList()

    assert list_.head is None


def test_linked_list_add_empty(empty_list):
    """
    GIVEN empty linked list value to add
    WHEN add is called with the value
    THEN head is replaced with a Node with value set to input value and next_ set to
        None.
    """
    list_ = linked_list.LinkedList()
    value = "value 1"

    list_.add_first(value)

    assert list_.head.value == value
    assert list_.head.next_ == None


def test_linked_list_add_single(single_list):
    """
    GIVEN linked list with single node and a value
    WHEN add is called with the value
    THEN head is changed to the new value referencing the old value.
    """
    value = "value 2"

    single_list.add_first(value)


    assert single_list.head.value == value
    assert single_list.head.next_ is not None
    assert single_list.head.next_.value == "value 1"
    assert single_list.head.next_.next_ is None


def test_linked_list_add_multiple(multiple_list):
    """
    GIVEN linked list with two nodes and a value
    WHEN add is called with the value
    THEN the second node has the value.
    """
    value = "value 3"

    multiple_list.add_first(value)

    assert multiple_list.head.value == value


def test_linked_list_add_end_empty(empty_list):
    """
    GIVEN empty linked list value to add_end
    WHEN add_end is called with the value
    THEN head is replaced with a Node with value set to input value and next_ set to
        None.
    """
    list_ = linked_list.LinkedList()
    value = "value 1"

    list_.add_last(value)

    assert list_.head.value == value
    assert list_.head.next_ == None


def test_linked_list_add_end_single(single_list):
    """
    GIVEN linked list with single node and a value
    WHEN add_end is called with the value
    THEN head references a Node with the value and None for next_.
    """
    value = "value 2"

    single_list.add_last(value)

    assert single_list.head.next_ is not None
    assert single_list.head.next_.value == value
    assert single_list.head.next_.next_ is None


def test_linked_list_add_end_multiple(multiple_list):
    """
    GIVEN linked list with two nodes and a value
    WHEN add_end is called with the value
    THEN the second node has the value.
    """
    value = "value 3"

    multiple_list.add_last(value)

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


def test_linked_list_search_empty(empty_list):
    """
    GIVEN empty list
    WHEN search is called
    THEN False is returned.
    """
    found = empty_list.search("value 1")

    assert not found


@pytest.mark.parametrize(
    "value, expected_found",
    [("value 2", False), ("value 1", True)],
    ids=["not in list", "in list"],
)
def test_linked_list_found_single(single_list, value, expected_found):
    """
    GIVEN single list, value to search for and expected found value
    WHEN search is called with the value
    THEN the expected found value is returned
    """
    found = single_list.search(value)

    assert found == expected_found


@pytest.mark.parametrize(
    "value, expected_found",
    [("value 3", False), ("value 2", True), ("value 1", True)],
    ids=["not in list", "in list", "in list"],
)
def test_linked_list_found_multiple(multiple_list, value, expected_found):
    """
    GIVEN multiple list, value to search for and expected found value
    WHEN search is called with the value
    THEN the expected found value is returned
    """
    found = multiple_list.search(value)

    assert found == expected_found


def test_linked_list_iter_empty(empty_list):
    """
    GIVEN empty list
    WHEN list is iterated
    THEN empty generator is returned.
    """
    assert list(iter(empty_list)) == []


def test_linked_list_iter_single(single_list):
    """
    GIVEN single list
    WHEN list is iterated
    THEN generator with single item is returned.
    """
    assert list(iter(single_list)) == ["value 1"]


def test_linked_list_iter_multiple(multiple_list):
    """
    GIVEN multiple list
    WHEN list is iterated
    THEN generator with multiple items is returned.
    """
    assert list(iter(multiple_list)) == ["value 1", "value 2"]


def test_insert_after_empty(empty_list):
    """
    GIVEN empty list and value
    WHEN insert_after is called with the value
    THEN value is not added.
    """
    value = "value 1"

    empty_list.insert_after(value, value)

    assert list(iter(empty_list)) == []


@pytest.mark.parametrize(
    "insert_after_value, expected_list",
    [("value 2", ["value 1"]), ("value 1", ["value 1", "value 2"])],
    ids=["value not in list", "value in list"]
)
def test_insert_after_single(single_list, insert_after_value, expected_list):
    """
    GIVEN single item list, value, value after which to insert and expected values
    WHEN insert_after is called with the value and value after which to insert
    THEN the linked list contains the expected values in the expected order.
    """
    value = "value 2"

    single_list.insert_after(insert_after_value, value)

    assert list(iter(single_list)) == expected_list


@pytest.mark.parametrize(
    "insert_after_value, expected_list",
    [
        ("value 3", ["value 1", "value 2"]),
        ("value 2", ["value 1", "value 2", "value 3"]),
        ("value 1", ["value 1", "value 3", "value 2"]),
    ],
    ids=["value not in list", "value in list last", "value in list first"]
)
def test_insert_after_multiple(multiple_list, insert_after_value, expected_list):
    """
    GIVEN multiple item list, value, value after which to insert and expected values
    WHEN insert_after is called with the value and value after which to insert
    THEN the linked list contains the expected values in the expected order.
    """
    value = "value 3"

    multiple_list.insert_after(insert_after_value, value)

    assert list(iter(multiple_list)) == expected_list
