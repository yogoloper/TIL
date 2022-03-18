from typing import List


class Solution:
  dic = {
    '2' : ['a', 'b', 'c'],
    '3' : ['d', 'e', 'f'],
    '4' : ['g', 'h', 'i'],
    '5' : ['j', 'k', 'l'],
    '6' : ['m', 'n', 'o'],
    '7' : ['p', 'q', 'r', 's'],
    '8' : ['t', 'u', 'v'],
    '9' : ['w', 'x', 'y', 'z']
  }
  
  def letterCombinations(self, digits: str) -> List[str]:
    def recursion(digits: List[str]) -> List[str]:
      result = []
    
      if not digits:
        return []

      str = self.dic[digits.pop()]
      com_str = recursion(digits)
      
      for i in str:
        for j in com_str:
          result.append(i+j)
      
      return result
    
    result = []

    digits = list(digits)
    result = recursion(digits)

    return result
  
 

digits = "23"
o = Solution()
print(o.letterCombinations(digits))