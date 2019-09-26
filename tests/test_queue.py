"""Tests for queue."""
# pylint: disable=redefined-outer-name

import pytest

from library import queue


@pytest.mark.parametrize(
    "actions",
    [
        [("enq", "value 1"), ("deq", "value 1")],
        [
            ("enq", "value 1"),
            ("deq", "value 1"),
            ("enq", "value 1"),
            ("deq", "value 1"),
        ],
        [
            ("enq", "value 1"),
            ("enq", "value 2"),
            ("deq", "value 1"),
            ("deq", "value 2"),
        ],
        [
            ("enq", "value 1"),
            ("enq", "value 2"),
            ("enq", "value 3"),
            ("deq", "value 1"),
            ("deq", "value 2"),
            ("deq", "value 3"),
        ],
    ],
    ids=["enq-deq", "enq-deq-enq-deq", "enq-enq-deq-deq", "enq-enq-enq-deq-deq-deq"],
)
def test_enqueue_dequeue(actions):
    """
    GIVEN list of enqueue (with value to enqueue) and dequeue (with value expected to
        be dequeued) actions
    WHEN actions are performed
    THE expected values are dequeued and QueueEmptyError is raised on final dequeue.
    """
    test_queue = queue.Queue()

    for action in actions:
        operation, value = action

        if operation == "enq":
            test_queue.enqueue(value)
        elif operation == "deq":
            assert test_queue.dequeue() == value

    with pytest.raises(queue.QueueEmptyError):
        test_queue.dequeue()


def test_peek_empty():
    """
    GIVEN empty queue
    WHEN peek is called
    THEN queueEmptyError is raised.
    """
    test_queue = queue.Queue()

    with pytest.raises(queue.QueueEmptyError):
        test_queue.peek()


@pytest.mark.parametrize(
    ("values", "expected_value"),
    [(("value 1",), "value 1"), (("value 1", "value 2"), "value 1")],
)
def test_peek(values, expected_value):
    """
    GIVEN values to enqueue
    WHEN they are enqueued and peek is called
    THEN the expected value is returned and all values can still be dequeued.
    """
    test_queue = queue.Queue()
    for value in values:
        test_queue.enqueue(value)

    value = test_queue.peek()

    assert value == expected_value

    for value in values:
        assert test_queue.dequeue() == value


@pytest.mark.parametrize(
    ("values", "expected_result"),
    [((), True), (("value 1",), False), (("value 1", "value 2"), False)],
)
def test_is_empty(values, expected_result):
    """
    GIVEN values to enqueue
    WHEN they are enqueued and is_empty is called
    THEN the expected result is returned.
    """
    test_queue = queue.Queue()
    for value in values:
        test_queue.enqueue(value)

    result = test_queue.is_empty()

    assert result == expected_result


@pytest.mark.parametrize(
    "values",
    [[], ["value 1"], ["value 1", "value 2"]],
    ids=["empty", "single", "multiple"],
)
def test_clear(values):
    """
    GIVEN values to enqueue
    WHEN values are enqueued and clear is called
    THEN the queue is empty.
    """
    test_queue = queue.Queue()
    for value in values:
        test_queue.enqueue(value)

    test_queue.clear()

    assert test_queue.is_empty() is True
