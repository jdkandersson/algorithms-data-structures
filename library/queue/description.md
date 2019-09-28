# Queue

A queue implements the first in first out principle. This means, the element that has been in the queue the longest is returned first. The queue can be implemented using a variety of underlying data structures such as an array or a linked list. An array implemented is not expected to be efficient as elements have to be added and removed from opposite ends of the array meaning that one of the two methods has O(n) time complexity. A linked list is expected to be a more efficient data structure, although both a head and tail reference should be retained.

An even ore efficient data structure is making special use of an array. A front and back index and the number of elements in the queue and the maximum length of the queue is maintained. When a new element is enqueued the back index is incremented and the element is inserted at that index. When an element is dequeued the element at the front index is returned and the front index is incremented. Before operations are performed a check for empty or full is done based on the relationship between th number of elements in the queue and the maximum length of the queue. The front is initialized to 0 and the back index is initialized to -1.

## Operations

### Enqueue

Add an element to the back of the queue. This has O(1) time complexity.

### Dequeue

Remove an element from the front of the queue. This has O(1) time complexity.

### Get Front

Return the element from the front of the queue without dequeueing it. This has O(1) time complexity.

### Is Empty

Check whether the queue is empty. This has O(1) time complexity.

### Is Clear

Reset the queue to be empty. This has O(1) time complexity.

## Observations

Initially it might seem possible not to have to maintain the number of elements in the queue to know whether the queue is full or empty and use the front and back indexes instead. However, the front index being one more than the back index can indicate that the queue is either full or empty. For example, given the initial state of one spot being left in the queue:

```
|x|x| |
 f b
```

When an additional element is added the state is changed to:

```
|x|x|x|
 f   b
```

Which means that the front index is one past the back index. Next, consider the following initial state with a single element in the queue:

```
| | |x|
     f
     b
```

When an item is dequeued the state changes to:

```
| | | |
 f   b
```

Which has the same front and back indexes, except the queue is now empty.

## Applications

Queues are used quite frequently for batch processing and as an buffer between asynchronous workers or handling requests from clients. It is also possible to implement priority queues where certain values should be processed before others. This can be implemented using many ways, a common way is to maintain a queue for each priority and dequeue from the highest priority queue first.
