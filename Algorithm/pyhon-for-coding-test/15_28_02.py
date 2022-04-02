from bisect import bisect_left
from typing import List


n = input().split()
lst = list(map(int, input().split()))

def fixed_point(lst:List):
    lo = 0
    hi = len(lst)
    
    while lo < hi :
        mid = (lo + hi) // 2
        if lst[mid] < mid:
            lo = mid + 1
        else:
            hi = mid
            
    if lo >= len(lst) or lo != lst[lo]:
        return -1
    return lo

print(fixed_point(lst))