from bisect import bisect_left
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(lst, start, end):
            if start > end:
                return -1

            mid = (start + end) // 2
            if lst[mid] < target:
                return bs(lst, mid + 1, end)
            elif lst[mid] > target:
                return bs(lst, start, mid - 1)
            else:
                return mid

        if not nums:
            return -1

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        added = nums + nums[:left]

        result = bs(added, left, len(added) - 1)
        return result if result == -1 else result % len(nums)

nums = [1, 3]
nums = [4,5,6,7,0,1,2]
nums = []
target = 1
o = Solution()
print(o.search(nums, target))