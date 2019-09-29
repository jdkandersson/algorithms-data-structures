"""Tests for HashMap."""
# pylint: disable=protected-access

from unittest import mock

import pytest

from library import hash_map


@pytest.mark.parametrize(
    "key, capacity, expected_index",
    [
        (1, 16, 11),
        (2, 16, 5),
        (4, 16, 10),
        (8, 16, 3),
        (16, 16, 9),
        (32, 16, 11),
        (64, 16, 11),
        (1, 32, 11),
        (0.1, 16, 0),
        (0.2, 16, 13),
        (0.4, 16, 1),
        (0.8, 16, 4),
        (1.6, 16, 13),
        (3.2, 16, 1),
        (6.4, 16, 6),
        (0.1, 32, 16),
        ("key 1", 16, 9),
        ("key 2", 16, 3),
        ("key 4", 16, 9),
        ("key 8", 16, 7),
        ("key 16", 16, 0),
        ("key 32", 16, 14),
        ("key 64", 16, 6),
        ("key 1", 32, 9),
    ],
    ids=[
        "int-1-16",
        "int-2-16",
        "int-4-16",
        "int-8-16",
        "int-16-16",
        "int-32-16",
        "int-64-16",
        "int-1-32",
        "float-0.1-16",
        "float-0.2-16",
        "float-0.4-16",
        "float-0.8-16",
        "float-1.6-16",
        "float-3.2-16",
        "float-6.4-16",
        "float-0.1-32",
        "str-key 1-16",
        "str-key 2-16",
        "str-key 4-16",
        "str-key 8-16",
        "str-key 16-16",
        "str-key 32-16",
        "str-key 64-16",
        "str-key 1-32",
    ],
)
def test_calculate_index(key, capacity, expected_index):
    """
    GIVEN key, capacity of HashMap and expected index
    WHEN HashMap is constructed with the capacity and _calculate_index is called with
        the key
    THEN the expected index is returned.
    """
    test_hash_map = hash_map.HashMap(capacity)

    index = test_hash_map._calculate_index(key)

    assert index == expected_index


@pytest.fixture
def mocked_buckets_hash_map():
    """HashMap with mocked buckets and _calculate_index."""
    capacity = 16
    test_hash_map = hash_map.HashMap(capacity)
    for idx in range(capacity):
        test_hash_map._buckets[idx] = mock.MagicMock()
    test_hash_map._calculate_index = mock.MagicMock()
    return test_hash_map


def test_set_calculate_index(
    mocked_buckets_hash_map,
):  # pylint: disable=redefined-outer-name
    """
    GIVEN hash map with mocked _calculate_index and key
    WHEN set_ is called with the key
    THEN _calculate_index is called with the key.
    """
    mocked_buckets_hash_map._calculate_index.return_value = 0
    key = "key 1"

    mocked_buckets_hash_map.set_(key, "value 1")

    mocked_buckets_hash_map._calculate_index.assert_called_once_with(key)


def test_set_insert(mocked_buckets_hash_map):  # pylint: disable=redefined-outer-name
    """
    GIVEN hash map with mocked _calculate_index, mocked buckets and key and value
    WHEN set_ is called with the key and value
    THEN the bucket with the index returned by _calculate_index is called with the key
        and value.
    """
    mocked_buckets_hash_map._calculate_index.return_value = 0
    key = "key 1"
    value = "value 1"

    mocked_buckets_hash_map.set_(key, value)

    mocked_buckets_hash_map._buckets[0].insert.assert_called_once_with(key, value)
