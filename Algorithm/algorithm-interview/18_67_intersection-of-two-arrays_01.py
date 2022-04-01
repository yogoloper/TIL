from bisect import bisect_left
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = set()
        
        nums1.sort()
        nums2.sort()
        
        for i in nums2:
            idx = bisect_left(nums1, i)
            
            if idx < len(nums1) and nums1[idx] == i:
                ans.add(i)
        
        return list(ans)

nums1 = [1,2,2,1]
nums2 = [2,2]

nums1 = [2,1]
nums2 = [1,1]
o = Solution()
o.intersection(nums1, nums2)