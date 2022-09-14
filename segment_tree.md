## Segment tree

### What is it
Segment tree is a data structure that stores information about array intervals as a tree.
This allows efficient range queries and updates over an array.

It generally has two operations:
- `query(start, end)`: returns the value of interest from the given range, e.g. range min/max, range sum
- update
    - `update(i, val)`: updates the value of the `i`-th item in the original array to `val`
    - `update(start, end, val)`: increase the value of items in range `[start, end]` in the original array by val


```
        0  1  2  3  4  5  6  7
nums = [5, 2, 6, 3, 7, 4, 1, 1]


range sum tree

node range                                    [0:7]
node val                                       29

node range                [0:3]                               [4:7]
node val                    16                                  13

node range         [0:1]            [2:3]              [4:5]            [6:7]
node val             7                9                  11               2

node range   [0:0]    [1:1]     [2:2]   [3:3]     [4:4]    [5:5]    [6:6]   [7:7]      
node val       5        2         6       3         7        4        1       1


range_sum_tree = {1: 29, 2: 16, 3: 13, 4: 7, 5: 9, 6: 11, 7: 2, 8: 5, 9: 2, 10: 6, 11: 3, 12: 7, 13: 4, 14: 1, 15: 1}
```

### Construction
describe in words 
- A segment tree for a set of n intervals uses O(n log n) storage and can be built in O(n log n) time. 
+ code in ./src

### Query and Update 
range sum query
describe in words and sketch
+ code in ./src

### Lazy propagation
range sum query
describe in words and sketch
+ code in ./src

compare the runtime of updates w/ and w/ lazy propagation


### More advanced topics 
Higher dimensional segment tree

### Application 

1. Supports custom value calculation 
2. Fast range queries  
    - Segment trees support searching for all the intervals that contain a query point in time O(log n + k), k being the number of retrieved intervals or segments.
