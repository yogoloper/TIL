from bisect import bisect_left
from typing import List


n = input().split()
arr = list(map(int, input().split()))

result = -1
def bs_fixpoint(nums:List, target):
    if not nums:
        return -1
    
    bs_idx = bisect_left(nums, target)
    
    if bs_idx < len(nums):
        if nums[bs_idx] < bs_idx:
            mid = len(nums[bs_idx+1:]) // 2
            return bs_fixpoint(nums[bs_idx+1:], arr[mid])
        elif nums[bs_idx] > bs_idx:
            mid = len(nums[:bs_idx-1]) // 2
            return bs_fixpoint(nums[:bs_idx-1], arr[mid])
        else:
            return nums[bs_idx]

mid = len(arr) // 2
result = bs_fixpoint(arr, arr[mid])
print(result)