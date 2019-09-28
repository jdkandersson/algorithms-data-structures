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

### Is Empty

This operation uses the size to determine whether the hash map is empty. It has O(1) time complexity.
