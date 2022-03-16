# 보석과 돌

## 문제
- https://leetcode.com/problems/jewels-and-stones/
- 보석인 스톤의 종류를 나타내는 스트링 쥬얼과 가지고 있는 스톤을 나타내는 스톤이 주어집니다.  
- 스톤의 각 캐릭터는 가지고 있는 스톤의 유형입니다.  
- 당신은 당신이 가지고 있는 돌 중 얼마나 많은 보석이 보석인지 알고 싶어합니다.
- 문자는 대소문자를 구분하므로 ""는 "A"와 다른 유형의 돌로 간주됩니다.

## 예시
``` python
Example 1:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Example 2:
Input: jewels = "z", stones = "ZZ"
Output: 0
```

## 숙고 1
- 보석 a, A를 통해서 돌에 a, A가 얼마나 있는지 확인하는 문제
- 돌에 문자별로 몇 번 등장하는지 확인하고  
  보석으로 돌에 있는 문자가 몇 번 나왔는지 확인하고 나온 값들은 더해서 반환한다.
## 코드 1
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/11_29_jewels-and-stones_01.py  
``` python
class Solution:
  def numJewelsInStones(self, jewels: str, stones: str) -> int:
    freqs= {}
    count = 0
    
    for char in stones:
      if char not in freqs:
        freqs[char] = 1
      else:
        freqs[char] += 1
        
    for char in jewels:
      if char in freqs:
        count += freqs[char]
   
    return count
```