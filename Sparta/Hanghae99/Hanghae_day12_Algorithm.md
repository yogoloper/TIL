# [항해99 6기] 알고리즘 주간(8) - 2022.03.18

<!-- TOC -->

- [[항해99 6기] 알고리즘 주간8 - 2022.03.18](#%ED%95%AD%ED%95%B499-6%EA%B8%B0-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%A3%BC%EA%B0%848---20220318)
- [Learned](#learned)
  - [그래프](#%EA%B7%B8%EB%9E%98%ED%94%84)
    - [용어 정리](#%EC%9A%A9%EC%96%B4-%EC%A0%95%EB%A6%AC)
    - [표현방법](#%ED%91%9C%ED%98%84%EB%B0%A9%EB%B2%95)
    - [DFS 구현](#dfs-%EA%B5%AC%ED%98%84)
  - [섬의 개수 - 더 공부하기](#%EC%84%AC%EC%9D%98-%EA%B0%9C%EC%88%98---%EB%8D%94-%EA%B3%B5%EB%B6%80%ED%95%98%EA%B8%B0)
  - [전화 번호 문자 조합 - 더 공부하기](#%EC%A0%84%ED%99%94-%EB%B2%88%ED%98%B8-%EB%AC%B8%EC%9E%90-%EC%A1%B0%ED%95%A9---%EB%8D%94-%EA%B3%B5%EB%B6%80%ED%95%98%EA%B8%B0)
  - [순열 - 더 공부하기](#%EC%88%9C%EC%97%B4---%EB%8D%94-%EA%B3%B5%EB%B6%80%ED%95%98%EA%B8%B0)
  - [조합 - 더 공부하기](#%EC%A1%B0%ED%95%A9---%EB%8D%94-%EA%B3%B5%EB%B6%80%ED%95%98%EA%B8%B0)
  - [[boj]단지번호붙이기 - 더 공부하기](#boj%EB%8B%A8%EC%A7%80%EB%B2%88%ED%98%B8%EB%B6%99%EC%9D%B4%EA%B8%B0---%EB%8D%94-%EA%B3%B5%EB%B6%80%ED%95%98%EA%B8%B0)
  - [[boj]바이러스 - 더 공부하기](#boj%EB%B0%94%EC%9D%B4%EB%9F%AC%EC%8A%A4---%EB%8D%94-%EA%B3%B5%EB%B6%80%ED%95%98%EA%B8%B0)
- [Retrospect](#retrospect)

<!-- /TOC -->

# Learned
- 그래프
- 섬의 개수
- 전화 번호 문자 조합
- 순열
- 조합
- [boj]단지번호붙이기
- [boj]바이러스

## 그래프
- 그래프는 vertex와 edge로 구성된 한정된 자료구조를 의미한다.  
  vertex는 정점, edge는 정점과 정점을 연결하는 간선이다.

### 용어 정리
- 노드(Node): 연결 관계를 가진 각 데이터를 의미하며, 정점(Vertex)이라고도 한다.
- 간선(Edge): 노드 간의 관계를 표시한 선.
- 인접 노드(Adjacent Node): 간선으로 직접 연결된 노드(또는 정점)

### 표현방법
- 인접 행렬(Adjacency Matrix): 2차원 배열로 그래프의 연결 관계를 표현
- 인접 리스트(Adjacnecy List): 링크드 리스트로 그래프의 연결 관계를 표현
``` python
          2 - 3
          ⎜       
      0 - 1

1. 이를 인접 행렬, 2차원 배열로 나타내면 다음과 같다.
# 0은 1이랑만 연결되어 있고,
# 1은 0과 2와 연결되어 있다...
  0  1  2  3
0 X  O  X  X
1 O  X  O  X
2 X  O  X  O
3 X  X  O  X

이걸 배열로 표현하면 다음과 같다.
graph = [
    [False, True, False, False],
    [True, False, True, False],
    [False, True, False, True],
    [False, False, True, False]
]

2. 이번에는 인접 리스트로 표현해보면
인접 리스트는 모든 노드에 연결된 노드에 대한 정보를 차례대로 다음과 같이 저장된다.
# 0은 1이랑만 연결되어 있고,
# 1은 0과 2와 연결되어 있다...

0 -> 1
1 -> 0 -> 2
2 -> 1 -> 3
3 -> 2

이를 딕셔너리로 표현하면 다음과 같다.
graph = {
    0: [1],
    1: [0, 2]
    2: [1, 3]
    3: [2]
}
```

### DFS 구현
- 갈 수 있는 만큼 계속해서 탐색하다가 갈 수 없게 되면 다른 방향으로 다시 탐색하는 구조
  - 노드를 방문하고 깊이 우선으로 인접한 노드를 방문한다.
  - 또 그 노드를 방문해서 깊이 우선으로 인접한 노드를 방문한다.
  - 위 과정을 반복한다.
```python
graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}

def dfs_recursive(node, visited):
    # 방문처리
    visited.append(node)

    # 인접 노드 방문
    for adj in graph[node]:
        if adj not in visited:
            dfs_recursive(adj, visited)

    return visited

def dfs_stack(start):
    visited = []
    # 방문할 순서를 담아두는 용도
    stack = [start]

    # 방문할 노드가 남아있는 한 아래 로직을 반복한다.
    while stack:
        # 제일 최근에 삽입된 노드를 꺼내고 방문처리한다.
        top = stack.pop()
        visited.append(top)
        # 인접 노드를 방문한다.
        for adj in graph[top]:
            if adj not in visited:
                stack.append(adj)

    return visited


from dfs_bfs.prac import dfs_recursive, dfs_stack

assert dfs_recursive(1, []) == [1, 2, 5, 6, 7, 3, 4]
assert dfs_stack(1) == [1, 4, 3, 5, 7, 6, 2]
``````

## 섬의 개수 - 더 공부하기
- 문제 : https://leetcode.com/problems/number-of-islands/
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/12_31_number-of-islands.md 

## 전화 번호 문자 조합 - 더 공부하기
- 문제 : https://leetcode.com/problems/letter-combinations-of-a-phone-number/
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/12_33_letter-combinations-of-a-phone-number.md 

## 순열 - 더 공부하기
- 문제 : https://leetcode.com/problems/permutations/
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/12_34_permutations.md

## 조합 - 더 공부하기
- 문제 : https://leetcode.com/problems/combinations/
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/12_35_combinations.md 

## [boj]단지번호붙이기 - 더 공부하기
- 문제 : https://www.acmicpc.net/problem/2667
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/Baekjoon-Online-Judge/2667.md  

## [boj]바이러스 - 더 공부하기
- 문제 : https://www.acmicpc.net/problem/2606
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/Baekjoon-Online-Judge/2606.md  

# Retrospect
DFS가 너무 어렵다  .
어렵다기 보다는 인덱스를 따라가는게 너무 힘들다..
재귀가 싫다..

재귀를 내것으로 만들기 위해서 아래의 내용을 명심하자.

재귀로 구현시 고려해야 하는 것은  
1. 반복적으로 발생하는 일을 아는 것
2. 종료조건을 아는 것

DFS의 기초
``` python
def main():
  def dfs(*1*):
    if 종료조건:
      return

    for *2* : 
      작업*3*
      dfs(*1*)
      작업 원복*3*
```