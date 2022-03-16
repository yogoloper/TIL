# [항해99 6기] 알고리즘 주간(6) - 2022.03.16

<!-- TOC -->

- [[항해99 6기] 알고리즘 주간6 - 2022.03.16](#%ED%95%AD%ED%95%B499-6%EA%B8%B0-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%A3%BC%EA%B0%846---20220316)
- [Learned](#learned)
  - [해시 테이블](#%ED%95%B4%EC%8B%9C-%ED%85%8C%EC%9D%B4%EB%B8%94)
    - [해시 함수](#%ED%95%B4%EC%8B%9C-%ED%95%A8%EC%88%98)
    - [좋은 성능의 해시 함수](#%EC%A2%8B%EC%9D%80-%EC%84%B1%EB%8A%A5%EC%9D%98-%ED%95%B4%EC%8B%9C-%ED%95%A8%EC%88%98)
    - [로드 팩터](#%EB%A1%9C%EB%93%9C-%ED%8C%A9%ED%84%B0)
    - [충돌 대처 방법](#%EC%B6%A9%EB%8F%8C-%EB%8C%80%EC%B2%98-%EB%B0%A9%EB%B2%95)
    - [구현](#%EA%B5%AC%ED%98%84)
  - [해시맵 디자인](#%ED%95%B4%EC%8B%9C%EB%A7%B5-%EB%94%94%EC%9E%90%EC%9D%B8)
  - [보석과 돌](#%EB%B3%B4%EC%84%9D%EA%B3%BC-%EB%8F%8C)
  - [중복 문자가 없는 가장 긴 부분 문자열](#%EC%A4%91%EB%B3%B5-%EB%AC%B8%EC%9E%90%EA%B0%80-%EC%97%86%EB%8A%94-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EB%B6%80%EB%B6%84-%EB%AC%B8%EC%9E%90%EC%97%B4)
  - [상위 K 빈도 요소](#%EC%83%81%EC%9C%84-k-%EB%B9%88%EB%8F%84-%EC%9A%94%EC%86%8C)
  - [[boj] 수 찾기](#boj-%EC%88%98-%EC%B0%BE%EA%B8%B0)
  - [[boj] 비밀번호 찾기](#boj-%EB%B9%84%EB%B0%80%EB%B2%88%ED%98%B8-%EC%B0%BE%EA%B8%B0)
- [Retrospect](#retrospect)

<!-- /TOC -->

# Learned
- 해시맵 디자인
- 해시 테이블
- 보석과 돌
- 중복 문자가 없는 가장 긴 부분 문자열
- 상위 K 빈도 요소
- [boj] 수 찾기
- [boj] 비밀번호 찾기

## 해시 테이블
- 키를 값에 매핑할 수 있는 구조인, 연관 배열 추상 자료형(ADT)를 구현하는 자료구조이다.
- 대부분의 연산이 분할 상환 분석에 따른 시간복잡도가 O(1)  
 -> 데이터 양에 관계 없이 빠른 성능을 기대할 수 있다.

### 해시 함수
- 임의 크기 데이터를 고정 크기 값으로 매핑하는데 사용하는 함수
- 해시 테이블을 인덱싱하기 위해 해시 함수를 사용하는 것을 **해싱**이라고 한다.

### 좋은 성능의 해시 함수
- 해시 함수 값 충돌의 최소화
- 쉽고 빠른 연산
- 해시 테이블 전체에 해시 값이 균일하게 분포
- 사용할 키의 모든 정보를 이용하여 해싱
- 해시 테이블 사용 효율이 높을 것

### 로드 팩터
- 해시 테이블에 저장된 데이터 개수 n을 버킷의 개수 k로 나눈 것이다.  
 -> 공간이 얼마나 차있나..

### 충돌 대처 방법
- 개별 체이닝
- 오픈 어드레싱

### 구현
```python
from hashtable.structures import MyHashTable

def test_hashtable():
    ht = MyHashTable()

    ht.put(1, 1)
    ht.put(2, 2)
    assert ht.get(1) == 1
    assert ht.get(3) == -1

    ht.put(2, 1)
    assert ht.get(2) == 1

    ht.remove(2)
    assert ht.get(2) == -1

def test_birthday_problem():
    import random
    TRIALS = 100000
    same_birthdays = 0

    for _ in range(TRIALS):
        birthdays = []
        for i in range(23):
            birthday = random.randint(1, 365)
            if birthday in birthdays:
                same_birthdays += 1
                break
            birthdays.append(birthday)

    print(f"{same_birthdays / TRIALS * 100}%")

if __name__ == "__main__":
    test_birthday_problem()
    test_hashtable()
```
## 해시맵 디자인
- 문제 : https://leetcode.com/problems/design-hashmap/
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/11_28_design-hashmap.md  

## 보석과 돌
- 문제 : https://leetcode.com/problems/jewels-and-stones/
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/11_29_jewels-and-stones.md  

## 중복 문자가 없는 가장 긴 부분 문자열
- 문제 : https://leetcode.com/problems/longest-substring-without-repeating-characters/
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/11_30_longest-substring-without-repeating-characters.md  

## 상위 K 빈도 요소
- 문제 : https://leetcode.com/problems/top-k-frequent-elements/
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/11_31_top-k-frequent-elements.md  

## [boj] 수 찾기
- 문제 : https://www.acmicpc.net/problem/1920
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/Baekjoon-Online-Judge/1920.md  

## [boj] 비밀번호 찾기
- 문제 : https://www.acmicpc.net/problem/17219
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/Baekjoon-Online-Judge/17219.md  

# Retrospect
파이썬에서 제공하는 함수들을 먼저 공부해봐야 할 것 같다.  
그 함수들을 나는 바로 구현 할 수 있을지도 해봐야겠다.  

현재 알고리즘 외에도 컴퓨터과학 스터디도 진행중인데  
처음에는 웹개발자가 이런거까지 봐야 하나 싶다가도  
통신이 점점 발전하는 과정을 보는데 흥미로운 것 같다.