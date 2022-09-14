import sys 
import collections

class RangeSumSegmentTree:  
    # [LOWER, UPPER)
    LOWER = 0
    UPPER = sys.maxsize
    
    def __init__(self, nums):
        self.lazy = collections.defaultdict(int)

        def build(nums):
            val = collections.defaultdict(int)
            nums_len = len(nums)
            # add leaf nodes in val
            for i, num in enumerate(nums):
                val[i + nums_len] = num
            # create parent nodes' values by adding child nodes' values
            for i in range(nums_len - 1, 0, -1):
                val[i] = val[2 * i] + val[2 * i + 1]

            return val

        self.val = build(nums)
        
    
    def query(self, start, end, l=LOWER, r=UPPER, index=1):
        """
		node information: l, r, index
        query interval: start, end
		"""
		
        if start == l and end == r:
            return self.val[index] 
            
        m = (l + r) // 2

        if end <= m: # target range completely in the left subtree
            return self.lazy[index] + self.query(start, end, l, m, 2 * index)
        elif m <= start:
            return self.lazy[index] + self.query(start, end, m, r, 2 * index + 1)
        else: # start < m < end
            return self.lazy[index] + max(
                self.query(start, m, l, m, 2 * index),
                self.query(m, end, m, r, 2 * index + 1)
            )
        
    def update(self, start, end, delta=1, l=LOWER, r=UPPER, index=1):
        """
		node information: l, r, index
        query interval: start, end
		"""
		
        if start == l and end == r:
            self.val[index] += delta # update the current node val, which is range MAX in this case
            self.lazy[index] += delta # for all numbers in this range [l, r), they have to be updated, 
            # but there is no need to do it now. store the values to be applied in the lazy variable
            return

        m = (l + r) // 2

        if end <= m: # target range completely in the left subtree
            self.update(start, end, l, m, 2 * index)
        elif m <= start:
            self.update(start, end, m, r, 2 * index + 1)
        else: # start < m < end
            self.update(start, m, l, m, 2 * index)
            self.update(m, end, m, r, 2 * index + 1)

        self.val[index] = self.lazy[index] + max(self.val[2 * index], self.val[2 * index + 1])
 
        return



nums = [5, 2, 6, 3, 7, 4, 1, 1]
tree = RangeSumSegmentTree(nums)
print({k: v for k, v in sorted(tree.val.items(), key=lambda x: x[0])})