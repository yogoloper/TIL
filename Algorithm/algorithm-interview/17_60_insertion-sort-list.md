# 삽입 정렬 리스트

<!-- TOC -->

- [삽입 정렬 리스트](#%EC%82%BD%EC%9E%85-%EC%A0%95%EB%A0%AC-%EB%A6%AC%EC%8A%A4%ED%8A%B8)
  - [문제](#%EB%AC%B8%EC%A0%9C)
  - [에시](#%EC%97%90%EC%8B%9C)
  - [숙고 1](#%EC%88%99%EA%B3%A0-1)
  - [코드 1](#%EC%BD%94%EB%93%9C-1)

<!-- /TOC -->

## 문제
- 문제 : https://leetcode.com/problems/insertion-sort-list/
- 싱글 연결 리스트의 헤드가 주어지면 삽입 정렬을 사용하여 리스트를 정렬하고 헤드를 반환하여라.
- 삽입 정렬 알고리즘의 단계
  - 삽입 정렬은 반복될 때마다 하나의 입력 요소를 사용하고 정렬된 출력 목록을 늘린다.
  - 각 반복에서 삽입 정렬은 입력 데이터에서 하나의 요소를 제거하고  
    정렬된 목록 내에서 해당 요소가 속한 위치를 찾아 거기에 삽입한다.
  - 입력 요소가 남아 있지 않을 때까지 반복한다.
  
  다음은 삽입 정렬 알고리즘의 그래픽 예제이다.  
  부분적으로 정렬된 목록(검정색)은 처음에 목록의 첫 번째 요소만 포함한다.  
  하나의 요소(빨간색)가 입력 데이터에서 제거되고 각 반복과 함께 정렬된 목록에 제자리에 삽입된다.  
  ![](./images/17_60_insertion-sort-list_01.gif)

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
- 삽입 정렬은 첫 요소를 정렬된 상태로 취급하고  
  다음 요소부터 정렬된 상태의 리스트에서 자신의 자리를 찾아 삽입 하는 형태의 정렬이다.
- 리스트에서는 정렬된 리스트의 맨 뒤 인덱스부터 접근했지만,  
  싱글 연결 리스트이므로 앞의 요소들과 비교할 방법이 없으니 앞의 요소부터 next.val과 올라가며 비교하고자 한다.
- 그러려고 했지만 작성이 되지 않아 풀이를 봤다.
## 코드 1
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/17_60_insertion-sort-list_01.py
``` python
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # ans는 정렬이 완료된 대상, head는 정렬이 될 대상
        # root 는 ans를 다시 처음으로 돌릴때 사용
        ans = root = ListNode(None)
        
        # 정렬될 노드가 있을때까지 반복
        while head:
            # 비교할 완료된 대상이 남아있고, 
            # 비교할 값이 정렬될 값보다 작으면 다음 비교할 완료 대상을 가져온다.
            while ans.next and ans.next.val < head.val:
                ans = ans.next
            
            # 정렬될 리스트의 노드를 완료된 리스트에 연결하여 삽입하는 과정
            ans.next, head.next, head = head, ans.next, head.next

            # ans는 다시 처음으로 돌려보낸다.
            ans = root
        return ans.next
```