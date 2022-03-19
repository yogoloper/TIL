# 조합의 합

<!-- TOC -->

- [조합의 합](#%EC%A1%B0%ED%95%A9%EC%9D%98-%ED%95%A9)
  - [문제](#%EB%AC%B8%EC%A0%9C)
  - [예시](#%EC%98%88%EC%8B%9C)
  - [숙고 1](#%EC%88%99%EA%B3%A0-1)
  - [코드 1](#%EC%BD%94%EB%93%9C-1)

<!-- /TOC -->

## 문제
- https://leetcode.com/problems/combination-sum/
- 고유한 정수 후보의 배열과 대상 정수 대상이 주어지면  
  선택한 숫자의 합이 대상이 되는 모은 고유한 후보 조합의 목록을 반환하여라.  
  어떤 순서로든 조합을 반환할 수 있다.  

  후보자 중에서 동일한 번호를 무제한 선택할 수 있다.  
  선택한 숫자 중 하나 이상의 빈도가 다른 경우 두 조합은 고유하다.  

  주어진 입력에 대해 합계가 대상인 고유 조합의 수가 150개 미만인 것이 보장된다.  

## 예시
``` python
Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []
```

## 숙고 1
- DFS보다는 조금 마음이 편한것 같지만,  
  머리는 여전히 불편하다.
## 코드 1
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/12_36_combination-sum_01.py
``` python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 합이 taget인 조합을 담는 배열
        ans = []
        # 큐 생성
        queue = deque()
        
        # 조합 요소들을 차례로 탐색하기 위해 큐에 입력
        # idx : 현재 요소의 인덱스
        # candidate : 현재 요소의 값
        # [candidate] : 배열을 선언하고 현재 요소값 을 입력
        for idx, candidate in enumerate(candidates):
            queue.append((idx, candidate, [candidate]))
        
        # 요소 들의 길이
        n = len(candidates)
        
        # 큐가 있는 동안 반복
        while queue:
            # 큐에서 검사할 정보를 추출
            # idx : cur_sum이 target이 아닌경우 어디서 부터 요소를 비교할지를 위한 인덱스
            # cur_sum : arr을 통해 더해진 수
            # arr : cur_sum을 이루는 요소들의 배열
            idx, cur_sum, arr = queue.popleft()

            # 조합들을 통한 합이 target이라면 결과에 추가 한다.
            if cur_sum == target:
                ans.append(arr)
            
            # 큐에서 꺼낸 요소와 같은 요소부터 마지막 요소까지 꺼내어
            # 기존 요소와 더해 새로운 합을 만들고 배열에 꺼내온 요소 추가
            for i in range(idx, n):
                candidate = candidates[i]
                new_sum = cur_sum + candidate
                new_arr = arr.copy()
                new_arr.append(candidate)

                # 기존 요소와 새 요소의 합이 target이면 결과에 추가
                if new_sum == target:
                    ans.append(new_arr)
                # 기존 요소와 새 요소의 합이 target보다 작으면 큐에 삽입
                # target보다 크다면 버리게 되는 셈
                elif new_sum < target:
                    queue.append((i, new_sum, new_arr))
        
        return ans
```