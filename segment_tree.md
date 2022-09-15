## Segment tree

### What is it
Segment tree is a data structure that stores information about array intervals as a tree.
This allows efficient range queries and updates over an array.

It generally has two operations:
- `query(start, end)`: returns the value of interest from the given range, e.g. range min, max, sum
- `update(start, end, val)`: increase the value of all items in range `[start, end]` in the original array by `val`


### Construction
Segment trees are usually represented as a list (or dictionary for faster range value retrieval).

For example, given `nums = [5, 2, 6, 3, 7, 4, 1, 1]`, 
it's range sum segment tree looks like below, which is the same as the dictionary:

`val = {1: 29, 2: 16, 3: 13, 4: 7, 5: 9, 6: 11, 7: 2, 8: 5, 9: 2, 10: 6, 11: 3, 12: 7, 13: 4, 14: 1, 15: 1}` 

```
node range                                    [0:7]
node val                                       29
                                              idx=1

node range                 [0:3]                               [4:7]
node val                    16                                  13
                          idx=2                                idx=3

node range         [0:1]            [2:3]              [4:5]            [6:7]
node val             7                9                  11               2
                   idx=4            idx=5              idx=6            idx=7

node range   [0:0]    [1:1]     [2:2]    [3:3]     [4:4]    [5:5]    [6:6]    [7:7]      
node val       5        2         6        3         7        4        1        1
            idx=8    idx=9     idx=10    idx=11   idx=12    idx=13   idx=14   idx=15
```

This is built with two steps:
1. fill the dictionary with the leave nodes' values using their corresponding indices.
2. fill the values from the second deepest level to the top by using the following relationship: `node i is the parent of node i//2 and node i//2 + 1`. 

### Query and Update 
**Query**

Continue from the range sum segment tree above, querying here means returning the sum of all items in the given range `[start, end]`. 

This can be done recursively from the root node. In each step, check for overlap between the node's range and the given range and decide on the subtree to continue the recursion. There are four cases:
1. given range is entirely in the left subtree of the current node
    - e.g. `given range = [0: 3], current node idx = 1`
2. given range is entirely in the right subtree of the current node
    - e.g. `given range = [4: 7], current node idx = 1`
3. given range spans across two subtrees of the current node
    - e.g. `given range = [1: 2], current node idx = 2`
4. given range is identical to current node's range
    - return the current node's value as the final result

```
node range                                    [0:7]
node val                                       29
                                              idx=1

node range                 [0:3]                               [4:7]
node val                    16                                  13
                          idx=2                                idx=3

node range         [0:1]            [2:3]              [4:5]            [6:7]
node val             7                9                  11               2
                   idx=4            idx=5              idx=6            idx=7

node range   [0:0]    [1:1]     [2:2]    [3:3]     [4:4]    [5:5]    [6:6]    [7:7]      
node val       5        2         6        3         7        4        1        1
            idx=8    idx=9     idx=10    idx=11   idx=12    idx=13   idx=14   idx=15
```

**Update**
Update shares the same logic as Query to traverse from the root node to the each of the leaf node covered in the given range `[start, end]`.
When the leaf node is reached, its value in `val` is updated accordingly, which is then used to modify the value of all its parent nodes when the return trip starts.

### Lazy propagation
One drawback of the Update method above is that it's quit slow for range updates, since every single leaf node covered by the range has to be reached before an actual update can happen. 

Lazy propagation solves this issue. Instead of going all the way down to every leaf node, it saves the value to be applied on all descendent nodes in the parent node, and will not carry out the update until the descendent nodes are actually accessed (e.g. when they are queried).

In this way, only the nodes from the root node to that parent node are actually updated.

e.g. `update(2, 3, delta=1)`

'''
node range                                    [0:7]
node val                                       31 (prev=29)
                                              idx=1

node range                 [0:3]                               [4:7]
node val                    18 (prev=16)                        13
                          idx=2                                idx=3

node range         [0:1]            [2:3]              [4:5]            [6:7]
node val             7                11 (prev=9)       11                2
                   idx=4            idx=5              idx=6            idx=7
                                    lazy=2

node range   [0:0]    [1:1]     [2:2]    [3:3]     [4:4]    [5:5]    [6:6]    [7:7]      
node val       5        2         6        3         7        4        1        1
            idx=8    idx=9     idx=10    idx=11   idx=12    idx=13   idx=14   idx=15
'''


### More advanced topics 
Higher dimensional segment tree

### Application 
1. Supports custom value calculation 
2. Fast range queries  
