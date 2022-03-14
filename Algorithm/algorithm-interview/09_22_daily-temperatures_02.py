from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        
        for i, cur in enumerate(temperatures):
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
            
        return answer


testcase_1 = [73, 74, 75, 71, 69, 72, 76, 73]
testcase_2 = [30, 40, 50, 60]
testcase_3 = [30, 60, 90]

o = Solution()
print(o.dailyTemperatures(testcase_1))
print(o.dailyTemperatures(testcase_2))
print(o.dailyTemperatures(testcase_3))
