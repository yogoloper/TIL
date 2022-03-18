from itertools import combinations
from typing import List


class Solution:
  def combine(self, n: int, k: int) -> List[List[int]]:
    nums = [i for i in range(1, n + 1)]
    result = list(combinations(nums, k))
    
    return result
  
n = 4
k = 2
o = Solution()
print(o.combine(n, k))