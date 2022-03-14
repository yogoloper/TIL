# 중복 문자 제거
<!-- TOC -->

- [중복 문자 제거](#%EC%A4%91%EB%B3%B5-%EB%AC%B8%EC%9E%90-%EC%A0%9C%EA%B1%B0)
  - [문제](#%EB%AC%B8%EC%A0%9C)
    - [부연설명](#%EB%B6%80%EC%97%B0%EC%84%A4%EB%AA%85)
  - [예시](#%EC%98%88%EC%8B%9C)
  - [숙고 1](#%EC%88%99%EA%B3%A0-1)
  - [코드 1](#%EC%BD%94%EB%93%9C-1)

<!-- /TOC -->


## 문제
- https://leetcode.com/problems/remove-duplicate-letters/
- 문자열 S가 주어지면 모든 문자가 한 번만 나타나도록 중복 문자를 제거하여라.
- 결과는 사전식 순서로 반환한다.

### 부연설명
- 사전식 순서로 반환하라는 말은 문자열을 정렬하라는 것이 아닌  
  중복을 제거한 조합중에서 사전에서 검색시 가장 먼저 나올 조합으로 반환하라는 뜻

## 예시
``` python
Example 1:  
Input: s = "bcabc"
Output: "abc"

Example 2:
Input: s = "cbacdcbc"
Output: "acdb"
```
## 숙고 1
- 스택에 문자의 인덱스를 저장하고  
  결과를 반환하기 전에 사전 순서식을 관리할 수 있는 배열을 만드는 것이 좋을 것 같다.
- 풀이를 보면 collections의 Counter() 함수를 사용하는데  
  이는 문자열을 문자와, 해당 문자수를 dictionary 형태로 반환해준다.
- 문자의 순서를 기억시킬 셋을 지정해서 스택의 탑에 있는 문자가 뒤에 나올게 남아있고,  
  현재 비교 문자보다 뒷 문자라면 기억 셋에서 지워준다.

## 코드 1
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/09_21_remove-duplicate-letters_01.py  
``` python
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # 문자, 문자수를 dictionary 형태로 반환
        counter = collections.Counter(s)
        # 문자 순서를 기억시킬 셋
        seen = set()
        # 문자열을 기록할 스택 
        stack = []
        
        #문자열 반복
        for char in s:
            # 문자 dictionary에서 현재 문자의 수를 줄여준다.
            counter[char] -= 1

            # 현재 문자의 순서를 기억하게 한다면 다음 단어로 넘어간다.
            if char in seen:
                continue
            
            # 스택이 존재하고,
            # 현재 문자가 탑에 있는 문자보다 앞서고, 
            # 문자 dictionay에 탑 문자가 남아 있다면
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                # 스탭의 탑 문자를 제거
                seen.remove(stack.pop())
            
            # 현재 문자의 순서가 기억되지 않았다면
            # 문자를 스택에 넣어주고, 문자의 순서를 기억 시킨다.
            stack.append(char)
            seen.add(char)
                
        
        return ''.join(stack)
```