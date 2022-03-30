# [항해99 6기] 알고리즘 주간(20) - 2022.03.30

<!-- TOC -->

- [[항해99 6기] 알고리즘 주간20 - 2022.03.30](#%ED%95%AD%ED%95%B499-6%EA%B8%B0-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%A3%BC%EA%B0%8420---20220330)
- [Learned](#learned)
  - [힙](#%ED%9E%99)
  - [힙 정렬](#%ED%9E%99-%EC%A0%95%EB%A0%AC)
    - [시간 복잡도](#%EC%8B%9C%EA%B0%84-%EB%B3%B5%EC%9E%A1%EB%8F%84)
  - [유효한 에너그램](#%EC%9C%A0%ED%9A%A8%ED%95%9C-%EC%97%90%EB%84%88%EA%B7%B8%EB%9E%A8)
  - [[이코테]카드 정렬하기](#%EC%9D%B4%EC%BD%94%ED%85%8C%EC%B9%B4%EB%93%9C-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0)
  - [[boj]나이순 정렬](#boj%EB%82%98%EC%9D%B4%EC%88%9C-%EC%A0%95%EB%A0%AC)
  - [[boj]수 정렬하기2](#boj%EC%88%98-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B02)
- [Retrospect](#retrospect)

<!-- /TOC -->

# Learned
- 힙 정렬
- 유효한 에너그램 
- [이코테]카드 정렬하기
- [boj]나이순 정렬
- [boj]수 정렬하기2

## 힙
- 데이터에서 최대값과 최소값을 빠르게 찾기 위해 고안된 완전 이진 트리

## 힙 정렬
- 최대 힙 트리나 최소 힙 트리를 구성해 정렬을 하는 방법  
  내림차순 정렬을 위해서는 최대 힙을 구성하고  
  오름차순 정렬을 위해서는 최소 힙을 구성한다.

### 시간 복잡도
- O(NlogN)

## 유효한 에너그램
- 문제 : https://leetcode.com/problems/valid-anagram/
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/programmers/17_62_valid-anagram.md  

## [이코테]카드 정렬하기
- 문제 : https://www.acmicpc.net/problem/1715
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/pyhon-for-coding-test/14_26.md  

## [boj]나이순 정렬
- 문제 : https://www.acmicpc.net/problem/10814
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/Baekjoon-Online-Judge/10814.md  

## [boj]수 정렬하기2
- 문제 : https://www.acmicpc.net/problem/2751
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/Baekjoon-Online-Judge/2751.md  

# Retrospect
힙을 며칠 전에 본거 같은데 다시 봐도 새롭다.  
사람은 망각의 동물이라 했다.  
까먹기 전에 자주자주 보도록 하자.  

힙 한 번 더 짜보고  
오늘은 이만 다른 공부를 해야겠다.

-  heap  
    - 완전 이진 트리의 일종으로 우선순위 큐를 위하여 만들어진 자료구조이다.
    - 여러 개의 값들 중에서 최대값/최소값을 빠르게 찾아내도록 만들어진 자료구조이다.
    - 힙은 일종의 반정렬 상태(느슨한 정렬 상태) 를 유지한다.  
      큰(작은) 값이 상위 레벨에 있고 작은(큰) 값이 하위 레벨에 있다는 정도이며,  
      좌우 자식의 대소비교는 하지 않는다.
    - 힙 트리에서는 중복된 값을 허용한다.
    - 계산 편의를 위해 인덱스는 1부터 사용한다. (parent: x, left: 2x, right: 2x+1)
