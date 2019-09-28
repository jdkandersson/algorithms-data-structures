"""Tests for the hash map bucket."""
# pylint: disable=protected-access

from unittest import mock

import pytest

from library.hash_map import bucket


@pytest.fixture
def empty_bucket():
    """Return empty bucket."""
    return bucket.Bucket()


@pytest.fixture
def single_bucket(empty_bucket):  # pylint: disable=redefined-outer-name
    """Return single element bucket."""
    empty_bucket.insert("key 1", "value 1")
    return empty_bucket


@pytest.fixture
def multiple_bucket(single_bucket):  # pylint: disable=redefined-outer-name
    """Return multiple element bucket."""
    single_bucket.insert("key 2", "value 2")
    return single_bucket


def test_insert_integration():
    """
    GIVEN _list of bucket returns False for is_empty
    WHEN insert is called
    THEN then the is_empty function returns True.
    """
    test_bucket = bucket.Bucket()
    assert test_bucket._list.is_empty() is True

    test_bucket.insert("key 1", "value 1")

    assert test_bucket._list.is_empty() is False


def test_insert_call():
    """
    GIVEN key and value and mocked bucket list
    WHEN insert is called with the key and value
    THEN the bucket list is called with the key and value as a tuple.
    """
    key = "key 1"
    value = "value 1"
    test_bucket = bucket.Bucket()
    test_bucket._list = mock.MagicMock()

    test_bucket.insert(key, value)

    test_bucket._list.add_first.assert_called_once_with((key, value))


def test_get_empty(empty_bucket):  # pylint: disable=redefined-outer-name
    """
    GIVEN empty bucket
    WHEN get is called
    THEN KeyError is raised.
    """
    with pytest.raises(KeyError):
        empty_bucket.get("key 1")


def test_get_single(single_bucket):  # pylint: disable=redefined-outer-name
    """
    GIVEN bucket with single element
    WHEN get is called with the key of the element
    THEN the value of the element is returned.
    """
    returned_value = single_bucket.get("key 1")

    assert returned_value == "value 1"


def test_get_single_different(single_bucket):  # pylint: disable=redefined-outer-name
    """
    GIVEN bucket with single element and a different key
    WHEN get is called with the key
    THEN KeyError is raised.
    """
    with pytest.raises(KeyError):
        single_bucket.get("key 2")


def test_get_multiple(multiple_bucket):  # pylint: disable=redefined-outer-name
    """
    GIVEN bucket with multiple elements
    WHEN get is called with the key for each element
    THEN the value of the element is returned.
    """
    for idx in range(2):
        element_number = idx + 1
        assert multiple_bucket.get(f"key {element_number}") == f"value {element_number}"


@pytest.mark.parametrize(
    "keys, key, expected_result",
    [
        ([], "key 1", False),
        (["key 1"], "key 2", False),
        (["key 1"], "key 1", True),
        (["key 1", "key 2"], "key 3", False),
        (["key 1", "key 2"], "key 2", True),
        (["key 1", "key 2"], "key 1", True),
    ],
    ids=[
        "empty",
        "single-miss",
        "single-hit",
        "multiple-miss",
        "multiple-first-hit",
        "multiple-second-hit",
    ],
)
def test_exists(keys, key, expected_result):
    """
    GIVEN keys to add, key to check for and expected exists result
    WHEN keys are added to the bucket and exists is called with the key
    THEN the expected result is returned.
    """
    test_bucket = bucket.Bucket()
    for insert_key in keys:
        test_bucket.insert(insert_key, "value")

    result = test_bucket.exists(key)

    assert result == expected_result


def test_is_empty_empty(empty_bucket):  # pylint: disable=redefined-outer-name
    """
    GIVEN empty bucket
    WHEN is_empty is called
    THEN True is returned.
    """
    assert empty_bucket.is_empty() is True


def test_is_empty_single(single_bucket):  # pylint: disable=redefined-outer-name
    """
    GIVEN single element bucket
    WHEN is_empty is called
    THEN False is returned.
    """
    assert single_bucket.is_empty() is False


def test_delete_empty(empty_bucket):  # pylint: disable=redefined-outer-name
    """
    GIVEN empty bucket
    WHEN delete is called
    THEN KeyError is raised.
    """
    with pytest.raises(KeyError):
        empty_bucket.delete("key 1")


def test_delete_single(single_bucket):  # pylint: disable=redefined-outer-name
    """
    GIVEN single element bucket
    WHEN delete is called with the key of the element
    THEN the bucket is empty.
    """
    single_bucket.delete("key 1")

    assert single_bucket.is_empty() is True


def test_iter(multiple_bucket):  # pylint: disable=redefined-outer-name
    """
    GIVEN multiple element bucket
    WHEN bucket is iterated and converted to a list
    THEN the elements in the bucket are returned.
    """
    assert list(iter(multiple_bucket)) == [("key 2", "value 2"), ("key 1", "value 1")]


def test_clear(single_bucket):  # pylint: disable=redefined-outer-name
    """
    GIVEN single element bucket
    WHEN clear is called
    THEN bucket is empty.
    """
    single_bucket.clear()

    assert single_bucket.is_empty() is True
