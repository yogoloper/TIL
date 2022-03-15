# 원형 큐 디자인

<!-- TOC -->

- [원형 큐 디자인](#%EC%9B%90%ED%98%95-%ED%81%90-%EB%94%94%EC%9E%90%EC%9D%B8)
  - [문제](#%EB%AC%B8%EC%A0%9C)
  - [예시](#%EC%98%88%EC%8B%9C)
  - [숙고 1](#%EC%88%99%EA%B3%A0-1)
  - [코드 1](#%EC%BD%94%EB%93%9C-1)
  - [결과](#%EA%B2%B0%EA%B3%BC)

<!-- /TOC -->

## 문제
- https://leetcode.com/problems/design-circular-queue/
- 원형 큐 구현을 설계하여라.  
  원형 큐는 FIFO 원리에 따라 연산을 수행하고  
  마지막 위치에 연결하여 원을 만드는 선형 데이터 구조이다.  
  링 버퍼라고도 부른다.
- 원형 큐의 장점으로 대기열의 앞공간을 사용할 수 있다.  
  일반적인 큐에서는 큐 앞에 공간이 있더라도  
  큐가 가득차면 다음 요소를 삽입 할 수 없다.
- MyCircularQueue 클래스 구현  
  - MyCircularQueue(k) 큐의 크기가 k가 되도록 객체를 초기화 한다.  
  - int Front() 대기열에서 앞 항목을 가져오고  
    큐가 비어 있으면 -1을 반환한다.
  - int Rear() 대기열에서 마지막 항목을 가져오고  
    큐가 비어 있으면 -1을 반환한다.
  - boolean enQueue(int value) 순환 대기열에 요소를 삽입하며 
    작업이 성공하면 true를 반환한다.
  - boolean deQueue() 순환 대기열에서 요소를 삭제하며  
    작업이 성공하면 true를 반환한다.
  - boolean isEmpty() 순환 대기열이 비어 있는지 여부를 확인한다.
  - boolean isFull() 순환 큐가 가득 찼는지 여부를 확인한다.
  - 프로그래밍 언어에서 기본 제공 대기열 데이터 구조를 사용하지 않고 문제를 해결해야 한다.


## 예시
``` python
Example 1:

Input
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]

Output
[null, true, true, true, false, 3, true, true, true, 4]

Explanation
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4
```
## 숙고 1
- 배열을 이용해서 원형큐를 구현하고자 한다.
- init  
  - 입력 받은 숫자를 큐(배열)의 크기로 하고 공간을 할당한다.  
  - 할당받은 공간에는 아무것도 없으므로 None으로 초기화 한다.  
  - Front, Rear 인덱스로 배열을 관리한다.
- enQueue  
  - isFull을 통해 배열이 가득 찼는지 확인한다.
  - 가득 차지 않았다면 입력받은 값을 rear가 가리키는 곳에 입력 한다.
  - Rear의 인덱스를 증가시킨다.
- deQueue  
  - isEmpty을 통해 베열이 비어있는지 확인한다.
  - 비어 있지 않다면 front를 통해 배열의 맨 앞 부분 값을 가져오고  
    배열의 해당 요소 값을 None으로 변경한다.
  - front의 인덱스를 증가시킨다.
- Front  
  - front의 인덱스 값을 가져온다.
- Rear  
  - rear 의 인덱스 값을 가져온다.
- isEmpty
  - front와 rear의 인덱스가 같고  
    queue[front] 가 None이면 True를 반환한다.
- isFull  
  - front와 rear의 인덱스가 같고  
    queue[front] 가 None이 아니면 True를 반환한다.
- 인덱스 관리
  - front와 rear의 인덱스는 증가만 할 수 있으며,  
    인덱스가 size 까지 증가할 경우 0으로 교체한다.


## 코드 1
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/09_25_design-circular-queue_01.py
``` python
class MyCircularQueue:
    # 생성자
    def __init__(self, k: int):
        # 배열 할당
        self.queue = [None] * k
        # 배열 사이즈
        self.size = k
        # front 인덱스
        self.front = 0
        # rear 인덱스
        self.rear = 0

    # 요소 삽입
    def enQueue(self, value: int) -> bool:
        # 큐가 가득 차있지 않을 때만 삽입 가능
        if self.isFull():
            return False
        else:
            # rear가 가리키는 곳에 값 입력
            self.queue[self.rear] = value
            # 요소를 넣어주었으므로 rear는 다음 인덱스를 가리킴
            self.rear += 1
            # rear가 큐 공간을 넘어가지 않게 처리
            if self.rear == self.size:
                self.rear = 0
            return True

    # 요소 제거
    def deQueue(self) -> bool:
        # 큐가 비어있지 않을 때만 제거 가능
        if self.isEmpty():
            return False
        else:
            # front가 가리키는 곳의 값을 None으로 저장
            self.queue[self.front] = None
            # 요소를 제거 하였으므로 front는 다음 인덱스를 카리김
            self.front += 1
            # front가 큐 공간을 넘어가지 않게 처리
            if self.front == self.size:
                self.front = 0
            return True

    # 첫 요소 값 찾기
    def Front(self) -> int:
        # 큐가 비어있지 않을 때만 찾기 가능
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.front]

    # 끝 요소 값 찾기
    def Rear(self) -> int:
        # 큐가 비어 있지 않을 경우에만 찾기 가능
        if self.isEmpty():
            return -1
        else:
            # rear 요소의 값은 rear가 가리키는 곳의 -1 번째 해당
            return self.queue[self.rear -1]
    
    # 큐가 비어 있는지 확인
    def isEmpty(self) -> bool:
        # front와 rear의 인덱스가 같고 front의 요소 값이 없다면 빈것으로 판단
        if self.front == self.rear and self.queue[self.front] is None:
            return True
        else:
            return False

    # 큐가 가득 차있는지 확인
    def isFull(self) -> bool:
        # front와 rear의 인덱스가 같고 front의 요소 값이 있다면 가득찬것으로 판단
        if self.front == self.rear and self.queue[self.rear] is not None:
            return True
        else:
            return False
```

## 결과
``` python
obj = MyCircularQueue(3) queue: [None, None, None] 
front 0 rear: 0 

enQueue(1) queue: [1, None, None] 
front 0 rear: 1 

enQueue(2) queue: [1, 2, None] 
front 0 rear: 2 

enQueue(3) queue: [1, 2, 3] 
front 0 rear: 0 

enQueue(4) queue: [1, 2, 3] 
front 0 rear: 0 

Rear() queue: [1, 2, 3] 
front 0 rear: 0
Rear() result: 3 

isFull() queue: [1, 2, 3] 
front 0 rear: 0
isFull() result: True 

deQueue() queue: [None, 2, 3] 
front 1 rear: 0 

enQueue(4) queue: [4, 2, 3] 
front 1 rear: 1 

Rear() queue: [4, 2, 3] 
front 1 rear: 1
Rear() result: 4 
```