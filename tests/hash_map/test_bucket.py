"""Tests for the hash map bucket."""
# pylint: disable=protected-access

from unittest import mock

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
