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
		
        if start == l and end == r:
            return self.val[index] 
            
        m = (l + r) // 2

        if end <= m: # target range completely in the left subtree
            return self.lazy[index] + self.query(start, end, l, m, 2 * index)
        elif start >= m + 1:
            return self.lazy[index] + self.query(start, end, m + 1, r, 2 * index + 1)
        else:
            return self.lazy[index] + self.query(start, m, l, m, 2 * index) + \
                   self.query(m + 1, end, m + 1, r, 2 * index + 1)
        
    def update(self, start, end, l, r, index=1, delta=1):
        """
		node information: l, r, index
        interval to be updated: [start, end]
        delta: changes to be applied on all items in the range above  
		"""
		
        if start == l and end == r:
            self.val[index] += delta * (r - l + 1) # update the current node val 
            # all child nodes of the current range [l, r] have to be updated, 
            # but there is no need to do it now. store the value to be applied on them for later
            self.lazy[index] += delta 
            return

        m = (l + r) // 2

        if end <= m: # target range completely in the left subtree
            self.update(start, end, l, m, 2 * index, delta)
        elif start >= m + 1:
            self.update(start, end, m + 1, r, 2 * index + 1, delta)
        else: 
            self.update(start, m, l, m, 2 * index, delta)
            self.update(m + 1, end, m + 1, r, 2 * index + 1, delta)

        self.val[index] = self.lazy[index] + self.val[2 * index] + self.val[2 * index + 1]
 
        return



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
    tree.update(start, end, l=l, r=r)
    print('lazy', tree.lazy)
    print('tree', {k: v for k, v in sorted(tree.val.items(), key=lambda x: x[0])})
    
    print('query range', start, start)
    print(tree.query(start, start, l=l, r=r))
    print('query range', start, end)
    print(tree.query(start, end, l=l, r=r))

