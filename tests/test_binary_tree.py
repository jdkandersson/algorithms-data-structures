"""Tests for the binary tree."""
# pylint: disable=redefined-outer-name

from unittest import mock

import pytest

from library import binary_tree


@pytest.fixture
def leaf_node():
    """Get a leaf node."""
    return binary_tree.Node(0)


def test_insert_leaf_less(leaf_node: binary_tree.Node):
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


def test_insert_leaf_equal(leaf_node: binary_tree.Node):
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


def test_insert_leaf_greater(leaf_node: binary_tree.Node):
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


def test_insert_branch_less(branch_node: binary_tree.Node):
    """
    GIVEN branch node and value that is less than the node value
    WHEN insert is called with the value
    THEN the left child node insert is called with the value.
    """
    value = -1

    branch_node.insert(value)

    branch_node.left.insert.assert_called_once_with(value)


def test_insert_branch_equal(branch_node: binary_tree.Node):
    """
    GIVEN branch node and value that is equal to the node value
    WHEN insert is called with the value
    THEN the left child node insert is called with the value.
    """
    value = 0

    branch_node.insert(value)

    branch_node.left.insert.assert_called_once_with(value)


def test_insert_branch_greater(branch_node: binary_tree.Node):
    """
    GIVEN branch node and value that is greater than the node value
    WHEN insert is called with the value
    THEN the right child node insert is called with the value.
    """
    value = 1

    branch_node.insert(value)

    branch_node.right.insert.assert_called_once_with(value)
