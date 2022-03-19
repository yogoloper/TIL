# [항해99 6기] 알고리즘 주간(2) - 2022.03.12

<!-- TOC -->

- [[항해99 6기] 알고리즘 주간2 - 2022.03.12](#%ED%95%AD%ED%95%B499-6%EA%B8%B0-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%A3%BC%EA%B0%842---20220312)
- [Learned](#learned)
  - [연결리스트](#%EC%97%B0%EA%B2%B0%EB%A6%AC%EC%8A%A4%ED%8A%B8)
    - [배열 vs 연결리스트](#%EB%B0%B0%EC%97%B4-vs-%EC%97%B0%EA%B2%B0%EB%A6%AC%EC%8A%A4%ED%8A%B8)
    - [클래스](#%ED%81%B4%EB%9E%98%EC%8A%A4)
    - [구현](#%EA%B5%AC%ED%98%84)
  - [역순 연결 리스트](#%EC%97%AD%EC%88%9C-%EC%97%B0%EA%B2%B0-%EB%A6%AC%EC%8A%A4%ED%8A%B8)
  - [두 정렬 리스트 병합](#%EB%91%90-%EC%A0%95%EB%A0%AC-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EB%B3%91%ED%95%A9)
  - [홀짝 연결 리스트](#%ED%99%80%EC%A7%9D-%EC%97%B0%EA%B2%B0-%EB%A6%AC%EC%8A%A4%ED%8A%B8)
- [Retrospect](#retrospect)

<!-- /TOC -->

# Learned
- 연결리스트
- 역순 연결 리스트
- ~~두 정렬 리스트 병합~~
- 홀짝 연결 리스트

## 연결리스트
### 배열 vs 연결리스트
- 배열 : 파이썬의 리스트, 접근 쉬움, 삽입 어려움  
    - 원소 조회 : O(1)
    - 중간에 삽입 삭제 : O(N)
    - 데이터 추가 : 데이터 추가 시 모든 공간이 다 차버렸다면 새로운 메모리 공간을 할당받아야 한다 
    - 정리 : 데이터에 접근하는 경우가 빈번하다면 Array를 사용하자
- 연결리스트 : 직접 구현, 접근 어려움, 삽입 쉬움
    - 원소 조회 : O(N)
    - 중간에 삽입 삭제 : O(1)
    - 데이터 추가 : 모든 공간이 다 찼어도 맨 뒤의 노드만 동적으로 추가하면 된다
    - 정리 : 삽입과 삭제가 빈번하다면 연결리스트를 사용하는 것이 더 좋다

### 클래스
```python
class Person:
    def __init__(self, name):
        self.name = name

    def sayhello(self, to):
        print(f"hello {to}, I'm {self.name}")

rtan = Person("rtanny")
rtan.sayhello("hanghae")
```

### 구현
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = ListNode(val, None)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = ListNode(val, None)
```

## 역순 연결 리스트
- 문제 : https://leetcode.com/problems/reverse-linked-list/submissions/
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/08_15_reverse-linked-list.md  

## 두 정렬 리스트 병합
- 문제 : https://leetcode.com/problems/merge-two-sorted-lists/
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/08_14_merge-two-sorted-lists.md  

## 홀짝 연결 리스트
- 문제 : https://leetcode.com/problems/odd-even-linked-list/
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/08_18-odd-even-linked-list.md  

# Retrospect
학부때는 자료구조/알고리즘을 그렇게 어려워했는데  
이렇게 공부하다보니 재미있다.  

할당된 문제를 그날 다 풀지는 못하고 있는데  
시간 할당을 다시 해봐야 겠다.

조금씩이나마 굳었던 머리가 돌아가는 것 같다.  
~~데굴데굴~~