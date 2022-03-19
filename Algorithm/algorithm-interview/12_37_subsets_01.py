from collections import deque
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        queue = deque()
        
        for idx, num in enumerate(nums):
            queue.append((idx, [num]))
        
        lenth = len(nums)
        
        while queue:
            idx, arr = queue.popleft()
            
            ans.append(arr)
            
            for i in range(idx+1, lenth):
                num = nums[i]
                new_arr = arr.copy()
                new_arr.append(num)
                
                queue.append((i, new_arr))
        return ans



nums = [1,2,3]
o = Solution()
print(o.subsets(nums))