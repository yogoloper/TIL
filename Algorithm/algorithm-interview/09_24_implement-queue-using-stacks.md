# 스택을 이용한 큐 구현

<!-- TOC -->

- [스택을 이용한 큐 구현](#%EC%8A%A4%ED%83%9D%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%9C-%ED%81%90-%EA%B5%AC%ED%98%84)
  - [문제](#%EB%AC%B8%EC%A0%9C)
  - [예시](#%EC%98%88%EC%8B%9C)
  - [숙고 1](#%EC%88%99%EA%B3%A0-1)
  - [코드 1](#%EC%BD%94%EB%93%9C-1)

<!-- /TOC -->

## 문제
- https://leetcode.com/problems/implement-queue-using-stacks/
- 2개의 스택만 사용하여 FIFO 대기열을 구현하여라.  
  일반 큐의 모든 기능(push(), pop(), peek(), empty())을 구현하여라.
- MyQueue 클래스를 구현하여라.
 - void push(int x) 요소 x를 큐 뒤쪽으로 푸시한다.
 - int pop() 큐의 앞쪽에서 요소를 제거하고 반환한다.
 - int peek() 큐의 맨 앞에 있는 요소를 반환한다.
 - boolean empty() 대기열이 비어 있으면 true를 반환하고 그렇지 않으면 false를 반환한다.


## 예시
``` python
Example 1:
Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]

Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
```
## 숙고 1
- 배열 두 개를 활용해서 하나는 입력용 하나는 출력용으로 사용
- Push가 들어오면 입력 배열에 추가한다.
- 출력 요청이 들어오고 출력 배열의 요소가 존재한다면 pop()  
  비어있다면 입력 배열을 입력 순서대로 출력 배열에 복사하고 출력 배열 pop()


## 코드 1
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/09_24_implement-queue-using-stacks_01.py  
``` python
class MyQueue:
  
    def __init__(self):
        # 입력용 배열
        self.input = []
        # 출력용 배열
        self.output = []
        
    def push(self, x: int) -> None:
        # 입력 배열에 요소 삽입
        self.input.append(x)

    def pop(self) -> int:
        # peek()를 통해 첫 요소를 반환 및 출력 배열 재배열
        self.peek()
        return self.output.pop()

    # 첫 요소 찾기 위해 출력 배열을 통해 재배열 
    def peek(self) -> int:
        # 출력 배열이 비어있으면
        if not self.output:
            # 입력 배열의 요소를 역순으로 꺼내
            # 출력 배열에 차례로 입력
            while self.input:
                self.output.append(self.input.pop())
        # 출력 배열의 마지막 요소에 입력 배열의 첫 요소가 들어가 있음
        return self.output[-1]

    def empty(self) -> bool:
        return self.input == [] and self.output == []

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```
