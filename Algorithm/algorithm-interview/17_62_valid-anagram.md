# 유효한 에너그램

<!-- TOC -->

- [유효한 에너그램](#%EC%9C%A0%ED%9A%A8%ED%95%9C-%EC%97%90%EB%84%88%EA%B7%B8%EB%9E%A8)
  - [문제](#%EB%AC%B8%EC%A0%9C)
  - [에시](#%EC%97%90%EC%8B%9C)
  - [숙고 1](#%EC%88%99%EA%B3%A0-1)
  - [코드 1](#%EC%BD%94%EB%93%9C-1)
  - [숙고 2](#%EC%88%99%EA%B3%A0-2)

<!-- /TOC -->

## 문제
- 문제 : https://leetcode.com/problems/valid-anagram/
- 두 문자열 s, t가 주어지면, t가 s의 아나그램이면 True를 아니면 False를 반환하여라.  
  아나그램은 일반적으로 모든 원래 문자를 정확히 한 번 사용하여  
  다른 단어 또는 구의 문자를 재배열하여 형성된 단어 또는 구이다.

## 에시
``` python
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
```

## 숙고 1
- 두 문자열을 분해해서 정렬하자
- 너무 느린데 좋은 방법이 뭐가 있을까..

## 코드 1
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/17_62_valid-anagram_01.py
``` python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lst1 = sorted(list(s))
        lst2 = sorted(list(t))
        
        if ''.join(lst1) == ''.join(lst2):
            return True
        else:
            return False
```

## 숙고 2
- 한 줄로 작성하는 법도 있었다.
- 문자열을 리스트로 변환하는데 시간이 오래 걸리나보다.

코드 2
``` python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return ''.join(sorted(s)) == ''.join(sorted(t))
```