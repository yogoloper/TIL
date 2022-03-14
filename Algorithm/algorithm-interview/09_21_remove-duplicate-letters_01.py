import collections
from curses.ascii import SO
from gc import collect
from typing import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = collections.Counter(s)
        seen = set()
        stack = []
        
        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)
                
        
        return ''.join(stack)

testcase_1 = "bcabc"
testcase_2 = "cbacdcbc"

o = Solution()
# print(o.removeDuplicateLetters(testcase_1))
print(o.removeDuplicateLetters(testcase_2))