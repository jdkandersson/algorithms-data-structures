"""Tests for the stack."""

import pytest

from library import stack


@pytest.mark.parametrize(
    "values",
    [
        (),
        ("value 1"),
        ("value 1", "value 2"),
    ],
    ids=["empty", "single", "multiple"]
)
def test_push_pop(values):
    """
    GIVEN values
    WHEN a stack is created, all values are added and then popped back
    THEN values are returned in the first in last out order and StackEmptyError is
        raised after all values are popped.
    """
    test_stack = stack.Stack()

    for value in values:
        test_stack.push(value)

    for expected_value in reversed(values):
        value = test_stack.pop()
        assert value == expected_value

    with pytest.raises(stack.StackEmptyError):
        test_stack.pop()


def test_peek_empty():
    """
    GIVEN empty stack
    WHEN peek is called
    THEN StackEmptyError is raised.
    """
    test_stack = stack.Stack()

    with pytest.raises(stack.StackEmptyError):
        test_stack.peek()


@pytest.mark.parametrize(
    "values, expected_value",
    [
        (("value 1",), "value 1"),
        (("value 1", "value 2"), "value 2"),
    ]
)
def test_peek_single(values, expected_value):
    """
    GIVEN values to push and expected value
    WHEN values are pushed onto the stack and peek is called
    THEN the expected value is returned.
    """
    test_stack = stack.Stack()
    for value in values:
        test_stack.push(value)

    returned_value = test_stack.peek()

    assert returned_value == expected_value
