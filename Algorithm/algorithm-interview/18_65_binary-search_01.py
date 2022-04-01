from bisect import bisect_left
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans = 0
        
        idx = bisect_left(nums, target)
        
        if idx < len(nums) and nums[idx] == target:
            ans = idx
        else:
            ans = -1
            
        return ans
        
nums = [-1,0,3,5,9,12]
# nums = [i for i in range(1, 46)]
print(nums)
target = 4
o = Solution()
# print(o.search(nums, target))