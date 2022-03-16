# 상위 K 빈도 요소

<!-- TOC -->

- [상위 K 빈도 요소](#%EC%83%81%EC%9C%84-k-%EB%B9%88%EB%8F%84-%EC%9A%94%EC%86%8C)
  - [문제](#%EB%AC%B8%EC%A0%9C)
  - [예시](#%EC%98%88%EC%8B%9C)
  - [숙고 1](#%EC%88%99%EA%B3%A0-1)
  - [코드 1](#%EC%BD%94%EB%93%9C-1)

<!-- /TOC -->

## 문제
- https://leetcode.com/problems/top-k-frequent-elements/
- 정수 배열 nums와 정수 k가 주어지면 k개의 가장 빈번한 요소를 반환합니다.  
- 어떤 순서로든 답을 반환할 수 있습니다.
## 예시
``` python
Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
```

## 숙고 1
- Counter를 통해서 숫자별로 빈도수를 묶어준다.
- most_common()을 통해서 가장 많이 노출된 항목을 k에 맞게 추려낸다.
- 추려낸 것을 돌면서 빈도수만 한 번 더 추려내서 결과에 담아준다.

## 코드 1
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/11_31_top-k-frequent-elements_01.py  
``` python
class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
    result = []
    counter = collections.Counter(nums).most_common(k)
    
    for i in counter:
      result.append(i[0])
    
    return sorted(result)
```
