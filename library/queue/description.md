# Queue

A queue implements the first in first out principle. This means, the element that has been in the queue the longest is returned first. The queue can be implemented using a variety of underlying data structures such as an array or a linked list. An array implemented is not expected to be efficient as elements have to be added and removed from opposite ends of the array meaning that one of the two methods has O(n) time complexity. A linked list is expected to be a more efficient data structure, although both a head and tail reference should be retained.

## Operations

### Enqueue

Add an element to the back of the queue. This has O(1) time and memory complexity.

### Dequeue

Remove an element from the front of the queue. This has O(1) time and memory complexity.

### Peek

Return the element from the front of the queue without dequeueing it. This has O(1) time and memory complexity.

### Is Empty

Check whether the queue is empty. This has O(1) time and memory complexity.

## Applications

Queues are used quite frequently for batch processing and as an buffer between asynchronous workers or handling requests from clients.
