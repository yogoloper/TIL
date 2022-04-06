# [항해99 6기] 알고리즘 주간(26) - 2022.04.05

<!-- TOC -->

- [[항해99 6기] 알고리즘 주간26 - 2022.04.05](#%ED%95%AD%ED%95%B499-6%EA%B8%B0-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%A3%BC%EA%B0%8426---20220405)
- [Learned](#learned)
  - [동적 계획법Dynamic Programming](#%EB%8F%99%EC%A0%81-%EA%B3%84%ED%9A%8D%EB%B2%95dynamic-programming)
  - [DP로 피보나치 수열 구현](#dp%EB%A1%9C-%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98-%EC%88%98%EC%97%B4-%EA%B5%AC%ED%98%84)
  - [[이코테]정수 삼각형 - 더 공부하기](#%EC%9D%B4%EC%BD%94%ED%85%8C%EC%A0%95%EC%88%98-%EC%82%BC%EA%B0%81%ED%98%95---%EB%8D%94-%EA%B3%B5%EB%B6%80%ED%95%98%EA%B8%B0)
  - [[이코테]퇴사 - 더 공부하기](#%EC%9D%B4%EC%BD%94%ED%85%8C%ED%87%B4%EC%82%AC---%EB%8D%94-%EA%B3%B5%EB%B6%80%ED%95%98%EA%B8%B0)
  - [[이코테]효율적인 화폐 구성 - 더 공부하기](#%EC%9D%B4%EC%BD%94%ED%85%8C%ED%9A%A8%EC%9C%A8%EC%A0%81%EC%9D%B8-%ED%99%94%ED%8F%90-%EA%B5%AC%EC%84%B1---%EB%8D%94-%EA%B3%B5%EB%B6%80%ED%95%98%EA%B8%B0)
  - [[이코테]개미 전사 - 더 공부하기](#%EC%9D%B4%EC%BD%94%ED%85%8C%EA%B0%9C%EB%AF%B8-%EC%A0%84%EC%82%AC---%EB%8D%94-%EA%B3%B5%EB%B6%80%ED%95%98%EA%B8%B0)
  - [[이코테]바닥 공사 - 더 공부하기](#%EC%9D%B4%EC%BD%94%ED%85%8C%EB%B0%94%EB%8B%A5-%EA%B3%B5%EC%82%AC---%EB%8D%94-%EA%B3%B5%EB%B6%80%ED%95%98%EA%B8%B0)
- [Retrospect](#retrospect)

<!-- /TOC -->

# Learned
- 동적 계획법(Dynamic Programming)
- 피보나치 수열
- [이코테]정수 삼각형
- [이코테]퇴사
- [이코테]효율적인 화폐 구성
- [이코테]개미 전사
= [이코테]바닥 공사

## 동적 계획법(Dynamic Programming)
- 큰 문제를 작은 문제로 쪼개서 그 답을 저장해두고 재활용한다.  
  -> 겹치는 부분 문제(Overlapping Subproblem)을 메모이제이션(Memoication)한다.

## DP로 피보나치 수열 구현
- 일반 적인 피보나치
``` python
def fibo(n):
    if n in [1, 2]:
        return 1
    return fibo(n-1) + fibo(n-2)

assert fibo(10) == 55
assert fibo(100) == 354224848179261915075 # 안끝난다.
```
- DP 피보나치  
  -> 메모를 통해서 작게 처리된 부분들을 기억시킴
``` python
memo = {1: 1, 2: 1}

def fibo(n):
    if n in memo:
        return memo[n]
    memo[n] = fibo(n - 1) + fibo(n - 2)
    return memo[n]

assert fibo(10) == 55
assert fibo(100) == 354224848179261915075
```

## [이코테]정수 삼각형 - 더 공부하기
- 문제 : https://www.acmicpc.net/problem/1932
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/pyhon-for-coding-test/16_32.md  

## [이코테]퇴사 - 더 공부하기
- 문제 : https://www.acmicpc.net/problem/14501
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/pyhon-for-coding-test/16_33.md  

## [이코테]효율적인 화폐 구성 - 더 공부하기
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/pyhon-for-coding-test/08_05.md  

## [이코테]개미 전사 - 더 공부하기
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/pyhon-for-coding-test/08_03.md  

## [이코테]바닥 공사 - 더 공부하기
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/pyhon-for-coding-test/08_04.md  

# Retrospect
동적 계획법.. 유형이 딱 정해지지도 않고 점화식을 찾아내기도 어렵다..