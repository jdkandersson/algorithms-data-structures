"""Tests for the binary tree."""
# pylint: disable=redefined-outer-name

from unittest import mock

import pytest

from library import binary_tree


@pytest.fixture
def leaf_node():
    """Get a leaf node."""
    return binary_tree.Node(0)


def test_node_leaf_insert_less(leaf_node: binary_tree.Node):
    """
    GIVEN leaf node and value that is less than the node value
    WHEN insert is called with the value
    THEN a new leaf node is inserted on the left with the value.
    """
    value = -1

    leaf_node.insert(value)

    assert leaf_node.left is not None
    assert leaf_node.left.value == value
    assert leaf_node.left.left is None
    assert leaf_node.left.right is None


def test_node_leaf_insert_equal(leaf_node: binary_tree.Node):
    """
    GIVEN leaf node and value that is equal to the node value
    WHEN insert is called with the value
    THEN a new leaf node is inserted on the left with the value.
    """
    value = 0

    leaf_node.insert(value)

    assert leaf_node.left is not None
    assert leaf_node.left.value == value
    assert leaf_node.left.left is None
    assert leaf_node.left.right is None


def test_node_leaf_insert_greater(leaf_node: binary_tree.Node):
    """
    GIVEN leaf node and value that is greater than the node value
    WHEN insert is called with the value
    THEN a new leaf node is inserted on the right with the value.
    """
    value = 1

    leaf_node.insert(value)

    assert leaf_node.right is not None
    assert leaf_node.right.value == value
    assert leaf_node.right.left is None
    assert leaf_node.right.right is None


@pytest.fixture
def branch_node(leaf_node: binary_tree.Node):
    """Get a branch node with mocked children."""
    leaf_node.left = mock.MagicMock()
    leaf_node.right = mock.MagicMock()
    return leaf_node


def test_node_branch_insert_less(branch_node: binary_tree.Node):
    """
    GIVEN branch node and value that is less than the node value
    WHEN insert is called with the value
    THEN the left child node insert is called with the value.
    """
    value = -1

    branch_node.insert(value)

    branch_node.left.insert.assert_called_once_with(value)


def test_node_branch_insert_equal(branch_node: binary_tree.Node):
    """
    GIVEN branch node and value that is equal to the node value
    WHEN insert is called with the value
    THEN the left child node insert is called with the value.
    """
    value = 0

    branch_node.insert(value)

    branch_node.left.insert.assert_called_once_with(value)


def test_node_branch_insert_greater(branch_node: binary_tree.Node):
    """
    GIVEN branch node and value that is greater than the node value
    WHEN insert is called with the value
    THEN the right child node insert is called with the value.
    """
    value = 1

    branch_node.insert(value)

    branch_node.right.insert.assert_called_once_with(value)


@pytest.mark.parametrize(
    "value, expected_value",
    [(0, 0), (-1, None), (1, None)],
    ids=["hit", "miss less", "miss greater"],
)
def test_node_leaf_search(value, expected_value, leaf_node):
    """
    GIVEN leaf node, value to search for and expected value
    WHEN search is called on the node with the value
    THEN the expected value is returned.
    """
    returned_value = leaf_node.search(value)

    assert returned_value == expected_value


def test_node_branch_search_less_call(branch_node: binary_tree.Node):
    """
    GIVEN branch node and value that is less than the node value
    WHEN search is called with the value
    THEN the left child node search is called with the value.
    """
    value = -1

    branch_node.search(value)

    branch_node.left.search.assert_called_once_with(value)


def test_node_branch_search_less_return(branch_node: binary_tree.Node):
    """
    GIVEN branch node and value that is less than the node value
    WHEN search is called with the value
    THEN the left child node search return value is returned.
    """
    value = -1

    return_value = branch_node.search(value)

    assert return_value == branch_node.left.search.return_value


def test_node_branch_search_greater_call(branch_node: binary_tree.Node):
    """
    GIVEN branch node and value that is greater than the node value
    WHEN search is called with the value
    THEN the right child node search is called with the value.
    """
    value = 1

    branch_node.search(value)

    branch_node.right.search.assert_called_once_with(value)


def test_node_branch_search_greater_return(branch_node: binary_tree.Node):
    """
    GIVEN branch node and value that is greater than the node value
    WHEN search is called with the value
    THEN the right child node search return value is returned.
    """
    value = 1

    return_value = branch_node.search(value)

    assert return_value == branch_node.right.search.return_value


def test_node_leaf_get_smallest(leaf_node):
    """
    GIVEN leaf node
    WHEN get_smallest is called
    THEN the node value is returned.
    """
    value = leaf_node.get_smallest()

    assert value == 0


def test_node_branch_get_smallest_call(branch_node):
    """
    GIVEN branch node
    WHEN get_smallest is called
    THEN the left node get_smallest is called.
    """
    branch_node.get_smallest()

    branch_node.left.get_smallest.assert_called_once_with()


def test_node_branch_get_smallest_return(branch_node):
    """
    GIVEN branch node
    WHEN get_smallest is called
    THEN the left node get_smallest return value is returned.
    """
    value = branch_node.get_smallest()

    assert value == branch_node.left.get_smallest.return_value


@pytest.mark.parametrize(
    "args, expected_result",
    [
        ((0, None, None), True),
        ((0, binary_tree.Node(-1), None), False),
        ((0, None, binary_tree.Node(1)), False),
        ((0, binary_tree.Node(-1), binary_tree.Node(1)), False),
    ],
    ids=["leaf", "branch left only", "branch right only", "branch with both"],
)
def test_is_leaf(args, expected_result):
    """
    GIVEN arguments to construct a node and expected result
    WHEN the node is constructed with the arguments and is_leaf is called
    THEN the returned result is the expected result.
    """
    test_node = binary_tree.Node(*args)

    result = test_node.is_leaf()

    assert result == expected_result


def test_delete_leaf_hit(leaf_node):
    """
    GIVEN leaf node and value that is equal to the node value
    WHEN delete is called with the value
    THEN None is returned.
    """
    new_root = leaf_node.delete(0)

    assert new_root is None


@pytest.mark.parametrize("value", [-1, 1], ids=["less", "more"])
def test_delete_leaf_miss(leaf_node, value):
    """
    GIVEN leaf node and value that is different to the node value
    WHEN delete is called with the value
    THEN ValueError is raised.
    """
    with pytest.raises(ValueError):
        leaf_node.delete(value)
