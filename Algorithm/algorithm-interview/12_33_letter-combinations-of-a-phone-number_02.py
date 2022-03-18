from typing import List


class Solution:
  dic = {
    '2' : 'abc',
    '3' : 'def',
    '4' : 'ghi',
    '5' : 'jkl',
    '6' : 'mno',
    '7' : 'pqrs',
    '8' : 'tuv',
    '9' : 'wxyz',
  }
  
  def letterCombinations(self, digits: str) -> List[str]:
    def dfs(index, path):
      
      if len(path) == len(digits):
        result.append(path)
        return
    
      for i in range(index, len(digits)):
        for j in self.dic[digits[i]]:
          print('index: ', index, 'i:', i, 'j:', j, 'dfs(',i+1, ', ', path + j, ')' )
          dfs(i + 1, path + j)
        print('---------------------------------------')
    
    if not digits:
      return []
    
    result = []
    dfs(0, "")
    
    return result

digits = "23"
o = Solution()
print(o.letterCombinations(digits))