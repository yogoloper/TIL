# [항해99 6기] 알고리즘 주간(9) - 2022.03.19

<!-- TOC -->

- [[항해99 6기] 알고리즘 주간9 - 2022.03.19](#%ED%95%AD%ED%95%B499-6%EA%B8%B0-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%A3%BC%EA%B0%849---20220319)
- [Learned](#learned)
  - [BFS](#bfs)
    - [BFS 구현](#bfs-%EA%B5%AC%ED%98%84)
  - [조합의 합](#%EC%A1%B0%ED%95%A9%EC%9D%98-%ED%95%A9)
  - [부분 집합](#%EB%B6%80%EB%B6%84-%EC%A7%91%ED%95%A9)
  - [일정 재구성 - 더 공부하기](#%EC%9D%BC%EC%A0%95-%EC%9E%AC%EA%B5%AC%EC%84%B1---%EB%8D%94-%EA%B3%B5%EB%B6%80%ED%95%98%EA%B8%B0)
  - [코스 스케줄 - 더 공부하기](#%EC%BD%94%EC%8A%A4-%EC%8A%A4%EC%BC%80%EC%A4%84---%EB%8D%94-%EA%B3%B5%EB%B6%80%ED%95%98%EA%B8%B0)
  - [[boj]단지번호붙이기 BFS - 더 공부하기](#boj%EB%8B%A8%EC%A7%80%EB%B2%88%ED%98%B8%EB%B6%99%EC%9D%B4%EA%B8%B0-bfs---%EB%8D%94-%EA%B3%B5%EB%B6%80%ED%95%98%EA%B8%B0)
  - [[boj]바이러스 BFS - 더 공부하기](#boj%EB%B0%94%EC%9D%B4%EB%9F%AC%EC%8A%A4-bfs---%EB%8D%94-%EA%B3%B5%EB%B6%80%ED%95%98%EA%B8%B0)
- [Retrospect](#retrospect)

<!-- /TOC -->

# Learned
- BFS
- 조합의 합
- 부분 집합
- 일정 재구성
- 코스 스케줄
- [boj]단지번호붙이기
- [boj]바이러스

## BFS
- 인접노드를 먼저 방문하는 형태의 알고리즘
- 큐로 구현의 방법  
  1. 루트 노드를 큐에 넣는다.  
  2. 현재 큐의 노드를 빼서 visited 에 추가한다.  
  3. 현재 방문한 노드와 인접한 노드 중 방문하지 않은 노드를 큐에 추가한다.  
  4. 2부터 반복한다.  
  5. 큐가 비면 탐색을 종료한다.  
- 간선의 비용이 모두 동일한 상황에서  
  최단거리 문제를 해결하기 위해서도 사용된다.
### BFS 구현
```python
from collections import deque

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}

def bfs_queue(start):
    visited = [start]
    q = deque([start])

    while q:
        node = q.popleft()
        for adj in graph[node]:
            if adj not in visited:
                q.append(adj)
                visited.append(adj)

    return visited

assert bfs_queue(1) == [1, 2, 3, 4, 5, 6, 7]
```

## 조합의 합
- 문제 : https://leetcode.com/problems/combination-sum/
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/12_36_combination-sum.md 

## 부분 집합
- 문제 : https://leetcode.com/problems/subsets/
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/12_37_subsets.md 

## 일정 재구성 - 더 공부하기
- 문제 : https://leetcode.com/problems/reconstruct-itinerary/
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/12_38_reconstruct-itinerary.md

## 코스 스케줄 - 더 공부하기
- 문제 : https://leetcode.com/problems/course-schedule/
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/12_39_course-schedule.md 

## [boj]단지번호붙이기 (BFS) - 더 공부하기
- 문제 : https://www.acmicpc.net/problem/2667
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/Baekjoon-Online-Judge/2667_BFS.md  

## [boj]바이러스 (BFS) - 더 공부하기
- 문제 : https://www.acmicpc.net/problem/2606
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/Baekjoon-Online-Judge/2606_BFS.md  

# Retrospect
BFS로 접근하라고 하니 DFS 보다 마음은 편했던것 같다.  
그런데 머리는 여전히 불편하다.  
DFS나 BFS 둘다 반복을 하면서 인덱스 관리를 하는게 어려운것 같다.  
반복을 해야겠다.  
익숙해 질때까지