# 순열

<!-- TOC -->

- [순열](#%EC%88%9C%EC%97%B4)
  - [문제](#%EB%AC%B8%EC%A0%9C)
  - [예시](#%EC%98%88%EC%8B%9C)
  - [숙고 1](#%EC%88%99%EA%B3%A0-1)
  - [코드 1](#%EC%BD%94%EB%93%9C-1)

<!-- /TOC -->

## 문제
- https://leetcode.com/problems/permutations/
- 고유한 정수의 배열 번호가 주어지면 가능한 모든 순열을 반환한다.  
  어떤 순서로든 반환 할 수 있다.
## 예시
``` python
Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]
```

## 숙고 1
- 어제 파이썬 문법을 정리하다가 itertools를 발견한게 기억 났다.  
  itertools의 permutaions를 이용하면 될 것 같다.

## 코드 1
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview//12_34_permutations_01.py
``` python
class Solution:
  def permute(self, nums: List[int]) -> List[List[int]]:

    result = list(permutations(nums, len(nums)))
    return result
```

## 숙고 2
- DFS를 공부해서 풀어보자.