from collections import deque
import enum
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        queue = deque()
        
        for idx, candidate in enumerate(candidates):
            queue.append((idx, candidate, [candidate]))
        
        n = len(candidates)
        
        while queue:
            idx, cur_sum, arr = queue.popleft()

            if cur_sum == target:
                ans.append(arr)
            for i in range(idx, n):
                candidate = candidates[i]
                new_sum = cur_sum + candidate
                new_arr = arr.copy()
                new_arr.append(candidate)

                if new_sum == target:
                    ans.append(new_arr)
                elif new_sum < target:
                    queue.append((i, new_sum, new_arr))
        
        return ans


candidates = [2, 3, 6, 7]
target = 7
o = Solution()
print(o.combinationSum(candidates, target))
