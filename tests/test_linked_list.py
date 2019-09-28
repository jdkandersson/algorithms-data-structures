"""Tests for linked list."""
# pylint: disable=redefined-outer-name,unused-argument

from unittest import mock

import pytest

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


@pytest.fixture
def duplicate_list(single_list):
    """Linked list with duplicate values."""
    single_list.add_last("value 1")
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
    assert node.next_ is not linked_list.Node
    assert node.next_.value == "value 1"


def test_construct():
    """
    GIVEN
    WHEN linked list is constructed
    THEN head is None.
    """
    list_ = linked_list.LinkedList()

    assert list_.head is None


def test_add_empty(empty_list):
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
    assert list_.head.next_ is None


def test_add_single(single_list):
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


def test_add_multiple(multiple_list):
    """
    GIVEN linked list with two nodes and a value
    WHEN add is called with the value
    THEN the second node has the value.
    """
    value = "value 3"

    multiple_list.add_first(value)

    assert multiple_list.head.value == value


def test_add_last_empty(empty_list):
    """
    GIVEN empty linked list value to add_last
    WHEN add_last is called with the value
    THEN head is replaced with a Node with value set to input value and next_ set to
        None.
    """
    list_ = linked_list.LinkedList()
    value = "value 1"

    list_.add_last(value)

    assert list_.head.value == value
    assert list_.head.next_ is None


def test_add_last_single(single_list):
    """
    GIVEN linked list with single node and a value
    WHEN add_last is called with the value
    THEN head references a Node with the value and None for next_.
    """
    value = "value 2"

    single_list.add_last(value)

    assert single_list.head.next_ is not None
    assert single_list.head.next_.value == value
    assert single_list.head.next_.next_ is None


def test_add_last_multiple(multiple_list):
    """
    GIVEN linked list with two nodes and a value
    WHEN add_last is called with the value
    THEN the second node has the value.
    """
    value = "value 3"

    multiple_list.add_last(value)

    assert multiple_list.head.next_.next_.value == value


def test_traverse_empty(empty_list):
    """
    GIVEN empty list and mock function
    WHEN traverse is called with the mock function
    THEN the mock function is not called.
    """
    func = mock.MagicMock()

    empty_list.traverse(func)

    func.assert_not_called()


def test_traverse_single(single_list):
    """
    GIVEN single list and mock function
    WHEN traverse is called with the mock function
    THEN the mock function is called with a single value.
    """
    func = mock.MagicMock()

    single_list.traverse(func)

    func.assert_called_once_with("value 1")


def test_traverse_multiple(multiple_list):
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


def test_search_empty(empty_list):
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
def test_found_single(single_list, value, expected_found):
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
def test_found_multiple(multiple_list, value, expected_found):
    """
    GIVEN multiple list, value to search for and expected found value
    WHEN search is called with the value
    THEN the expected found value is returned
    """
    found = multiple_list.search(value)

    assert found == expected_found


def test_iter_empty(empty_list):
    """
    GIVEN empty list
    WHEN list is iterated
    THEN empty generator is returned.
    """
    assert list(iter(empty_list)) == []


def test_iter_single(single_list):
    """
    GIVEN single list
    WHEN list is iterated
    THEN generator with single item is returned.
    """
    assert list(iter(single_list)) == ["value 1"]


def test_iter_multiple(multiple_list):
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
    "key, expected_list",
    [("value 2", ["value 1"]), ("value 1", ["value 1", "value 2"])],
    ids=["value not in list", "value in list"],
)
def test_insert_after_single(single_list, key, expected_list):
    """
    GIVEN single item list, value, key and expected list
    WHEN insert_after is called with the value and key
    THEN the linked list contains the expected values in the expected order.
    """
    value = "value 2"

    single_list.insert_after(key, value)

    assert list(iter(single_list)) == expected_list


@pytest.mark.parametrize(
    "key, expected_list",
    [
        ("value 3", ["value 1", "value 2"]),
        ("value 2", ["value 1", "value 2", "value 3"]),
        ("value 1", ["value 1", "value 3", "value 2"]),
    ],
    ids=["value not in list", "value in list last", "value in list first"],
)
def test_insert_after_multiple(multiple_list, key, expected_list):
    """
    GIVEN multiple item list, value, key and expected list
    WHEN insert_after is called with the value and key
    THEN the linked list contains the expected values in the expected order.
    """
    value = "value 3"

    multiple_list.insert_after(key, value)

    assert list(iter(multiple_list)) == expected_list


def test_insert_after_duplicate(duplicate_list):
    """
    GIVEN duplicate item list, value and key that is equal to the duplicate value
    WHEN insert_after is called with the value and key
    THEN new value is inserted after the first matched item.
    """
    value = "value 2"

    duplicate_list.insert_after("value 1", value)

    assert list(iter(duplicate_list)) == ["value 1", "value 2", "value 1"]


def test_insert_before_empty(empty_list):
    """
    GIVEN empty list and value
    WHEN insert_before is called with the value
    THEN value is not added.
    """
    value = "value 1"

    empty_list.insert_before(value, value)

    assert list(iter(empty_list)) == []


@pytest.mark.parametrize(
    "key, expected_list",
    [("value 2", ["value 1"]), ("value 1", ["value 2", "value 1"])],
    ids=["value not in list", "value in list"],
)
def test_insert_before_single(single_list, key, expected_list):
    """
    GIVEN single item list, value, key and expected list
    WHEN insert_before is called with the value and key
    THEN the linked list contains the expected values in the expected order.
    """
    value = "value 2"

    single_list.insert_before(key, value)

    assert list(iter(single_list)) == expected_list


