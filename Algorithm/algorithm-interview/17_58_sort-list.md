# 리스트 정렬

<!-- TOC -->

- [리스트 정렬](#%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%A0%95%EB%A0%AC)
  - [문제](#%EB%AC%B8%EC%A0%9C)
  - [에시](#%EC%97%90%EC%8B%9C)
  - [숙고 1](#%EC%88%99%EA%B3%A0-1)
  - [코드 1](#%EC%BD%94%EB%93%9C-1)

<!-- /TOC -->

## 문제
- 문제 : https://leetcode.com/problems/sort-list/
- 연결리스트의 헤드가 주어지면 오름차순으로 정렬된 리스트를 반환하여라.

## 에시
``` python
Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
```

## 숙고 1
- 제약 사항을 보면 NlogN의 시간복잡도 제약사항이 있는데, 내장함수가 NlgoN의 시간 복잡도를 갖는다. 연결 리스트를 리스트로 변경후 내장함수로 정렬하여 다시 연결 리스트로 반환하면 될 듯 하다.

## 코드 1
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/17_58_sort-list_01.py
``` python
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        node = head
        
        while node:
            arr.append(node.val)
            node = node.next
            
        arr = sorted(arr)
        
        node = head
        for i in arr:
            node.val = i
            node = node.next
        
        return head
```