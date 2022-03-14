from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(0, len(temperatures)):
            after_days = 0
            flag = False

            for j in range(i + 1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    flag = True
                    after_days += 1
                    break
                else:
                    after_days += 1

            if flag is not True:
                after_days = 0
            result.append(after_days)
        return result


testcase_1 = [73, 74, 75, 71, 69, 72, 76, 73]
testcase_2 = [30, 40, 50, 60]
testcase_3 = [30, 60, 90]

o = Solution()
print(o.dailyTemperatures(testcase_1))
print(o.dailyTemperatures(testcase_2))
print(o.dailyTemperatures(testcase_3))
