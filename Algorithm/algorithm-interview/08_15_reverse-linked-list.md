# 역순 연결 리스트

<!-- TOC -->

- [역순 연결 리스트](#%EC%97%AD%EC%88%9C-%EC%97%B0%EA%B2%B0-%EB%A6%AC%EC%8A%A4%ED%8A%B8)
  - [문제](#%EB%AC%B8%EC%A0%9C)
  - [예시](#%EC%98%88%EC%8B%9C)
  - [숙고 1](#%EC%88%99%EA%B3%A0-1)
  - [코드 1](#%EC%BD%94%EB%93%9C-1)
  - [숙고 2](#%EC%88%99%EA%B3%A0-2)
  - [코드 2](#%EC%BD%94%EB%93%9C-2)

<!-- /TOC -->


## 문제
- https://leetcode.com/problems/reverse-linked-list/
- 단일 연결 리스트의 헤를 받아 목록을 뒤집어 역정렬하여 반환하여라.  

## 예시
- Example 1:  
  Input: head = [1,2,3,4,5]  
  Output: [5,4,3,2,1]  

- Example 2:  
  Input: head = [1,2]  
  Output: [2,1]  

- Example 3:  
  Input: head = []  
  Output: []  

## 숙고 1
- 새 연결 리스트를 만들어서 기존의 연결 리스에 역순으로 넣어주면 안될까?

## 코드 1
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/08_15_reverse-linked-list_01.py  

- 전달 받은 리스트를로 배열에 하나씩 넣고  
  새로 만든 리스트에 차례로 넣어주었다  
  풀기는 했지만 반복분을 두 번 쓰는게 찜찜하다 -> O(2N)

``` python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverse = LinkedList()
        arr = []

        node = head

        while node:
            arr.append(node.val)
            node = node.next

        while arr:
            reverse.append(arr.pop())

        return reverse.head
```

## 숙고 2
- 연결 리스트의 노드들이 가리키는 방향을 바꾸면 되지 않을까?
- None <- 1 2 -> 3 -> 4 -> 5 -> None  
  None <- 1 <- 2 3 -> 4 -> 5 -> None  
  None <- 1 <- 2 < -3 4 -> 5 -> None  
  None <- 1 <- 2 <- 3 <- 4 5 -> None  
  None <- 1 <- 2 <- 3 <- 4 <- 5 None  


## 코드 2
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/08_15_reverse-linked-list_02.py  

``` python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        node = head
        # 현재 노드를 저장해서 다음 노드가 현재 노드를 가리키기 위해서 선언
        prev = None
        
        while node:
            # 다음 작업을 할 노드를 잃지 않기 위해 저장해두고
            next = node.next
            # 현재 노드의 다음 값을 이전 노드로 가리키도록 변경
            # 헤드 노드의 다음 값을 None 으로 변경하는 것으로 시작
            node.next = prev 
            
            # next가 변경된 현재 노드를 
            # 다음 노드의 이전 노드로 가리키기 위해 저장
            prev = node
            # while 처음에 저장해 두었던 다음 작업할 노드를 가져옴
            node = next

        return 
```