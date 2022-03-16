import collections
from curses.ascii import SO
from typing import List


class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
    result = []
    counter = collections.Counter(nums).most_common(k)
    
    for i in counter:
      result.append(i[0])
    
    return sorted(result)

o = Solution()
print(o.topKFrequent([1,1,1,2,2,3,3,3,3], 2))