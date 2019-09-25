# Array

Arrays store data in the most compact way possible. The advantage is potential memory efficiency, the disadvantage is that arrays are always setup with a limited capacity. In python, the language chooses some defaults and, once the array is full, to be able to add a new element to the array the array has to be copied first. This is taken care of by the language.

## Operations

### Insert

Adding a new element to an array,on average, is O(1). However, the worst case is O(n) because the array might be out of memory and has to be re-allocated.

### Access

Index access to array elements is O(1). However, value access is O(n) because the value has to be found in the array first.

### Delete

Removing an element from an array is O(n) because elements after the deleted element have to be shifted to fill the empty space.

### Search

A number of searching algorithms are possible on arrays because the length of the array is known. The base case for search algorithms is O(log(n)). The worst time complexity algorithms are O(n).

### Copy

Copying an array can be done a number of ways. Re-assigning an array to a new variable does not copy the array. The copy library can be used to copy the array. If the array contains objects a deep copy might be considered, otherwise each element in the copied array still points to the same underlying object.

## Multi-Dimensional Arrays

Multi-dimensional arrays are possible in Python as arrays in Python can contain anything, including another list. It is easy to get lost in multi-dimensional lists, however, unless done carefully as there is no easy way to control the size of the sub lists so that they are all equal. There are libraries available to help with multi-dimensional arrays.
