from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ans = []
        for i in nums:
            ans.append(str(i))
        
        return ''.join(sorted(ans, reverse = True))
      
nums = [3,30,34,5,9]
o = Solution()
print(o.largestNumber(nums))