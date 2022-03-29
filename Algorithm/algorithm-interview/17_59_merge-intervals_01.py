from heapq import merge
from re import S
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        
        intervals = sorted(intervals, key=lambda x: x[0])
        
        for i in intervals:
            if ans and i[0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], i[1])
            else:
                ans += i,
        
        return ans

intervals = [[1,3],[2,6],[8,16],[15,18]]
o = Solution()
print(o.merge(intervals))