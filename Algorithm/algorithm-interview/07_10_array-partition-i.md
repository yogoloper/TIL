# 배열 파티션  

<!-- TOC -->

- [배열 파티션](#%EB%B0%B0%EC%97%B4-%ED%8C%8C%ED%8B%B0%EC%85%98)
  - [문제](#%EB%AC%B8%EC%A0%9C)
  - [숙고 1](#%EC%88%99%EA%B3%A0-1)
  - [코드 1](#%EC%BD%94%EB%93%9C-1)

<!-- /TOC -->

## 문제
- https://leetcode.com/problems/array-partition-i  
- 2n 개의 정수 배열이 주어지면 n쌍으로 묶고  
- 묶인 쌍에서 작은 값들만 더한것이  
- 모든 그룹화를 거친 값중 제일 높은 값을 구하여라.
``` python
Example 1:  
nums = [1,4,3,2]  
Output: 4  
Example 2:  
Input: nums = [6,2,6,5,1,2]  
Output: 9 
```
## 숙고 1
- 배열의 요소들 중에서 큰 숫자들을 최대한 덜 버리기 위해서는  
  오름차순으로 정렬해 앞에서 부터 차례대로 쌍을 맺어야 한다.

## 코드 1
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/07_10_array-partition-i_01.py
```python
class Solution(object):
    def arrayPairSum(self, nums):
        # 값을 더할 변수
        sum = 0
        # 쌍으로 묶을 배열 변수
        pair = []
        # 정렬
        nums.sort()

        for n in nums:
            # 쌍 배열에 요소를 추가하고
            pair.append(n)
            # 쌍 배열의 길이가 2이면
            # 두 개 중 작은 값을 구해서 결과에 더해준다
            if len(pair) == 2:
                sum += min(pair)
                # 연산을 마친 쌍 배열은 초기화 해준다
                pair = []
        
        return sum
        
```
