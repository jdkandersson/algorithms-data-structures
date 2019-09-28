"""Tests for the hash map bucket."""
# pylint: disable=protected-access

from unittest import mock

import pytest

from library.hash_map import bucket


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


def test_get_empty():
    """
    GIVEN empty bucket
    WHEN get is called
    THEN KeyError is raised.
    """
    test_bucket = bucket.Bucket()

    with pytest.raises(KeyError):
        test_bucket.get("key 1")


def test_get_single():
    """
    GIVEN bucket with single element
    WHEN get is called with the key of the element
    THEN the value of the element is returned.
    """
    test_bucket = bucket.Bucket()
    key = "key 1"
    value = "value 1"
    test_bucket.insert(key, value)

    returned_value = test_bucket.get(key)

    assert returned_value == value


def test_get_single_different():
    """
    GIVEN bucket with single element and a different key
    WHEN get is called with the key
    THEN KeyError is raised.
    """
    test_bucket = bucket.Bucket()
    test_bucket.insert("key 1", "value 1")

    with pytest.raises(KeyError):
        test_bucket.get("key 2")


def test_get_multiple():
    """
    GIVEN bucket with multiple elements
    WHEN get is called with the key for each element
    THEN the value of the element is returned.
    """
    test_bucket = bucket.Bucket()
    for idx in range(2):
        element_number = idx + 1
        test_bucket.insert(f"key {element_number}", f"value {element_number}")

    for idx in range(2):
        element_number = idx + 1
        assert test_bucket.get(f"key {element_number}") == f"value {element_number}"


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
