import collections


class RangeSumSegmentTree:      
    def __init__(self, nums):
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
        
        # search range does not overlap with the node's range
        if end < l or r < start:
            return 0

        # current node's range is inside the given range 
        if start <= l <= r <= end:
            return self.val[index] 
        else:
            m = (l + r) // 2

            return self.query(start, end, l, m, 2 * index) + \
                   self.query(start, end, m + 1, r, 2 * index + 1)
            
    def update(self, start, end, l, r, index=1, delta=1):
        """
        node information: l, r, index
        interval to be updated: [start, end]
        delta: changes to be applied on all items in the range above  
        """

        # search range does not overlap with the node's range
        if end < l or r < start:
            return 

        # current node's range is inside the given range 
        if start <= l <= r <= end:
            self.val[index] += delta # update current node's val
            return 
        else:
            # recurse deeper to find the appropriate node
            m = (l + r) // 2

            self.update(start, end, l, m, 2 * index, delta)
            self.update(start, end, m + 1, r, 2 * index + 1, delta)
        
            self.val[index] = self.val[2 * index] + self.val[2 * index + 1]


nums = [5, 2, 6, 3, 7, 4, 1, 1]
tree = RangeSumSegmentTree(nums)
print({k: v for k, v in sorted(tree.val.items(), key=lambda x: x[0])})

queries = [[2, 3], [0, 5], [4, 4]]
l, r = 0, len(nums) - 1 # root node's range
for start, end in queries:
    print(start, end)
    print(tree.query(start, end, l=l, r=r))

updates = [[2, 3], [3, 5], [0, 7], [4, 4]]
for start, end in updates:
    print(start, end)
    for i in range(start, end + 1):
        print(i, i)
        tree.update(i, i, l=l, r=r)
        print({k: v for k, v in sorted(tree.val.items(), key=lambda x: x[0])})
