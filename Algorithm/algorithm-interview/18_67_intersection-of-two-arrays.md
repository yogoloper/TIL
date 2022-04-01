# 두 배열의 교집합

<!-- TOC -->

- [두 배열의 교집합](#%EB%91%90-%EB%B0%B0%EC%97%B4%EC%9D%98-%EA%B5%90%EC%A7%91%ED%95%A9)
  - [문제](#%EB%AC%B8%EC%A0%9C)
  - [예시](#%EC%98%88%EC%8B%9C)
  - [숙고 1](#%EC%88%99%EA%B3%A0-1)
  - [코드 1](#%EC%BD%94%EB%93%9C-1)

<!-- /TOC -->

## 문제
- 문제 : https://leetcode.com/problems/intersection-of-two-arrays/
- 두 정수 배열이 주어지면 이들의 교집합 배열을 반환하여라.  
  교집합 배열의 순서는 상관 없으며 요소의 중복은 없어야 한다.

## 예시
``` python
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
```

## 숙고 1
- 두 번째 배열을 반복하면서 첫 번째 배열에서 값을 찾아내면 될 듯 하다.  
  중복을 없애기 위해서 set으로 결과 요소를 담자.

## 코드 1
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/18_67_intersection-of-two-arrays_01.py  
``` python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = set()
        
        nums1.sort()
        nums2.sort()
        
        for i in nums2:
            idx = bisect_left(nums1, i)
            
            if idx < len(nums1) and nums1[idx] == i:
                ans.add(i)
        
        return list(ans)
```
