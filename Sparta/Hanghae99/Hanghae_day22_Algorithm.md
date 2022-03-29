# [항해99 6기] 알고리즘 주간(18) - 2022.03.28

<!-- TOC -->

- [[항해99 6기] 알고리즘 주간18 - 2022.03.28](#%ED%95%AD%ED%95%B499-6%EA%B8%B0-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%A3%BC%EA%B0%8418---20220328)
- [Learned](#learned)
  - [퀵 정렬](#%ED%80%B5-%EC%A0%95%EB%A0%AC)
    - [시간복잡도](#%EC%8B%9C%EA%B0%84%EB%B3%B5%EC%9E%A1%EB%8F%84)
    - [구현](#%EA%B5%AC%ED%98%84)
  - [리스트 정렬](#%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%A0%95%EB%A0%AC)
  - [색 정렬 - 더 공부하기](#%EC%83%89-%EC%A0%95%EB%A0%AC---%EB%8D%94-%EA%B3%B5%EB%B6%80%ED%95%98%EA%B8%B0)
  - [[이코테]국영수](#%EC%9D%B4%EC%BD%94%ED%85%8C%EA%B5%AD%EC%98%81%EC%88%98)
  - [[이코테]안테나](#%EC%9D%B4%EC%BD%94%ED%85%8C%EC%95%88%ED%85%8C%EB%82%98)
  - [[boj]좌표 정렬하기](#boj%EC%A2%8C%ED%91%9C-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0)
  - [[boj]좌표 정렬하기2](#boj%EC%A2%8C%ED%91%9C-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B02)
- [Retrospect](#retrospect)

<!-- /TOC -->

# Learned
- 퀵 정렬
- 리스트 정렬
- 색 정렬
- [이코테]국영수
- [이코테]안테나
- [boj]좌표 정렬하기
- [boj]좌표 정렬하기2

## 퀵 정렬
- 분할정복을 통해서 배열을 정렬하는 알고리즘
  1. 리스트 가운데서 하나의 원소를 고른다. 이렇게 고른 원소를 피벗이라고 한다.  
  2. 피벗 앞에는 피벗보다 값이 작은 모든 원소들이 오고, 피벗 뒤에는 피벗보다 값이 큰 모든 원소들이 오도록 피벗을 기준으로 리스트를 둘로 나눈다. 이렇게 리스트를 둘로 나누는 것을 분할이라고 한다. 분할을 마친 뒤에 피벗은 더 이상 움직이지 않는다.
  3. 분할된 두 개의 작은 리스트에 대해 재귀(Recursion)적으로 이 과정을 반복한다. 재귀는 리스트의 크기가 0이나 1이 될 때까지 반복된다.

### 시간복잡도
- 평균적으로는 O(NlogN) 이지만,  
  이미 정렬이 되어있는 상태에서는 **O(N^2)**이다.

### 구현
``` python
def quicksort(lst, start, end):
    def partition(part, ps, pe):
        pivot = part[pe]
        i = ps - 1
        for j in range(ps, pe):
            if part[j] <= pivot:
                i += 1
                part[i], part[j] = part[j], part[i]
        
        part[i+1], part[pe] = part[pe], part[i+1]
        return i + 1
    
    if start >= end:
        return None
    
    p = partition(lst, start, end)
    quicksort(lst, start, p-1)
    quicksort(lst, p+1, end)
    
    return lst
```

## 리스트 정렬
- 문제 : https://leetcode.com/problems/sort-list/
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/programmers/17_58_sort-list.md  

## 색 정렬 - 더 공부하기
- 문제 : https://leetcode.com/problems/sort-colors/
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/programmers/17_63_sort-colors.md  

## [이코테]국영수
- 문제 : https://www.acmicpc.net/problem/10825
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/pyhon-for-coding-test/14_23.md  

## [이코테]안테나
- 문제 : https://www.acmicpc.net/problem/
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/pyhon-for-coding-test/14_24.md  

## [boj]좌표 정렬하기
- 문제 : https://www.acmicpc.net/problem/11650
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/Baekjoon-Online-Judge/11650.md  

## [boj]좌표 정렬하기2
- 문제 : https://www.acmicpc.net/problem/11651
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/Baekjoon-Online-Judge/11651.md  

# Retrospect
퀵 정렬이 이렇게 헷갈리던 것이었나..?  
피봇을 하나 정하고, 피봇보다 작은건 왼쪽 큰건 오른쪽  
작은쪽은 처음 피봇-1까지 큰쪽은 처음 피봇+1부터 재귀!