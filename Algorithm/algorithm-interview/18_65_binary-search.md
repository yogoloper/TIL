# 이진 검색

<!-- TOC -->

- [이진 검색](#%EC%9D%B4%EC%A7%84-%EA%B2%80%EC%83%89)
  - [문제](#%EB%AC%B8%EC%A0%9C)
  - [예시](#%EC%98%88%EC%8B%9C)
  - [숙고 1](#%EC%88%99%EA%B3%A0-1)
  - [코드 1](#%EC%BD%94%EB%93%9C-1)

<!-- /TOC -->

## 문제
- 문제 : https://leetcode.com/problems/binary-search/
- 오름차순 정렬된 숫자 배열이 nums와 대상 숫자가 주어지면  
  대상을 nums에서 검색하는 함수를 작성하여라.  
  대상이 존재하면 해당 인덱스를, 그렇지 않으면 -1을 반환하여라.

  시간 복잡도 O(logN) 제한

## 예시
``` python
Exeample 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
```

## 숙고 1
- bisect_left를 사용하자

## 코드 1
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/18_65_binary-search_01.py  
``` python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans = 0
        
        idx = bisect_left(nums, target)
        
        if idx < len(nums) and nums[idx] == target:
            ans = idx
        else:
            ans = -1
            
        return ans
```