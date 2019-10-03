# Hash Map

Arrays are efficient in terms of memory for storing data. Often in programming there is a need to sore key-value pairs which will then be retrieved later based on the key. If they were stored in an array, it would take O(n) time complexity to retrieve the value. A hash map is similar to an array, but it can retrieve a value associated with a key in O(1) time (with some caveats). This is done by placing elements in the array at a particular index related to the key that will be used to retrieve the value later. Typically a hash function is used to map the key to a number and then the modulus operator is used to ensure that number is within the bounds of the array. This opens up the possibility of clashes, which is why each element of the array is a collection (bucket) as well. This can be implemented as a linked list or array.

The hash map is most efficient when the hash algorithm evenly distributes key value pairs over the array. This is because, to retrieve a value based on a key, most of the work should be done by the hashing algorithm and not in the iterating over the particular bucket to see if it has the value. A hash algorithm that maps each key to the same bucket would mean the hash map has not achieved its purpose.

Assuming the hash algorithm does its job properly, the next pitfall is the number of elements versus the number of buckets in the hash map. If the number of buckets is constrained to 1, not matter how good the hash algorithm is, the hash map will not be able to serve its purpose. Most of the time of retrieving a value based on the key will be spent iterating over the bucket. Conversely, maintaining an empty bucket is expensive in terms of wasted memory. A common rule of thumb is to target a load factor of 0.75. Depending on the nature of the data, even the best hashing algorithm may place a disproportionate number of elements into a bucket. This is why a load factor of 0.75 is chosen to add some padding to reduce the chance of having large buckets.

Ensuring that the O(1) time and complexity for key operations are maintained depends on the choice of hash algorithm and load factor. A bad hash algorithm or inappropriate load factor can jeopardize the time complexity to O(n).

## Operations

### Add or update key value pair

This operation uses the hash algorithm to calculate the index where the data should be stored and adds to or updates the data in that bucket. This has O(1) time complexity.

### Retrieve value for a key

This operation uses the hash algorithm to find the bucket and iterates over the bucket to retrieve the value for the key. It has O(1) time complexity.

### Check if key exists

This operation uses the hash algorithm to find the bucket and iterates over the bucket to see if the key exists. It has O(1) time complexity.

### Remove key

This operation uses the hash algorithm to find the bucket and then iterates over the bucket to find the key and remove it. It has O(1) time complexity.

### Size of hash map

To ensure O(1) time complexity, this is maintained separately and returned on demand. The number of buckets is not a reliable indicator because of the variable number of elements in each bucket.

### Iterate over elements

This operation iterates over each bucket and value in the bucket. It has O(n) time complexity.

### Clear

This operation resets the size of the hash map and clears out each bucket. It has O(n) time complexity.

### Clone

Copy all values in the hash map to a new hash map. May or may not clone key value pairs. It has O(n) time complexity.

## Observations

The hash map heavily relies on the bucket data structure to implement functionality. The value the hash map adds is the mapping from a key to a particular bucket. There is a case for changing the function that calculates the index to be a decorator, although the difference is minor. There will still be a line using that decorator instead of a function call within each function implementing an feature. It would also change the arguments which makes it harder to understand the implementation.

The change of the number of buckets is a complex operation. However, in steady state, it is not expected to occur often as the number of elements in the hash map is not expected to change as frequently. Allowing the setting of an initial capacity can also help, although if an element is removed before the hash map is sufficiently full the capacity of the hash map will be reduced. Also, it seems that a copy of all elements must be taken on a change in the number of buckets because it is hard to know where a particular element will be stored in the new capacity. However the memory complexity is still O(n). If the 0.75 threshold is used as the trigger for both up and downsizing, an unlucky steady state might required frequent copying of elements as the load factor fluctuates slightly. A better approach might be defensive up and downsizing where the load factor must vary from the ideal load factor by a safety margin before an expensive resizing operation is triggered.
