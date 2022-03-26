# 가장 큰 수

<!-- TOC -->

- [가장 큰 수](#%EA%B0%80%EC%9E%A5-%ED%81%B0-%EC%88%98)
  - [문제](#%EB%AC%B8%EC%A0%9C)
  - [에시](#%EC%97%90%EC%8B%9C)
  - [숙고 1](#%EC%88%99%EA%B3%A0-1)
  - [코드 1](#%EC%BD%94%EB%93%9C-1)
  - [숙고 2](#%EC%88%99%EA%B3%A0-2)
  - [코드 2](#%EC%BD%94%EB%93%9C-2)

<!-- /TOC -->

## 문제
- 문제 : https://leetcode.com/problems/largest-number/
- 양수의 nums 리스트가 주어지면, 가장 큰 숫자가 되도록 배열하고 반환하여라.
  결과가 매우 클 수 있으므로, 문자열로 반환하여라.

## 에시
``` python
Example 1:
Input: nums = [10,2]
Output: "210"

Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"
```

## 숙고 1
- 숫자를 개별 문자로 다 바꾼뒤에 내림차순 정렬하면 되지 않나?  
  -> ㅇㅇ 안됨

## 코드 1
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/17_61_largest-number_01.py
``` python
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ans = []
        for i in nums:
            ans.append(str(i))
        
        return ''.join(sorted(ans, reverse = True))
      
```

## 숙고 2
- 두 자리 숫자는 두 자리로 붙어서 정렬되어야 하고,  
  3, 30 이 있을경우 330이 큰지, 303이 큰지 비교를 하는 것을 넣어야 한다.
- 삽입 정렬을 통해서 진행

## 코드 2
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/17_61_largest-number_02.py
``` python
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        for i in range(1, len(nums)):
            for j in range(i, 0, -1):
                # 앞요소와 뒷요소의 단순 크기를 비교하는 것이 아닌
                # 문자열로 더했을때 더 큰값을 찾는다.
                if str(nums[j-1]) + str(nums[j]) < str(nums[j]) + str(nums[j-1]):
                    nums[j], nums[j-1] = nums[j-1], nums[j]
                else:
                    break
        
        return str(int(''.join(map(str, nums))))
```