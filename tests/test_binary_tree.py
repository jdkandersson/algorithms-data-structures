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


@pytest.mark.parametrize(
    "args, expected_values",
    [
        ((0,), [0]),
        ((0, binary_tree.Node(-1)), [-1, 0]),
        ((0, None, binary_tree.Node(1)), [0, 1]),
        ((0, binary_tree.Node(-1), binary_tree.Node(1)), [-1, 0, 1]),
    ],
    ids=["leaf", "branch right only", "branch left only", "branch"],
)
def test_iter(args, expected_values):
    """
    GIVEN args for node construction and expected values
    WHEN node is constructed with the args and iterated
    THEN the expected values are returned.
    """
    test_node = binary_tree.Node(*args)

    values = list(iter(test_node))

    assert values == expected_values


def test_delete_branch_hit_single_left():
    """
    GIVEN branch node that has a left child and value that is equal to the node value
    WHEN delete is called with the value
    THEN the left child is returned with the correct value.
    """
    left_child = binary_tree.Node(-1)
    test_node = binary_tree.Node(0, left_child)

    new_root = test_node.delete(0)

    assert id(left_child) == id(new_root)
    assert new_root.value == -1


def test_delete_branch_hit_single_right():
    """
    GIVEN branch node that has a left child and value that is equal to the node value
    WHEN delete is called with the value
    THEN the left child is returned with the correct value.
    """
    right_child = binary_tree.Node(1)
    test_node = binary_tree.Node(0, None, right_child)

    new_root = test_node.delete(0)

    assert id(right_child) == id(new_root)
    assert new_root.value == 1


def test_delete_branch_hit_get_smallest_call(branch_node):
    """
    GIVEN branch node and value that is equal to the node value
    WHEN delete is called with the value
    THEN get_smallest is called on the right child node.
    """
    right_child = branch_node.right

    branch_node.delete(0)

    right_child.get_smallest.assert_called_once_with()


def test_delete_branch_hit_value(branch_node):
    """
    GIVEN branch node and value that is equal to the node value
    WHEN delete is called with the value
    THEN get_smallest right node return value is set to the value.
    """
    right_child = branch_node.right

    branch_node.delete(0)

    assert branch_node.value == right_child.get_smallest.return_value


def test_delete_branch_hit_delete_call(branch_node):
    """
    GIVEN branch node and value that is equal to the node value
    WHEN delete is called with the value
    THEN delete is called on the right node with the get_smallest right node return
        value.
    """
    right_child = branch_node.right

    branch_node.delete(0)

    right_child.delete.assert_called_once_with(right_child.get_smallest.return_value)


def test_delete_branch_hit_right_child(branch_node):
    """
    GIVEN branch node and value that is equal to the node value
    WHEN delete is called with the value
    THEN right child is set to the right child delete return value.
    """
    right_child = branch_node.right

    branch_node.delete(0)

    assert branch_node.right == right_child.delete.return_value


def test_delete_branch_hit_return(branch_node):
    """
    GIVEN branch node and value that is equal to the node value
    WHEN delete is called with the value
    THEN the node is returned.
    """
    new_root = branch_node.delete(0)

    assert id(new_root) == id(branch_node)


def test_delete_branch_miss_left_call(branch_node):
    """
    GIVEN branch node and value that is less than the node value
    WHEN delete is called with the value
    THEN the left child delete is called with the value.
    """
    left_child = branch_node.left

    branch_node.delete(-1)

    left_child.delete.assert_called_once_with(-1)


def test_delete_branch_miss_left_left(branch_node):
    """
    GIVEN branch node and value that is less than the node value
    WHEN delete is called with the value
    THEN the left child  is set to the left child delete return value.
    """
    left_child = branch_node.left

    branch_node.delete(-1)

    assert branch_node.left == left_child.delete.return_value


def test_delete_branch_miss_left_return(branch_node):
    """
    GIVEN branch node and value that is less than the node value
    WHEN delete is called with the value
    THEN the node is returned.
    """
    new_root = branch_node.delete(-1)

    assert id(new_root) == id(branch_node)


def test_delete_branch_miss_right_call(branch_node):
    """
    GIVEN branch node and value that is greater than the node value
    WHEN delete is called with the value
    THEN the right child delete is called with the value.
    """
    right_child = branch_node.right

    branch_node.delete(1)

    right_child.delete.assert_called_once_with(1)


def test_delete_branch_miss_right_right(branch_node):
    """
    GIVEN branch node and value that is greater than the node value
    WHEN delete is called with the value
    THEN the right child  is set to the right child delete return value.
    """
    right_child = branch_node.right

    branch_node.delete(1)

    assert branch_node.right == right_child.delete.return_value


