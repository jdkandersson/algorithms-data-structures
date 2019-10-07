# Binary Tree

A binary tree is a basic non-linear data structure. Arrays, maps, sets and so on usually have a next logical element. A Binary tree, and trees in general, do not as one node in the tree can point to multiple other nodes.

There are some commonly used terms for trees that are good to know what they mean. The root is the entry point of a tree. The root is a node which has a value and may point to any number of other nodes. In a binary tree a node can point to at most two other nodes. The way a node points to other nodes is via an edge. The relationship between nodes is usually described in terms of parents, child and sibling. A child node is a node that is pointed to by another node. A parent node is the node that points to a node. A sibling node is a node that shares the same parent node. There are also more indirect relationships such as descendants (all the nodes pointed to by a node, including the child nodes of child nodes and so on) and ancestors (a node parents and their parents and so on). A leaf node does not have any children. A branch node has at least 1 child. There are also global terms. The depth of a node is the number of parent nodes before the root is reached. A path is the shortest route from one node to another. The height is the number of edges on the longest path in the tree. Level is the number of nodes on the longest path in the tree. The level of a node is the number of nodes on the shortest path to the root. The Width at a level is the number of nodes that share the level.

Trees, and binary trees, are typically not used as a general purpose data structure, such as arrays, maps and sets. Typically they are used for certain algorithms. The tree that will be considered here is the binary search tree. A binary search tree satisfies a certain condition that makes it efficient to search for a value in the tree. Specifically, the left sub tree of a node must contain values less than the node and the right sub tree must contain values that are larger than the node's value. Any modification to the tree must maintain this condition of the tree. There are also some structure considerations. For example, if the root node has the largest value in the tree, searching for an element in the tree is not as efficient as the data structure promises if the distribution of nodes is more even. A binary search tree is particularly useful for maintaining the order of elements.

## Operations

### Search

Finding an element in the tree. This operation is O(log(n)), assuming the tree is reasonably balanced. This is because at each level, at least half the nodes can be eliminated from the set of possible values.

### Insert

This operation is not O(1) because the condition of the binary search tree must be maintained. Essentially, the correct place for the node must first be found and then the insert operation at that place is O(1). Since finding a value in the tree is O(log(n)), the insert operation is also O(log(n)). The algorithm boils down to traversing the tree to find an empty child slot.

### Delete

This operation is not O(1) because the node with the value has to be found first. This operation is also more complex because there can be a range of conditions that the node with the value may have that requires different steps to be taken to remove the node. If the node is a leaf, it can simply be deleted. If the node has a single child, the node can be deleted and that child takes the place of the node. If the node has two children, then the smallest value in the right node is copied into the node. The smallest value in the right node is guaranteed to be a leaf node. It is also guaranteed to be larger than the values in the left sub tree and smaller than the nodes in the right subtree. It is also possible to use the largest value in the left subtree.

### Traverse

Due to the nature of the tree there are multiple ways of traversing the tree. For a binary search tree a logical traversal is the in order traversal which traverses the tree as the left child node first, then the value and then the right node. This means that the values are returned sorted according to their value. There is also pre-order traversal where the value is traversed before the left and right nodes. There is also post order traversal where the value is traversed after the left and right child. In this case only in order traversal is implemented.
