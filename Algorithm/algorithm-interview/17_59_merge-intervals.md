# 구간 병합

<!-- TOC -->

- [구간 병합](#%EA%B5%AC%EA%B0%84-%EB%B3%91%ED%95%A9)
  - [문제](#%EB%AC%B8%EC%A0%9C)
  - [에시](#%EC%97%90%EC%8B%9C)
  - [숙고 1](#%EC%88%99%EA%B3%A0-1)
  - [코드 1](#%EC%BD%94%EB%93%9C-1)

<!-- /TOC -->

## 문제
- 문제 : https://leetcode.com/problems/merge-intervals/
- interval[i] = [starti, endi]인 간격의 배열이 주어지면,  
  겹치는 모든 간격을 병합하고 입력의 모든 간격을 포함하는 겹치지 않는 간격의 배열을 반환하여라.

## 에시
``` python
Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

## 숙고 1
- 이러한 아이디어를 어떻게 생각할 수 있지..
- 우선 전달 받은 리스트를 첫번째 요소를 기준으로 정렬한다.  
  결과 리스트에 요소쌍이 존재하면 있으면,  
  다음 요소의 첫 요소와 결과 리스트 요소의 뒷 요소와 크기를 비교해서  
  결과 리스트에 있는 요소의 뒷 요소의 값이 크면 병합한다.  
  아니라면 결과 리스트에 해당 요소쌍을 바로 삽입한다.

## 코드 1
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/17_59_merge-intervals_01.py
``` python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        
        # 전달 받은 리스트 정렬
        intervals = sorted(intervals, key=lambda x: x[0])
        
        # 리스트 길이 만큼 반복
        for i in intervals:
            # 다음 요소의 첫요소와, 결과 리스트 마지막 요소의 뒷요소 비교
            if ans and i[0] <= ans[-1][1]:
                # 병합
                ans[-1][1] = max(ans[-1][1], i[1])
            else:
                # 결과 리스트에 삽입 
                ans += i,
        
        return ans
```