from itertools import permutations
import re
from typing import List


class Solution:
  def permute(self, nums: List[int]) -> List[List[int]]:

    result = list(permutations(nums, len(nums)))
    return result


nums = [1,2,3]
o = Solution()
print(o.permute(nums))