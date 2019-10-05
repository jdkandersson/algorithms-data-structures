"""Tests for HashMap."""
# pylint: disable=protected-access

from unittest import mock

import pytest

from library import hash_map


@pytest.mark.parametrize(
    "capacity, raises",
    [(0, True), (15, True), (16, False), (17, True), (32, False)],
    ids=["too small", "too small", "minimum size", "not multiple of 2", "larger size"],
)
def test_construct_capacity(capacity, raises):
    """
    GIVEN initial capacity and whether ValueError should be raised
    WHEN a HashMap is constructed with the capacity
    THEN ValueError is raised when expected raises is True.
    """
    if raises:
        with pytest.raises(ValueError):
            hash_map.HashMap(capacity)
    else:
        hash_map.HashMap(capacity)


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

    mocked_buckets_hash_map._calculate_index.assert_called_with(key)


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


def test_get_calculate_index(
    mocked_buckets_hash_map,
):  # pylint: disable=redefined-outer-name
    """
    GIVEN hash map with mocked _calculate_index and key
    WHEN get is called with the key
    THEN _calculate_index is called with the key.
    """
    mocked_buckets_hash_map._calculate_index.return_value = 0
    key = "key 1"

    mocked_buckets_hash_map.get(key)

    mocked_buckets_hash_map._calculate_index.assert_called_once_with(key)


def test_get_get_call(mocked_buckets_hash_map):  # pylint: disable=redefined-outer-name
    """
    GIVEN hash map with mocked _calculate_index, mocked buckets and key
    WHEN get is called with the key
    THEN the bucket with the index returned by _calculate_index is called with the key.
    """
    mocked_buckets_hash_map._calculate_index.return_value = 0
    key = "key 1"

    mocked_buckets_hash_map.get(key)

    mocked_buckets_hash_map._buckets[0].get.assert_called_once_with(key)


def test_get_get_return(
    mocked_buckets_hash_map,
):  # pylint: disable=redefined-outer-name
    """
    GIVEN hash map with mocked _calculate_index and mocked buckets
    WHEN get is called with the key
    THEN the get return value of the bucket with the index returned by
        _calculate_index is returned.
    """
    mocked_buckets_hash_map._calculate_index.return_value = 0
    key = "key 1"

    return_value = mocked_buckets_hash_map.get(key)

    assert return_value == mocked_buckets_hash_map._buckets[0].get.return_value


def test_set_get_missing():
    """
    GIVEN empty hash map
    WHEN get is called with a key
    THEN KeyError is raised.
    """
    test_hash_map = hash_map.HashMap()

    with pytest.raises(KeyError):
        test_hash_map.get("key 1")


def test_set_get():
    """
    GIVEN empty hash map and key and value
    WHEN set is called with the key and value and get is called with the key
    THEN the value is returned.
    """
    test_hash_map = hash_map.HashMap()
    key = "key 1"
    value = "value 1"

    test_hash_map.set_(key, value)
    return_value = test_hash_map.get(key)

    assert return_value == value


def test_exists_calculate_index(
    mocked_buckets_hash_map,
):  # pylint: disable=redefined-outer-name
    """
    GIVEN hash map with mocked _calculate_index and key
    WHEN exists is called with the key
    THEN _calculate_index is called with the key.
    """
    mocked_buckets_hash_map._calculate_index.return_value = 0
    key = "key 1"

    mocked_buckets_hash_map.exists(key)

    mocked_buckets_hash_map._calculate_index.assert_called_once_with(key)


def test_exists_exists_call(
    mocked_buckets_hash_map,
):  # pylint: disable=redefined-outer-name
    """
    GIVEN hash map with mocked _calculate_index, mocked buckets and key
    WHEN exists is called with the key
    THEN the bucket with the index returned by _calculate_index is called with the key.
    """
    mocked_buckets_hash_map._calculate_index.return_value = 0
    key = "key 1"

    mocked_buckets_hash_map.exists(key)

    mocked_buckets_hash_map._buckets[0].exists.assert_called_once_with(key)


def test_exists_exists_return(
    mocked_buckets_hash_map,
):  # pylint: disable=redefined-outer-name
    """
    GIVEN hash map with mocked _calculate_index and mocked buckets
    WHEN exists is called with the key
    THEN the exists return value of the bucket with the index returned by
        _calculate_index is returned.
    """
    mocked_buckets_hash_map._calculate_index.return_value = 0
    key = "key 1"

    return_value = mocked_buckets_hash_map.exists(key)

    assert return_value == mocked_buckets_hash_map._buckets[0].exists.return_value


def test_exists_missing():
    """
    GIVEN empty hash map
    WHEN exists is called with a key
    THEN False is returned.
    """
    test_hash_map = hash_map.HashMap()

    exists = test_hash_map.exists("key 1")

    assert exists is False


def test_exists_present():
    """
    GIVEN empty hash map and key and value
    WHEN set is called with the key and value and exists is called with the key
    THEN True is returned.
    """
    test_hash_map = hash_map.HashMap()
    key = "key 1"

    test_hash_map.set_(key, "value 1")
    exists = test_hash_map.exists(key)

    assert exists is True


