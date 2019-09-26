# Stack

A stack is a data structure implementing a last in first out principle. The most recent element pushed into the stack is the first that is popped out of the stack. Under the hood it can be implemented using, for example, an array or a linked list. Depending on the programming language, an array might not be a good choice as deletion and insertion cn be an expensive operation as memory might have to be expanded or contracted and elements copied. In Python, as long as new elements are added to the end of the list, the complexity is reasonable as extra memory is allocated to allow the list to expand and contract to a degree without having to copy elements to a new array. However, a linked list may consume less memory and generalizes to a good implementation for other programming languages.

## Operations

### Push

Adds a new element to the stack. This has O(1) time and memory complexity.

### Pop

Remove the last added element from the stack and return it. This has O(1) time and memory complexity.

### Peek

Return the element at the top of the stack without popping it from the stack. This has O(1) time and memory complexity. This cn be implemented using the pop and push command. However, this may make changes to where the element is stored and, therefore, the data structure which might be unexpected for an operation that is expected to be read only.

### Is Empty

Return whether the stack is empty. This has o(1) time and memory complexity.
