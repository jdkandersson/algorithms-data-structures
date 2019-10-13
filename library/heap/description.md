# Heap

A heap is a linear data structure that allows for an efficient implementation of retrieving the largest/smallest value from an array of values. It can be used for things like priority queues where insertion and deletion has O(log(n)) time complexity. It is also an efficient data structure to sort an array allowing for in-place sorting in O(n log(n)) time complexity and O(n) memory complexity.

A heap is often implemented as an array in a certain order. The order is that any element at index n is larger (or smaller) than the element at both index 2n+1 and 2n+2 given indexes are zero based. The element at index n is considered the root element and the elements at indexes 2n+1 and 2n+2 are considered it's children. If the child element indexes are out of bounds it means that the root element is a leaf node. This doesn't mean that the array is sorted since no relationship between the children is asserted.

## Operations

### Sift Down

This operation has O(log(n)) time complexity. It assumes that the heaps rooted at the children are valid heaps. It accepts a start and end index. It starts at the start index and swaps the parent and children to satisfy the heap property, if required. If a swap is required, then the sift down operation proceeds on the swapped element as the start index.

### Sift Up

This operation has O(log(n)) time complexity. It takes a start and end index. It starts at the end and checks if the child needs to be swapped with the parent. If it does, the algorithm proceeds up the tree until the root start index is reached.

### Heapify

This operation turns an array into a heap. It either uses sift down or sift up to complete the transformation. If heapify is done using sift down, it has O(n) time complexity. If it is done using sift up, it has O(log(n)) time complexity. The reason is somewhat complex. The sift down operation, when used in the heapify algorithm, calls sift down mostly on sub heaps that have a depth of 1. The sift up version mostly operates on the sub heaps with a comparable depth as the full heap. Therefore, most of the time the sift down version has O(1) time complexity and the sift up version has O(log(n)) time complexity.

### Insert

Insert a new element into the heap. This is usually done by adding the element to an empty slot at the end of the heap and then use the sift up  operation to ensure the heap property.

### Extract Max (or Min)

Remove the maximum (or minimum) element from the heap. This is usually done by swapping the root with the last element, then sifting that element down repeatedly.

### Size

The number of elements in the heap. Has O(1) time complexity.

### Empty

Return whether the heap is empty. Has O(1) time complexity.
