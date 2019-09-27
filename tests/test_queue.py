"""Tests for queue."""
# pylint: disable=redefined-outer-name

import pytest

from library import queue


@pytest.mark.parametrize(
    "length, operations, exception",
    [
        (0, ["deq"], queue.QueueEmptyError),
        (0, ["enq"], queue.QueueFullError),
        (1, ["enq", "enq"], queue.QueueFullError),
        (1, ["enq", "deq", "deq"], queue.QueueEmptyError),
    ],
    ids=["0,deq", "0,enq", "1,enq-enq", "1,enq-deq-deq"],
)
def test_end_deq_raise(length, operations, exception):
    """
    GIVEN length of queue, operations to perform and exception that should be raised
    WHEN queue with the length is constructed and the operations are performed
    THEN the exception is raised
    """
    test_queue = queue.Queue(length)

    def perform_operation(operation):
        if operation == "enq":
            test_queue.enqueue("value")
        elif operation == "deq":
            test_queue.dequeue()
        else:
            raise Exception

    for idx, operation in enumerate(operations):
        if idx == len(operations) - 1:
            with pytest.raises(exception):
                perform_operation(operation)
            continue
        perform_operation(operation)


@pytest.mark.parametrize(
    "length, actions",
    [
        (1, [("enq", "value 1"), ("deq", "value 1")]),
        (
            1,
            [
                ("enq", "value 1"),
                ("deq", "value 1"),
                ("enq", "value 1"),
                ("deq", "value 1"),
            ],
        ),
        (
            2,
            [
                ("enq", "value 1"),
                ("enq", "value 2"),
                ("deq", "value 1"),
                ("enq", "value 3"),
                ("deq", "value 2"),
                ("deq", "value 3"),
            ],
        ),
    ],
    ids=["1,enq-deq", "1,enq-deq-enq-deq", "2,enq-enq-deq-enq-deq-deq"],
)
def test_enqueue_dequeue(length, actions):
    """
    GIVEN list of enqueue (with value to enqueue) and dequeue (with value expected to
        be dequeued) actions and the length of a queue
    WHEN actions are performed
    THE expected values are dequeued.
    """
    test_queue = queue.Queue(length)

    for action in actions:
        operation, value = action

        if operation == "enq":
            test_queue.enqueue(value)
        elif operation == "deq":
            assert test_queue.dequeue() == value


def test_get_front_empty():
    """
    GIVEN empty queue
    WHEN get_front is called
    THEN queueEmptyError is raised.
    """
    test_queue = queue.Queue()

    with pytest.raises(queue.QueueEmptyError):
        test_queue.get_front()


def test_get_front_single():
    """
    GIVEN queue with a single value
    WHEN get_front is called
    THEN the value is returned and can still be dequeued.
    """
    test_queue = queue.Queue()
    value = "value 1"
    test_queue.enqueue(value)

    returned_value = test_queue.get_front()

    assert returned_value == value
    assert test_queue.dequeue() == value


def test_get_front_multiple():
    """
    GIVEN queue with a multiple values
    WHEN get_front is called
    THEN the front value is returned.
    """
    test_queue = queue.Queue()
    test_queue.enqueue("value 1")
    test_queue.enqueue("value 2")

    returned_value = test_queue.get_front()

    assert returned_value == "value 1"


def test_is_empty_empty():
    """
    GIVEN empty queue
    WHEN is_empty is called
    THEN True is returned.
    """
    test_queue = queue.Queue()

    result = test_queue.is_empty()

    assert result is True


def test_is_empty_not_empty():
    """
    GIVEN queue that is not empty
    WHEN is_empty is called
    THEN False is returned.
    """
    test_queue = queue.Queue()
    test_queue.enqueue("value 1")

    result = test_queue.is_empty()

    assert result is False


def test_clear():
    """
    GIVEN queue with length 1 with an item
    WHEN clear is called
    THEN the queue is empty and can be filled up again.
    """
    test_queue = queue.Queue(1)
    test_queue.enqueue("value 1")

    test_queue.clear()

    assert test_queue.is_empty() is True
    test_queue.enqueue("value 2")
