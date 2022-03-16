# 중복 문자가 없는 가장 긴 부분 문자열

<!-- TOC -->

- [중복 문자가 없는 가장 긴 부분 문자열](#%EC%A4%91%EB%B3%B5-%EB%AC%B8%EC%9E%90%EA%B0%80-%EC%97%86%EB%8A%94-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EB%B6%80%EB%B6%84-%EB%AC%B8%EC%9E%90%EC%97%B4)
  - [문제](#%EB%AC%B8%EC%A0%9C)
  - [예시](#%EC%98%88%EC%8B%9C)
  - [숙고 1](#%EC%88%99%EA%B3%A0-1)
  - [코드 1](#%EC%BD%94%EB%93%9C-1)

<!-- /TOC -->

## 문제
- https://leetcode.com/problems/longest-substring-without-repeating-characters/
- 문자열 s가 주어지면 문자를 반복하지 않고 가장 긴 부분 문자열의 길이를 찾습니다.
## 예시
``` python
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

## 숙고 1
- 고민고민 하다가 풀이를 보게되었다..
- dictionary, max_len, start_index를 생성한다.  
  문자열을 enumerate를 통해 인덱스와 문자로 받아온다.  
  문자열이 있는동안 반복하면서  

  현재 문자가 dictionary에 있고 start_index 보다 크거나 같은 인덱스라면  
  start_index를 현재 문자의 인덱스로 교체한다.  
  아니라면 기존 max_len을 현재 문자 인덱스 - start_index + 1과 비교하여 교체한다.  

  문자의 인덱스를 dictionary에 저장한다.  

  반복이 끝나면 max_len을 반환한다.

## 코드 1
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/11_30_longest-substring-without-repeating-characters_01.py  
``` python
class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    # 문자별로 인덱스를 관리할 dictionary
    used = {}
    # 최대길이, 최대길이 문자열의 첫 인덱스를 0으로 초기화
    max_length = start = 0

    # 문자열이 있는동안 index와 문자를 사용하며 반복
    for index, char in enumerate(s):
      
      # 문자가 dictionary에 있고,
      # 최대길이 문자열의 인덱스가 현재 문자의 인덱스보다 작거나 같으면
      # 첫 인덱스를 변경해준다.
      if char in used and start <= used[char]:
        start = used[char] + 1
      # 아닐경우 최대 길이를 비교하여 저장한다.
      else:
        max_length = max(max_length, index - start + 1)
      
      # 문자를 관리하기 위해 문자의 index를 dictionary 에 넣는다(교체한다)
      used[char] = index

    return max_length
```