def test_delete_calculate_index(
    mocked_buckets_hash_map,
):  # pylint: disable=redefined-outer-name
    """
    GIVEN hash map with mocked _calculate_index and key
    WHEN delete is called with the key
    THEN _calculate_index is called with the key.
    """
    mocked_buckets_hash_map._calculate_index.return_value = 0
    key = "key 1"

    mocked_buckets_hash_map.delete(key)

    mocked_buckets_hash_map._calculate_index.assert_called_once_with(key)


def test_delete_delete_call(
    mocked_buckets_hash_map,
):  # pylint: disable=redefined-outer-name
    """
    GIVEN hash map with mocked _calculate_index, mocked buckets and key
    WHEN delete is called with the key
    THEN the bucket with the index returned by _calculate_index is called with the key.
    """
    mocked_buckets_hash_map._calculate_index.return_value = 0
    key = "key 1"

    mocked_buckets_hash_map.delete(key)

    mocked_buckets_hash_map._buckets[0].delete.assert_called_once_with(key)


def test_delete_missing():
    """
    GIVEN empty hash map
    WHEN delete is called with a key
    THEN KeyError is raised.
    """
    test_hash_map = hash_map.HashMap()

    with pytest.raises(KeyError):
        test_hash_map.delete("key 1")


def test_delete_present():
    """
    GIVEN empty hash map and key and value
    WHEN set is called with the key and value and delete is called with the key
    THEN the key no longer exists in the hash map.
    """
    test_hash_map = hash_map.HashMap()
    key = "key 1"

    test_hash_map.set_(key, "value 1")
    test_hash_map.delete(key)

    assert test_hash_map.exists(key) is False


@pytest.mark.parametrize(
    "actions, expected_size",
    [
        ([], 0),
        ([("set_", ("key 1", "value 1"))], 1),
        ([("set_", ("key 1", "value 1")), ("set_", ("key 1", "value 2"))], 1),
        ([("set_", ("key 1", "value 1")), ("delete", ("key 1",))], 0),
        ([("set_", ("key 1", "value 1")), ("set_", ("key 2", "value 2"))], 2),
        (
            [
                ("set_", ("key 1", "value 1")),
                ("set_", ("key 2", "value 2")),
                ("delete", ("key 2",)),
            ],
            1,
        ),
    ],
    ids=[
        "empty,0",
        "set,1",
        "set-update,1",
        "set-delete,0",
        "set-set,2",
        "set-set-delete,1",
    ],
)
def test_size(actions, expected_size):
    """
    GIVEN empty hash map, actions to modify the hash map and expected size
    WHEN the actions are performed on the map
    THEN the map has the expected size.
    """
    test_hash_map = hash_map.HashMap()
    for operation, args in actions:
        getattr(test_hash_map, operation)(*args)

    assert test_hash_map.size == expected_size


def test_size_delete_raises():
    """
    GIVEN hash map with a single element
    WHEN delete is called with a different key than the element
    THEN size is not decremented.
    """
    test_hash_map = hash_map.HashMap()
    test_hash_map.set_("key 1", "value 1")

    with pytest.raises(KeyError):
        test_hash_map.delete("key 2")

    assert test_hash_map.size == 1


@pytest.mark.parametrize(
    "elements",
    [
        [],
        [("key 1", "value 1")],
        [("key 1", "value 1"), ("key 2", "value 2")],
        [
            ("key 1", "value 1"),
            ("key 2", "value 2"),
            ("key 4", "value 4"),
            ("key 8", "value 8"),
            ("key 16", "value 16"),
            ("key 32", "value 32"),
            ("key 64", "value 64"),
        ],
    ],
    ids=["empty", "single", "multiple", "many"],
)
def test_iterate(elements):
    """
    GIVEN empty hash map and elements to set
    WHEN elements are set and the map is iterated over
    THEN all elements are returned.
    """
    test_hash_map = hash_map.HashMap()
    for element in elements:
        test_hash_map.set_(*element)

    element_set = set(iter(test_hash_map))
    assert len(element_set) == len(elements)
    for element in elements:
        assert element in element_set


@pytest.mark.parametrize(
    "elements",
    [
        [],
        [("key 1", "value 1")],
        [("key 1", "value 1"), ("key 2", "value 2")],
        [
            ("key 1", "value 1"),
            ("key 2", "value 2"),
            ("key 4", "value 4"),
            ("key 8", "value 8"),
            ("key 16", "value 16"),
            ("key 32", "value 32"),
            ("key 64", "value 64"),
        ],
    ],
    ids=["empty", "single", "multiple", "many"],
)
def test_clear(elements):
    """
    GIVEN empty hash map and elements to set
    WHEN elements are set and clear is called
    THEN the map has zero size and iterating over it returns an empty list.
    """
    test_hash_map = hash_map.HashMap()
    for element in elements:
        test_hash_map.set_(*element)

    test_hash_map.clear()

    assert test_hash_map.size == 0
    assert list(iter(test_hash_map)) == []


