# [항해99 6기] 알고리즘 주간(12) - 2022.03.22

<!-- TOC -->

- [[항해99 6기] 알고리즘 주간12 - 2022.03.22](#%ED%95%AD%ED%95%B499-6%EA%B8%B0-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%A3%BC%EA%B0%8412---20220322)
- [Learned](#learned)
  - [이진 트리](#%EC%9D%B4%EC%A7%84-%ED%8A%B8%EB%A6%AC)
    - [용어 정리](#%EC%9A%A9%EC%96%B4-%EC%A0%95%EB%A6%AC)
    - [Graph vs Tree](#graph-vs-tree)
    - [이진 트리](#%EC%9D%B4%EC%A7%84-%ED%8A%B8%EB%A6%AC)
    - [완전 이진 트리](#%EC%99%84%EC%A0%84-%EC%9D%B4%EC%A7%84-%ED%8A%B8%EB%A6%AC)
    - [완전 이진 트리 배열로 표현](#%EC%99%84%EC%A0%84-%EC%9D%B4%EC%A7%84-%ED%8A%B8%EB%A6%AC-%EB%B0%B0%EC%97%B4%EB%A1%9C-%ED%91%9C%ED%98%84)
    - [완전 이진 트리의 높이](#%EC%99%84%EC%A0%84-%EC%9D%B4%EC%A7%84-%ED%8A%B8%EB%A6%AC%EC%9D%98-%EB%86%92%EC%9D%B4)
    - [완전 이진 트리 높이, 개수,](#%EC%99%84%EC%A0%84-%EC%9D%B4%EC%A7%84-%ED%8A%B8%EB%A6%AC-%EB%86%92%EC%9D%B4-%EA%B0%9C%EC%88%98)
  - [이진 트리의 최대 깊이 - 더 공부하기](#%EC%9D%B4%EC%A7%84-%ED%8A%B8%EB%A6%AC%EC%9D%98-%EC%B5%9C%EB%8C%80-%EA%B9%8A%EC%9D%B4---%EB%8D%94-%EA%B3%B5%EB%B6%80%ED%95%98%EA%B8%B0)
  - [이진 트리의 직경 - 더 공부하기](#%EC%9D%B4%EC%A7%84-%ED%8A%B8%EB%A6%AC%EC%9D%98-%EC%A7%81%EA%B2%BD---%EB%8D%94-%EA%B3%B5%EB%B6%80%ED%95%98%EA%B8%B0)
  - [가장 긴 동일 값의 경로 - 더 공부하기](#%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EB%8F%99%EC%9D%BC-%EA%B0%92%EC%9D%98-%EA%B2%BD%EB%A1%9C---%EB%8D%94-%EA%B3%B5%EB%B6%80%ED%95%98%EA%B8%B0)
  - [이진 트리 반전 - 더 공부하기](#%EC%9D%B4%EC%A7%84-%ED%8A%B8%EB%A6%AC-%EB%B0%98%EC%A0%84---%EB%8D%94-%EA%B3%B5%EB%B6%80%ED%95%98%EA%B8%B0)
  - [[boj트리의 부모 찾기 - 더 공부하기](#boj%ED%8A%B8%EB%A6%AC%EC%9D%98-%EB%B6%80%EB%AA%A8-%EC%B0%BE%EA%B8%B0---%EB%8D%94-%EA%B3%B5%EB%B6%80%ED%95%98%EA%B8%B0)
- [Retrospect](#retrospect)

<!-- /TOC -->

# Learned
- 이진 트리
- 이진 트리의 최대 깊이
- 이진 트리의 직경
- 가장 긴 동일 값의 경로
- 이진 트리 반전
- [boj]트리의 부모 찾기

## 이진 트리
- 비선형 자료구조  
  선형 자료구조는 자료를 저장하고 꺼내는 것에 초점이 맞춰져 있다면,  
  비선형 자료구조는 표현에 초점이 맞춰져 있다.

### 용어 정리
- Node: 트리에서 데이터를 저장하는 기본 요소  
- Root Node: 트리 맨 위에 있는 노드  
- Level: 최상위 노드를 Level 0으로 하였을 때,  
  하위 Branch로 연결된 노드의 깊이를 나타냄  
- Parent Node: 어떤 노드의 상위 레벨에 연결된 노드  
- Child Node: 어떤 노드의 하위 레벨에 연결된 노드  
- Leaf Node(Terminal Node): Child Node가 하나도 없는 노드  
- Sibling: 동일한 Parent Node를 가진 노드  
- Depth: 트리에서 Node가 가질 수 있는 최대 Level  

### Graph vs Tree
- 트리는 순환 구조를 갖지 않는, 루트가 하나인 그래프

### 이진 트리
- 각 노드가 최대 두 개의 자식을 가짐  
  하위 노드가 4~5개를 갖는것은 불가능, 0~2개만 가능

### 완전 이진 트리
- 노드를 삽입할 때 최하단 왼쪽 노드부터 차례대로 삽입해야 함
``` python
  o      Level 0
o   o    Level 1
  o o     Level 2  # -> 이진 트리 O 완전 이진 트리 X

  o      Level 0
o   o    Level 1
o o o     Level 2  # -> 이진 트리 O 완전 이진 트리 O
```

### 완전 이진 트리 배열로 표현
- 완전 이진 트리는 왼쪽부터 데이터가 쌓이게 되는데,  
  이를 순서대로 배열에 쌓으면서 표현하면 아래와 같다.
```python
      8      Level 0 -> [**8**] 첫번째 레벨의 8을 넣고,
    6   3    Level 1 -> [8, **6, 3**] 다음 레벨인 6, 3을 넣고
   4 2 5     Level 2 -> [8, 6, 3, **4, 2, 5**] 다음 레벨인 4, 2, 5를 삽입
```
### 완전 이진 트리의 높이
- 트리의 높이(Height)는, 루트 노드부터 가장 아래 리프 노드까지의 길이
```python
  o      Level 0  # 루트 노드
o   o    Level 1
o o o     Level 2  # 가장 아래 리프 노드

이 트리의 높이는 ? 2 - 0 = 2! 
```
### 완전 이진 트리 높이, 개수, 
- 노드가 꽉차있고 **레벨이 K**라면 최대 노드의 수는 : n = **2^k**
- **높이가 h**인데 모든 노드가 꽉 차있는 이진 트리라면 노드의 수는 : n = **2^(h+1) - 1**
- 최대 노드의 수가 n이라면 h는 : h = **log2(N+1)-1**
- **따라서 이진 트리의 높이는 최대 O(log(N))**

## 이진 트리의 최대 깊이 - 더 공부하기
- 문제 : https://leetcode.com/problems/maximum-depth-of-binary-tree/
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/14_42_maximum-depth-of-binary-tree.md 

## 이진 트리의 직경 - 더 공부하기
- 문제 : https://leetcode.com/problems/diameter-of-binary-tree/
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/14_43_diameter-of-binary-tree.md 

## 가장 긴 동일 값의 경로 - 더 공부하기
- 문제 : https://leetcode.com/problems/longest-univalue-path/
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/14_44_longest-univalue-path.md 

## 이진 트리 반전 - 더 공부하기
- 문제 : https://leetcode.com/problems/invert-binary-tree/
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/14_45_invert-binary-tree.md 

## [boj트리의 부모 찾기 - 더 공부하기
- 문제 : https://www.acmicpc.net/problem/11725
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/Baekjoon-Online-Judge/9663.md  

# Retrospect
여전히 나를 괴롭히는 DFS..  
그래도 흐름이 보인다.