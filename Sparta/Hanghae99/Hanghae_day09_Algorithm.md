# [항해99 6기] 알고리즘 주간(5) - 2022.03.15

<!-- TOC -->

- [[항해99 6기] 알고리즘 주간5 - 2022.03.15](#%ED%95%AD%ED%95%B499-6%EA%B8%B0-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%A3%BC%EA%B0%845---20220315)
- [Learned](#learned)
  - [큐](#%ED%81%90)
    - [구현](#%EA%B5%AC%ED%98%84)
  - [deque](#deque)
  - [스택을 이용한 큐 구현](#%EC%8A%A4%ED%83%9D%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%9C-%ED%81%90-%EA%B5%AC%ED%98%84)
  - [원형 큐 디자인](#%EC%9B%90%ED%98%95-%ED%81%90-%EB%94%94%EC%9E%90%EC%9D%B8)
  - [[boj] 카드2](#boj-%EC%B9%B4%EB%93%9C2)
  - [[boj] 프린터큐](#boj-%ED%94%84%EB%A6%B0%ED%84%B0%ED%81%90)
- [Retrospect](#retrospect)

<!-- /TOC -->

# Learned
- 큐
- 스택을 이용한 큐 구현
- 원형 큐 디자인
- [boj] 카드2
- [boj] 프린터큐

## 큐
- 컴퓨터의 기본적인 자료 구조의 한가지로,  
  먼저 집어 넣은 데이터가 먼저 나오는 FIFO(First In First Out)구조로 저장하는 형식

### 구현
```python
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class Queue:
    def __init__(self):
        self.front = None

    def push(self, value):
        if not self.front:
            self.front = Node(value, None)
            return

        node = self.front
        while node.next:
            node = node.next
        node.next = Node(value, None)

    def pop(self):
        if not self.front:
            return None

        node = self.front
        self.front = self.front.next
        return node.item

    def is_empty(self):
        return self.front is None

def test_queue():
    queue = Queue()

    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    queue.push(5)

    assert queue.pop() == 1
    assert queue.pop() == 2
    assert queue.pop() == 3
    assert queue.pop() == 4
    assert queue.pop() == 5
    assert queue.pop() is None
    assert queue.is_empty()

test_queue()
```

## deque
- https://docs.python.org/ko/3/library/collections.html?highlight=deque#collections.deque
- deque 빠른 이유  
  중간의 값을 넣고 빼고 하는게 없다.
  참고 : https://wiki.python.org/moin/TimeComplexity
  
## 스택을 이용한 큐 구현
- 문제 : https://leetcode.com/problems/implement-queue-using-stacks/
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/09_24_implement-queue-using-stacks.md  

## 원형 큐 디자인
- 문제 : https://leetcode.com/problems/design-circular-queue/
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/09_25_design-circular-queue.md  

## [boj] 카드2
- 문제 : https://www.acmicpc.net/problem/2164
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/Baekjoon-Online-Judge/2164.md  

## [boj] 프린터큐
- 문제 : https://www.acmicpc.net/problem/1966
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/Baekjoon-Online-Judge/1966.md  

# Retrospect
확실히 큐가 스택보다 편한 것 같다.  
근데 문제를 풀면 풀수록 자괴감이 드는것은 기분탓인가