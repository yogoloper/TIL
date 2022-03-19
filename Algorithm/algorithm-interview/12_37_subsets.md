# 부분 집합

<!-- TOC -->

- [부분 집합](#%EB%B6%80%EB%B6%84-%EC%A7%91%ED%95%A9)
  - [문제](#%EB%AC%B8%EC%A0%9C)
  - [예시](#%EC%98%88%EC%8B%9C)
  - [숙고 1](#%EC%88%99%EA%B3%A0-1)
  - [코드 1](#%EC%BD%94%EB%93%9C-1)

<!-- /TOC -->

## 문제
- https://leetcode.com/problems/subsets/
- 고유한 요소의 정수 배열이 주어지면 가능한 모든 하위 집합을 반환하여라.  
  
  솔루션 세트에는 중복 서브세트가 포함되어서는 안된다.  
  임의의 순서로 솔루션을 반환하여라.

## 예시
``` python
Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
```

## 숙고 1
- 풀긴 했는데.. 어떻게 해서 풀린건지 잘..  
- 결과 배열에 빈 배열 하나를 추가하여 주고  
  큐를 통해서 숫자 요소들을 (인덱스, [숫자]) 형태로 전부 넣어준다.  
  큐가 있는 동안 반복한다.  

  큐에서 하나씩 인덱스와 숫자배열을 추출하고  
  결과 리스트에 숫자 배열을 더해준다.  

  추출된 요소의 인덱스 + 1을 해 다음 숫자를 배열에 넣고,  
  큐에 증가된 인덱스와 추가된 숫자배열을 넣어준다.
  
## 코드 1
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/12_37_subsets_01.py
``` python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 결과를 담을 배열, 빈 배열도 초기화 해준다.
        ans = [[]]
        queue = deque()
        
        # 숫자 요소들 전부 (idx, [num]) 형태로 큐에 넣는다.
        for idx, num in enumerate(nums):
            queue.append((idx, [num]))
        
        lenth = len(nums)
        
        while queue:
            # 큐에서 요소를 추출하고
            idx, arr = queue.popleft()
            
            # 결과에 추가해준다.

            # 중복 제거를 위해 조건을 걸어 주었지만
            # 인덱스가 섞이지 않으므로 조건이 없더라도 중복되지 않는다.
            # 조건이 없는게 더 빠르다.
            if arr not in ans:
                ans.append(arr)
            
            # 다음 숫자를 배열에 추가하기 위해 idx + 1에서 lenth까지 돌며  
            # 증가된 인덱스와 더해진 배열을 큐에 넣어준다.
            for i in range(idx+1, lenth):
                num = nums[i]
                new_arr = arr.copy()
                new_arr.append(num)
                
                queue.append((i, new_arr))
        return ans
```