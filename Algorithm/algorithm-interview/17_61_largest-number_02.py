from re import I
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        for i in range(1, len(nums)):
            for j in range(i, 0, -1):
                if str(nums[j-1]) + str(nums[j]) < str(nums[j]) + str(nums[j-1]):
                    nums[j], nums[j-1] = nums[j-1], nums[j]
                else:
                    break
        
        return str(int(''.join(map(str, nums))))
      
nums = [3,30,34,5,9]
o = Solution()
print(o.largestNumber(nums))