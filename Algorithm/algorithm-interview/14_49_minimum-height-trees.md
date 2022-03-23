# 최소 높이 트리

<!-- TOC -->

- [최소 높이 트리](#%EC%B5%9C%EC%86%8C-%EB%86%92%EC%9D%B4-%ED%8A%B8%EB%A6%AC)
  - [문제](#%EB%AC%B8%EC%A0%9C)
  - [에시](#%EC%97%90%EC%8B%9C)
  - [숙고 1](#%EC%88%99%EA%B3%A0-1)
  - [코드 1](#%EC%BD%94%EB%93%9C-1)

<!-- /TOC -->

## 문제
- 문제 : https://leetcode.com/problems/minimum-height-trees/
- 트리는 두 정점이 정확히 하나의 경로로 연결된 무방향 그래프이다.  
  순환 주기가 없이 연결된 그래프는 모드 트리이다.  
- 0에서 n-1까지 레이블이 지정된 n개의 노드로 구성된 트리와  
  edge[i] = [ai, bi]인 n-1개의 가장자리 배열이 주어지면,  
  트리에서 두 노드 ai와 bi 사이에 무방향 가장자리가 있음을 나타낸다.  
  트리의 모든 노드를 루트로 선택할 수 있다.
  노드 x를 루트로 선택하면 결과 트리의 높이가 h이다.  
  가능한 모든 뿌리 나무중에서 최소 높이(즉, min(h))를 갖는 트리를 최소 높이 트리라고 한다.

  모든 MHT의 루트 레이블 목록을 반환한다. 순서는 상관 없다.  

  뿌리 나무의 높이는 뿌리와 잎 사이의 가장 긴 하향 경로의 가장자리 수이다.

## 에시
![Example 1](./images/14_49_minimum-height-trees_01.jpeg)
``` python
Example 1:
Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
```
![Example 2](./images/14_49_minimum-height-trees_02.jpeg)
``` python
Example 2:
Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]
```

## 숙고 1
- 우선 양방향 접점 정보를 통해 dictionary를 만든다. 그리고 풀이를 보자..  
  연결 노드가 적은것 부터 차례로 제거하다가 남은  
  하나, 혹은 두개의 노드가 최소 신장 트리의 루트가 된다.

## 코드 1
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/14_49_minimum-height-trees_01.py
``` python
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # 입력 받은게 없을 경우 0을 반환
        if n <= 1:
            return [0]
        
        # 그래프를 연결된 점점 정보를 통해 dictionary이 담는다.
        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        # 연결 노드가 1개 인것부터 반환 배열에 담는다.
        leaves = []
        for i in range(n + 1):
           if len(graph[i]) == 1:
              leaves.append(i)
        
        # 남는 노드의 수가 1개 혹은 2개 일때까지 반복한다.
        # 입력된 노드의 수가 짝수일때는 2개가 될 수 있기 때문
        while n > 2:
            # 확인하는 노드들의 갯수를 전체 노드 수에서 빼준다.
            n -= len(leaves)
            
            # 다음에 확인할 노드 정보를 담을 배열 선언
            new_leaves = []
            
            #확인할 노드가 있는동안 반복하며
            for leaf in leaves:
                # leaves에 접점 노드가 적은 순으로 담겨있기에
                # 모두 제거해 준다.
                neighbor = graph[leaf].pop()
                # 제거된 노드들의 연결 정보도 제거해 준다.
                graph[neighbor].remove(leaf)
                
                # 연결 정보 제거후 해당 노드의 접점 노드가 1개이면
                # 다음 반복때 제거하기 위해서 배열에 추가한다.
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            # 다음 반복시 제거하기 위해 배열을 교체 해준다.
            leaves = new_leaves
        
        return leaves
```