def test_delete_branch_miss_right_return(branch_node):
    """
    GIVEN branch node and value that is greater than the node value
    WHEN delete is called with the value
    THEN the node is returned.
    """
    new_root = branch_node.delete(1)

    assert id(new_root) == id(branch_node)


@pytest.mark.parametrize(
    "value, expected_values",
    [
        (-3, [-2, -1, 0, 1, 2, 3]),
        (-2, [-3, -1, 0, 1, 2, 3]),
        (-1, [-3, -2, 0, 1, 2, 3]),
        (0, [-3, -2, -1, 1, 2, 3]),
        (1, [-3, -2, -1, 0, 2, 3]),
        (2, [-3, -2, -1, 0, 1, 3]),
        (3, [-3, -2, -1, 0, 1, 2]),
    ],
    ids=[
        "left child's left child",
        "left child",
        "left child's right child",
        "root",
        "right child's left child",
        "right child",
        "right child's right child",
    ],
)
def test_delete_integration(value, expected_values):
    """
    GIVEN node with many child nodes, value to delete and expected tree contents
    WHEN delete is called with the value
    THEN the tree contains the expected values.
    """
    left_child = binary_tree.Node(-2, binary_tree.Node(-3), binary_tree.Node(-1))
    right_child = binary_tree.Node(2, binary_tree.Node(1), binary_tree.Node(3))
    test_node = binary_tree.Node(0, left_child, right_child)

    new_root = test_node.delete(value)

    assert list(iter(new_root)) == expected_values


@pytest.mark.parametrize(
    "values, expected_values",
    [
        ([], []),
        ([0], [0]),
        ([-1, 0, 1], [-1, 0, 1]),
        ([0, -1, 1], [-1, 0, 1]),
        ([-1, 1, 0], [-1, 0, 1]),
    ],
    ids=[
        "empty",
        "single",
        "multiple in order",
        "multiple pre order",
        "multiple post order",
    ],
)
def test_binary_tree_insert(values, expected_values):
    """
    GIVEN values to insert and expected values
    WHEN binary tree is constructed, the values are inserted and the tree is iterated
    THEN the tree contains all inserted values in the correct order.
    """
    test_binary_tree = binary_tree.BinaryTree()
    for value in values:
        test_binary_tree.insert(value)

    returned_values = list(iter(test_binary_tree))

    assert returned_values == expected_values


def test_binary_tree_delete_empty():
    """
    GIVEN empty binary tree
    WHEN delete is called
    THEN ValueError is raised.
    """
    test_binary_tree = binary_tree.BinaryTree()

    with pytest.raises(ValueError):
        test_binary_tree.delete(0)


@pytest.mark.parametrize(
    "values, delete_value, expected_values",
    [
        ([0], 0, []),
        ([-1, 0, 1], -1, [0, 1]),
        ([-1, 0, 1], 0, [-1, 1]),
        ([-1, 0, 1], 1, [-1, 0]),
    ],
    ids=["single", "multiple first", "multiple middle", "multiple last"],
)
def test_binary_tree_delete(values, delete_value, expected_values):
    """
    GIVEN values to insert, value to delete and expected values
    WHEN values are inserted into a binary tree the value is deleted
    THEN the tree contains the expected values when it is iterated.
    """
    test_binary_tree = binary_tree.BinaryTree()
    for value in values:
        test_binary_tree.insert(value)
    test_binary_tree.delete(delete_value)

    returned_values = list(iter(test_binary_tree))
    assert returned_values == expected_values


@pytest.mark.parametrize(
    "values, search_value, expected_result",
    [
        ([], 0, None),
        ([0], 0, 0),
        ([0], 1, None),
        ([-1, 0, 1], -2, None),
        ([-1, 0, 1], -1, -1),
        ([-1, 0, 1], 0, 0),
        ([-1, 0, 1], 1, 1),
        ([-1, 0, 1], 2, None),
    ],
    ids=[
        "empty",
        "single hit",
        "single miss",
        "multiple miss left",
        "multiple first",
        "multiple middle",
        "multiple last",
        "multiple miss right",
    ],
)
def test_binary_tree_search(values, search_value, expected_result):
    """
    GIVEN values to insert, value to search for and expected result
    WHEN values are inserted into the tree and the value is searched for
    THEN the expected result is returned.
    """
    test_binary_tree = binary_tree.BinaryTree()
    for value in values:
        test_binary_tree.insert(value)

    result = test_binary_tree.search(search_value)

    assert result == expected_result
