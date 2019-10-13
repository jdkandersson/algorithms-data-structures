# Heap

A heap is a linear data structure that allows for an efficient implementation of retrieving the largest/smallest value from an array of values. It can be used for things like priority queues where insertion and deletion has O(log(n)) time complexity. It is also an efficient data structure to sort an array allowing for in-place sorting in O(n log(n)) time complexity and O(n) memory complexity.

A heap is often implemented as an array in a certain order. The order is that any element at index n is larger (or smaller) than the element at both index 2n+1 and 2n+2 given indexes are zero based. The element at index n is considered the root element and the elements at indexes 2n+1 and 2n+2 are considered it's children. If the child element indexes are out of bounds it means that the root element is a leaf node. This doesn't mean that the array is sorted since no relationship between the children is asserted.

## Operations

### Sift Down

This operation has O(1) time complexity. It accepts an index n, which is taken as the root of a heap, and assumes that the child elements are themselves valid heaps. After the operation is complete, the heap rooted at n is also a valid heap. This operation is implemented by swapping the left and right child with the root element, if required.

### Sift Up

This operation has O(log(n)) time complexity. It takes a start and end index. It starts at the end and proceeds up the heap swapping children with parents as required.

### Heapify

This operation turns an array into a heap. It either uses sift down or sift up to complete the transformation. If heapify is done using sift down, it has O(n) time complexity. If it is done using sift up, it has O(log(n)) time complexity. The reason is the difference in time complexity of the sift down and sift up algorithms.

### Insert

Insert a new element into the heap. This is usually done by adding the element to an empty slot at the end of the heap and then use the sift up  operation to ensure the heap property.

### Extract Max (or Min)

Remove the maximum (or minimum) element from the heap. This is usually done by swapping the root with the last element, then sifting that element down repeatedly.

### Size

The number of elements in the heap. Has O(1) time complexity.

### Empty

Return whether the heap is empty. Has O(1) time complexity.
