# 두 정렬 리스트 병합

<!-- TOC -->

- [두 정렬 리스트 병합](#%EB%91%90-%EC%A0%95%EB%A0%AC-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EB%B3%91%ED%95%A9)
  - [문제](#%EB%AC%B8%EC%A0%9C)
  - [예시](#%EC%98%88%EC%8B%9C)
  - [숙고 1](#%EC%88%99%EA%B3%A0-1)
  - [코드 1](#%EC%BD%94%EB%93%9C-1)

<!-- /TOC -->

## 문제
- https://leetcode.com/problems/merge-two-sorted-lists/
- 두 개의 정렬된 연결 리스트의 헤드가 입력된다.
- 두 개의 연결 리스트를 정렬된 하나의 정렬된 연결 리스트로 만들어 헤드를 반환하여라.
  
## 예시
``` python
Example 1:  
Input: list1 = [1,2,4], list2 = [1,3,4]  
Output: [1,1,2,3,4,4]  

Example 2:  
Input: list1 = [], list2 = []  
Output: []  

Example 3:  
Input: list1 = [], list2 = [0]  
Output: [0]  
```
## 숙고 1
- 두 리스트를 각각 배열로 변환 후 병합, 정렬을 한 다음에 다시 리스트로 만들어서 반환하면 어떨까?  
  해보지 않아도 O(3N)이 나올것 같다.
- 그러면 한 리스트 마지막노드의 next를 다른 노드의 head를 가리켜서 합친 후에  
  배열로 변환, 정렬 -> 다시 리스트로 변환한다면?  
  O(2N)으로 줄겠지
- 하나의 반복문에서 진행 할 수는 없을까?  
  더미 노드를 하나 만들고 두 연결 리스트의 첫 값을 비교해서 작은 쪽의 값을 더미 노드에 넣어준다.  
  반복문 안에서 같이 노드들을 이동하며 비교하고  
  작은 값의 노드를 더미 리스트에 리스트에 넣어준다.
- 첫 번째 리스트가 길 경우에는 정렬 다 하고서 두 번째 리스트 마지막에 연결하고  
  두 번째 리스트가 길 경우에는 나머지 요소들을 메인 리스트 마지막에 연결한다.
  
## 코드 1
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/08_14_merge-two-sorted-lists_01.py  
``` python
class Solution:
    class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 더미의 헤드 노드
        result = ListNode(0)
        
        # 리스트들이 비어 있을경우 처리
        if not list1:
            return list2
        elif not list2:
            return list1
        elif not list1 and not list2:
            return None
         
        # 더미에 첫 값을 넣어주기 위해 비교
        if list1.val <= list2.val:
            result.val = list1.val
            list1 = list1.next
        else:
            result.val = list2.val
            list2 = list2.next
        
        # 헤드를 기록해야하므로 임시 더미를 통해 노드를 연결
        temp = result
        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = ListNode(list1.val)
                list1 = list1.next
            else:
                temp.next = ListNode(list2.val)
                list2 = list2.next
            temp = temp.next
        
        # 정렬을 마치고 남은 연결 리스트를 뒤에 붙여준다.
        if list1:
            temp.next = list1
        else:
            temp.next = list2
        
        return result
```