@pytest.mark.parametrize(
    "key, expected_list",
    [
        ("value 3", ["value 1", "value 2"]),
        ("value 2", ["value 1", "value 3", "value 2"]),
        ("value 1", ["value 3", "value 1", "value 2"]),
    ],
    ids=["value not in list", "value in list last", "value in list first"],
)
def test_insert_before_multiple(multiple_list, key, expected_list):
    """
    GIVEN multiple item list, value, key and expected list
    WHEN insert_before is called with the value and key
    THEN the linked list contains the expected values in the expected order.
    """
    value = "value 3"

    multiple_list.insert_before(key, value)

    assert list(iter(multiple_list)) == expected_list


def test_insert_before_duplicate(duplicate_list):
    """
    GIVEN duplicate item list, value and key that is equal to the duplicate value
    WHEN insert_before is called with the value and key
    THEN new value is inserted before the first matched item.
    """
    value = "value 2"

    duplicate_list.insert_before("value 1", value)

    assert list(iter(duplicate_list)) == ["value 2", "value 1", "value 1"]


def test_delete_empty(empty_list):
    """
    GIVEN empty list and key
    WHEN delete is called with the key
    THEN list stays empty.
    """
    key = "value 1"

    empty_list.delete(key)

    assert list(iter(empty_list)) == []


@pytest.mark.parametrize(
    "key, expected_list",
    [("value 2", ["value 1"]), ("value 1", [])],
    ids=["value not in list", "value in list"],
)
def test_delete_single(single_list, key, expected_list):
    """
    GIVEN single item list, key and expected list
    WHEN delete is called with the key
    THEN the linked list contains the expected values in the expected order.
    """
    single_list.delete(key)

    assert list(iter(single_list)) == expected_list


@pytest.mark.parametrize(
    "key, expected_list",
    [
        ("value 3", ["value 1", "value 2"]),
        ("value 2", ["value 1"]),
        ("value 1", ["value 2"]),
    ],
    ids=["value not in list", "value in list last", "value in list first"],
)
def test_delete_multiple(multiple_list, key, expected_list):
    """
    GIVEN multiple item list, key and expected list
    WHEN delete is called with the key
    THEN the linked list contains the expected values in the expected order.
    """
    multiple_list.delete(key)

    assert list(iter(multiple_list)) == expected_list


def test_delete_duplicate(duplicate_list):
    """
    GIVEN duplicate item list and value that is equal to the duplicate value
    WHEN delete is called with the value
    THEN the first matched value is removed from the list.
    """
    value = "value 1"

    duplicate_list.delete(value)

    assert list(iter(duplicate_list)) == ["value 1"]


def test_clone_empty(empty_list):
    """
    GIVEN empty list
    WHEN clone is called
    THEN a new empty list is returned.
    """
    new_list = empty_list.clone()

    assert list(iter(new_list)) == list(iter(empty_list))
    assert id(new_list) != id(empty_list)


def test_clone_single(single_list):
    """
    GIVEN single list
    WHEN clone is called
    THEN a new single list is returned with all nodes copied.
    """
    new_list = single_list.clone()

    assert list(iter(new_list)) == list(iter(single_list))
    assert id(new_list) != id(single_list)
    node = single_list.head
    new_node = new_list.head
    while node is not None:
        assert id(node) != id(new_node)
        node = node.next_
        new_node = new_node.next_


def test_clone_multiple(multiple_list):
    """
    GIVEN multiple list
    WHEN clone is called
    THEN a new multiple list is returned with all nodes copied.
    """
    new_list = multiple_list.clone()

    assert list(iter(new_list)) == list(iter(multiple_list))
    assert id(new_list) != id(multiple_list)
    node = multiple_list.head
    new_node = new_list.head
    while node is not None:
        assert id(node) != id(new_node)
        node = node.next_
        new_node = new_node.next_


def test_clone_duplicate(duplicate_list):
    """
    GIVEN duplicate list
    WHEN clone is called
    THEN a new duplicate list is returned with all nodes copied.
    """
    new_list = duplicate_list.clone()

    assert list(iter(new_list)) == list(iter(duplicate_list))
    assert id(new_list) != id(duplicate_list)
    node = duplicate_list.head
    new_node = new_list.head
    while node is not None:
        assert id(node) != id(new_node)
        node = node.next_
        new_node = new_node.next_


def test_is_empty_empty(empty_list):
    """
    GIVEN empty list
    WHEN is_empty is called
    THEN True is returned.
    """
    assert empty_list.is_empty() is True


def test_is_empty_single(single_list):
    """
    GIVEN single item list
    WHEN is_empty is called
    THEN False is returned.
    """
    assert single_list.is_empty() is False


def test_is_empty_multiple(multiple_list):
    """
    GIVEN multiple item list
    WHEN is_empty is called
    THEN False is returned.
    """
    assert multiple_list.is_empty() is False


def test_clear_empty(empty_list):
    """
    GIVEN empty list
    WHEN clear is called
    THEN list is empty.
    """
    empty_list.clear()

    assert empty_list.is_empty() is True


def test_clear_single(single_list):
    """
    GIVEN single item list
    WHEN clear is called
    THEN list is empty.
    """
    single_list.clear()

    assert single_list.is_empty() is True


def test_clear_multiple(multiple_list):
    """
    GIVEN multiple item list
    WHEN clear is called
    THEN list is empty.
    """
    multiple_list.clear()

    assert multiple_list.is_empty() is True
