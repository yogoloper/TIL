import heapq
from typing import List

class Heap:
    def __init__(self):
        self.items = [None]
    
    def __len__(self):
        return len(self.items) - 1

    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    def extract(self):
        if len(self) < 1:
            return None

        root = self.items[1]
        self.items[1] = self.items[-1]
        self.items.pop()
        self._percolate_down(1)

        return root

    def _percolate_up(self):
        cur = len(self)

        parent = cur // 2

        while parent > 0:
            if self.items[cur] > self.items[parent]:
                self.items[cur], self.items[parent] = self.items[parent], self.items[cur]
            
            cur = parent
            parent = cur // 2

    def _percolate_down(self, cur):
        biggest = cur
        left = cur * 2
        right = cur * 2 + 1

        if left <= len(self) and self.items[left] > self.items[biggest]:
            biggest = left

        if right <= len(self) and self.items[right] > self.items[biggest]:
            biggest = right

        if biggest != cur:
            self.items[cur], self.items[biggest] = self.items[biggest], self.items[cur]
            self._percolate_down(biggest)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = Heap()
        
        for elem in nums:
            heap.insert(elem)
        
        return [heap.extract() for _ in range(k)][k - 1]
        # return heapq.nlargest(k, nums)[-1]
      
nums = [3,2,1,5,6,4]
k = 2
o = Solution()
print(o.findKthLargest(nums, k))


