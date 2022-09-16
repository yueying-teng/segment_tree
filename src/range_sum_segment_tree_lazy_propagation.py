import collections


class RangeSumSegmentTree:  
    def __init__(self, nums):
        self.lazy = collections.defaultdict(int)

        def build(nums):
            val = collections.defaultdict(int)
            nums_len = len(nums)
            # add leaf nodes in val using items in nums
            for i, num in enumerate(nums):
                val[i + nums_len] = num
            # create parent nodes' values by adding child nodes' values
            for i in range(nums_len - 1, 0, -1):
                val[i] = val[2 * i] + val[2 * i + 1]

            return val

        self.val = build(nums)
        
    
    def query(self, start, end, l, r, index=1):
        """
        node information: l, r, index
        interval being queried for range sum: [start, end]
        """

        if end < l or r < start:
            return 0

        # current node has previous updates, stored in lazy, that have not been applied 
        if self.lazy[index] != 0:     
            self.val[index] += (r - l + 1) * self.lazy[index]  # apply previous updates
            # postpone its child nodes' update
            if l != r:
                self.lazy[2 * index] += self.lazy[index]     
                self.lazy[2 * index + 1] += self.lazy[index]
            
            self.lazy[index] = 0

        if start <= l <= r <= end:
            return self.val[index]
            
        m = (l + r) // 2

        if end <= m: # target range completely in the left subtree
            return self.query(start, end, l, m, 2 * index)
        elif start >= m + 1:
            return self.query(start, end, m + 1, r, 2 * index + 1)
        else:
            return self.query(start, m, l, m, 2 * index) + \
                   self.query(m + 1, end, m + 1, r, 2 * index + 1)
        
    def update(self, start, end, l, r, index=1, delta=1):
        """
        node information: l, r, index
        interval to be updated: [start, end]
        delta: changes to be applied on all items in the range above  
        """
         
        # current node has previous updates, stored in lazy, that have not been applied 
        if self.lazy[index] != 0:     
            self.val[index] += (r - l + 1) * self.lazy[index]  # apply previous updates
            # postpone its child nodes' update
            if l != r:
                self.lazy[2 * index] += self.lazy[index]     
                self.lazy[2 * index + 1] += self.lazy[index]
            
            self.lazy[index] = 0
        
        if end < l or r < start:
            return 

        # full overlap, update current node's and child nodes' values
        if start <= l <= r <= end:
            self.val[index] += (r - l + 1) * delta
            if l != r:
                self.lazy[2 * index] += delta 
                self.lazy[2 * index + 1] += delta 
            
            return 

        m = (l + r) // 2

        self.update(start, end, l, m, 2 * index, delta)
        self.update(start, end, m + 1, r, 2 * index + 1, delta)

        self.val[index] = self.val[2 * index] + self.val[2 * index + 1]


nums = [5, 2, 6, 3, 7, 4, 1, 1]
tree = RangeSumSegmentTree(nums)
print({k: v for k, v in sorted(tree.val.items(), key=lambda x: x[0])})

l, r = 0, len(nums) - 1 # root node's range

queries = [[2, 3], [0, 5], [4, 4]]
for start, end in queries:
    print(start, end)
    print(tree.query(start, end, l=l, r=r))

updates = [[2, 3], [3, 5], [0, 7], [4, 4]]
for start, end in updates:
    print(start, end)
    tree.update(start, end, l=l, r=r)
    print('lazy', tree.lazy)
    print('tree', {k: v for k, v in sorted(tree.val.items(), key=lambda x: x[0])})
    
    print('query range', start, start)
    print(tree.query(start, start, l=l, r=r))
    print('tree', {k: v for k, v in sorted(tree.val.items(), key=lambda x: x[0])})



