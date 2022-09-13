## Segment tree

### What is it
Segment tree is a data structure that stores information about array intervals as a tree.
This allows efficient range queries and updates over an array.

It generally has two operations:
- `query(start, end)`: returns the value of interest from the given range, e.g. range min/max, range sum
- update
    - `update(i, val)`: updates the value of the `i`-th item in the original array to `val`
    - `update(start, end, val)`: increase the value of items in range `[start, end]` in the original array by val

<img src="./range_sum.png" height=300>

```

        0  1  2  3  4  5  6
nums = [5, 2, 6, 3, 7, 4, 1]

[range sum tree]

node range                                    [0:6]
node val                                       28

node range                [0:3]                               [4:6]
node val                    16                                  12

node range         [0:1]            [2:3]              [4:5]            [6:6]
node val             7                9                  11                1

node range   [0:0]    [1:1]     [2:2]   [3:3]     [4:4]    [5:5]      
node val       5        2         6       3         7        4              

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
