# Linked List

A linked list is a collection of objects that reference each other. One object might reference the next and/or the previous object. Depending on the use case, there might be multiple paths that can be taken. For example, a particular path might implement a certain order of objects (for example, if a node represents a name, one path might be the order in which the objects were inserted and another might be an alphabetical order).

Compared to arrays, the amount of memory to be used does not have to be pre-defined. However, the amount of memory is larger as the reference to the next object in the chain has to be recorded. Arrays allow for O(1) access to elements at a particular index, which is not possible for linked lists by default.

## Operations

### Add Object to the List

If the object is to be inserted at the front of the list, the operation is O(1). To insert an object at the back of a list, by default this operation is O(n) because the whole list has to be traversed to the end. However, a tail reference could be maintained which changes the operation back to O(1). A tradeoff between the extra memory and frequency should be considered. A circularly doubly linked list would also allow O(1) insertion at the back.

### Traversing the List

To perform an operation on each element of the list is O(n).

### Finding an Object

By default, this is an O(n) operation because, in the worst case, every element has to be checked. It is possible to get lucky and find a match on the first go, or the object might not be found. If some special paths have been implemented finding an object might be faster on average. However, the worst case is always O(n) as the object might not exist.

### Add Object relative to another Object

To add an object relative to another object, the relative object has to be found first. Therefore, the commentary in Finding an Object applies. The insertion operation itself is O(1).

### Remove Object from List

To delete an object based on a key, it has to be found first. Therefore, the commentary in Finding an Object applies. The deletion operation is O(1).


### Clone the List

Due to the nature of the data structure, if the linked list is cloned without further consideration it is likely that only the head node is actually cloned and all the linked nodes are shared between the object. This clone method has O(1) complexity. More likely the whole list is expected to be cloned, which requires cloning each node to a new list. This has O(n) complexity.


### Observations

Some of the linked list functions are easier to implement recursively and others using a loop. All operations can be implemented using a loop, some are a little cleaner recursively, although potentially harder to understand for someone not as familiar with coding. In Python, recursive is a little dangerous due to the limit that is placed on the number of recursive calls meaning that, depending on the size of the linked list, recursively implemented operations may fail. For a production environment in Python it is likely better to avoid recursive implementations of linked list operations.

Sometimes it is easy to combine base cases for linked list operations with checks for empty lists, and other times it isn't possible. Usually if a new node is added or a node is deleted from the list special considerations for empty lists have to be taken. For traversing the liked list you can usually roll the empty list check into the base case/end of loop check.
