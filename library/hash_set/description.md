# Hash Set

A hash set is similar to an array with a few key differences. Checking whether an element is an array is an expensive operation with O(n) time complexity. Checking whether an element is in a hash set is a cheap operation at O(1). Additionally, a hash set makes it easy to maintain a collection of unique elements having a unique insert time complexity of O(1) which is O(n) for an array. The drawback is that the order of elements in a hash set is not guaranteed and accessing an element at a certain index is not possible, both of which is the case for an array.

Hash sets are typically implemented using a HashMap by maintaining elements as keys of the hash map and setting the values to some constant.

## Operations

### Add element

Adding an element is O(1) time complexity. Only one unique copy of an element can be in a hash set at once.

### Remove an element

Removing an element has O(1) time complexity. Elements can only be removed by value, not by index.

### Check whether an element exists

Checking whether an element exists has O(1) time complexity.

### Retrieve Size

Retrieving the size of the hash map has O(1) time complexity. The size is tracked by the underlying data structure.

### Iterate over elements

This operation iterates over each bucket and value in the bucket. It has O(n) time complexity. No guarantees as to the order of elements is given.

### Clear

This operation resets clears out all elements from the set. It has O(n) time complexity. It might be faster to let the hash set be garbage collected and to construct a new set.

### Clone

Copy all elements in the hash set to a new hash set. May or may not clone individual elements. It has O(n) time complexity.