@pytest.mark.parametrize(
    "elements",
    [
        [],
        [("key 1", "value 1")],
        [("key 1", "value 1"), ("key 2", "value 2")],
        [
            ("key 1", "value 1"),
            ("key 2", "value 2"),
            ("key 4", "value 4"),
            ("key 8", "value 8"),
            ("key 16", "value 16"),
            ("key 32", "value 32"),
            ("key 64", "value 64"),
        ],
    ],
    ids=["empty", "single", "multiple", "many"],
)
def test_construct_source(elements):
    """
    GIVEN list of key value tuples
    WHEN hash map is constructed with list as source
    THEN map contains each element in the list.
    """
    test_hash_map = hash_map.HashMap(source=elements)

    element_set = set(iter(test_hash_map))
    assert len(element_set) == len(elements)
    for element in elements:
        assert element in element_set


@pytest.mark.parametrize(
    "elements",
    [
        [],
        [("key 1", "value 1")],
        [("key 1", "value 1"), ("key 2", "value 2")],
        [
            ("key 1", "value 1"),
            ("key 2", "value 2"),
            ("key 4", "value 4"),
            ("key 8", "value 8"),
            ("key 16", "value 16"),
            ("key 32", "value 32"),
            ("key 64", "value 64"),
        ],
    ],
    ids=["empty", "single", "multiple", "many"],
)
def test_clone_elements(elements):
    """
    GIVEN empty hash map and elements to add to it
    WHEN hash map is constructed with list as source and cloned
    THEN cloned map contains each element in the list.
    """
    test_hash_map = hash_map.HashMap(source=elements)

    cloned_hash_map = test_hash_map.clone()

    element_set = set(iter(cloned_hash_map))
    assert len(element_set) == len(elements)
    for element in elements:
        assert element in element_set


def test_clone_not_same():
    """
    GIVEN empty hash map
    WHEN hash map is cloned
    THEN the cloned map is not the same object and contains different buckets.
    """
    test_hash_map = hash_map.HashMap()

    cloned_hash_map = test_hash_map.clone()

    assert id(cloned_hash_map) != id(test_hash_map)
    for original_bucket, cloned_bucket in zip(
        test_hash_map._buckets, cloned_hash_map._buckets
    ):
        assert id(original_bucket) != id(cloned_bucket)


def test_clone_capacity_copied():
    """
    GIVEN empty hash map and capacity of the hash map
    WHEN hash map is cloned
    THEN the cloned map has the same capacity.
    """
    capacity = 16
    test_hash_map = hash_map.HashMap(capacity)

    cloned_hash_map = test_hash_map.clone()

    assert cloned_hash_map.capacity == capacity


@pytest.mark.parametrize(
    "initial_capacity, initial_size, expected_capacity",
    [(16, 11, 16), (16, 12, 32), (32, 13, 32), (32, 24, 64)],
    ids=[
        "16,11,no increase",
        "16,12,buckets double",
        "32,13,no increase",
        "32,24,buckets double",
    ],
)
def test_resize_up(initial_capacity, initial_size, expected_capacity):
    """
    GIVEN empty hash map, initial capacity, initial number of elements and
        expected capacity
    WHEN the initial size plus one key and value is added to the map
    THEN the capacity is the expected final capacity and all added key value pairs are
        still in the map.
    """
    elements = [
        (f"key {idx + 1}", f"value {idx + 1}") for idx in range(initial_size + 1)
    ]

    test_hash_map = hash_map.HashMap(initial_capacity, elements)

    assert test_hash_map.capacity == expected_capacity
    assert len(test_hash_map._buckets) == expected_capacity
    assert test_hash_map.size == initial_size + 1
    element_set = set(iter(test_hash_map))
    assert len(element_set) == len(elements)
    for element in elements:
        assert element in element_set


@pytest.mark.parametrize(
    "initial_capacity, initial_size, expected_capacity",
    [(32, 13, 32), (32, 12, 16), (16, 11, 16), (16, 6, 16), (64, 24, 32)],
    ids=[
        "32,13,no decrease",
        "32,12,buckets halve",
        "16,11,no decrease",
        "16,6,no decrease",
        "64,24,buckets halve",
    ],
)
def test_resize_down(initial_capacity, initial_size, expected_capacity):
    """
    GIVEN empty hash map, initial capacity, initial number of elements and
        expected capacity
    WHEN the initial size is added to the map and then one is removed
    THEN the capacity is the expected final capacity and all key value pairs except the
        removed pair are still in the map.
    """
    elements = [(f"key {idx + 1}", f"value {idx + 1}") for idx in range(initial_size)]

    test_hash_map = hash_map.HashMap(initial_capacity, elements)
    test_hash_map.delete(elements[-1][0])

    assert test_hash_map.capacity == expected_capacity
    assert len(test_hash_map._buckets) == expected_capacity
    assert test_hash_map.size == initial_size - 1
    element_set = set(iter(test_hash_map))
    assert len(element_set) == len(elements[:-1])
    for element in elements[:-1]:
        assert element in element_set
