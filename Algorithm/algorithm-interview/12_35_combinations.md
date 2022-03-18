# 조합

<!-- TOC -->

- [조합](#%EC%A1%B0%ED%95%A9)
  - [문제](#%EB%AC%B8%EC%A0%9C)
  - [예시](#%EC%98%88%EC%8B%9C)
  - [숙고 1](#%EC%88%99%EA%B3%A0-1)
  - [코드 1](#%EC%BD%94%EB%93%9C-1)

<!-- /TOC -->

## 문제
- https://leetcode.com/problems/combinations/
- 두 개의 정수 n과 k가 주어지면 [1, n] 범위에서 가능한 모든 k 숫자 조합을 반환하여라.
## 예시
``` python
Example 1:
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

Example 2:
Input: n = 1, k = 1
Output: [[1]]
```

## 숙고 1
- 이 문제는 itertools의 combinations를 사용하면 될 것 같다.
## 코드 1
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/12_35_combinations_01.py
``` python
class Solution:
  def combine(self, n: int, k: int) -> List[List[int]]:
    nums = [i for i in range(1, n + 1)]
    result = list(combinations(nums, k))
    
    return result
  
```
## 숙고 2
- DFS를 공부해서 풀어보자.