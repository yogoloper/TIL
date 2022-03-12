# 홀짝 연결 리스트

<!-- TOC -->

- [홀짝 연결 리스트](#%ED%99%80%EC%A7%9D-%EC%97%B0%EA%B2%B0-%EB%A6%AC%EC%8A%A4%ED%8A%B8)
  - [문제](#%EB%AC%B8%EC%A0%9C)
  - [예시](#%EC%98%88%EC%8B%9C)
  - [숙고 1](#%EC%88%99%EA%B3%A0-1)
  - [숙고 2](#%EC%88%99%EA%B3%A0-2)
  - [코드 1](#%EC%BD%94%EB%93%9C-1)

<!-- /TOC -->

## 문제
- https://leetcode.com/problems/odd-even-linked-list/
- 하나의 연결 리스트의 헤드가 주어지면 ***홀수별/짝수별 인덱스***를 가진 노드를 그룹화하고  
  재정렬된 리스트를 반환하여라.  
  -> 노드의 값이 아닌 인덱스의 홀짝으로 그룹화 하여라.
- 첫 번째 노드는 홀수로 간주되고, 두 번째 노드는 짝수로 간주된다.
- 짝수/홀수 그룹의 내부 순서는 입력 받은 순서를 유지해야 한다.
- O(1) 추가 공간 복잡도와 O(n) 시간 복잡도 문제를 해결해야 한다.

## 예시
``` python
Example 1:  
Input: head = [1,2,3,4,5]  
Output: [1,3,5,2,4]  

Example 2:  
Input: head = [2,1,3,5,6,4,7]  
Output: [2,3,6,7,1,5,4]  
```
## 숙고 1
- 헤드의 값이 홀수 인지 짝수 인지를 구분할 수 있는 변수를 하나 선언한다.
- 홀수 그룹을 메인 리스트로 정한다.
- 반복문을 돌면서 노드별로 홀수 짝수를 구분하여  
  홀수일 경우 메인 리스트에 남겨두고  
  짝수일 경우 별도 리스트로 연결해주고  
  메인 리스트에서는 다음 노드를 확인한다.
- 별도로 리스트를 만들어진 짝수 리스트의 헤드를 가져와서
- 홀짝 구분변수로 분할된 리스트들을 순서에 맞게 연결하고 반환한다.
- ~~시공간이 뒤틀릴것만 같다..~~
- 이런.. 문제 이해를 잘못했다..

## 숙고 2
- 두 번째 노드를 짝수 헤드 변수에 저장한다.
- 반복문을 돌면서 노드를 두 번씩 접근하고  
  짝수번 노드와 홀수번 노드가 모두 존재 할때까지 반복한다.
  짝수 노드는 짝수번째 노드를 가리키고 -> 
  홀수 노드는 홀수번째 노드를 가리킨다.
- 짝수번 노드만 남게 된 경우 그룹에 맞게 들어가 있을 것이므로  
  추가로 조건을 건드릴 필요가 없다.
- 홀수 그룹 마지막에 짝수 그룹의 헤드를 연결한다.


## 코드 1
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/08_18-odd-even-linked-list_01.py  

``` python
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        # 메인 리스트가 될 첫 번째 홀수 노드
        odd_node = head
        
        # 짝수 노드들을 접근할 노드
        even_node = odd_node.next
        # 마지막에 홀수 리스트 뒤에 붙여주기 위해 짝수 리스트의 헤드 노드를 저장
        first_even_node = odd_node.next
        
        # 반복문 한 번에 두 노드를 건너뛰기 때문에
        # 현재 노드(짝수)와 다음 노드(홀수) 둘다 존재할 때까지 반복
        while even_node and even_node.next:
            # 홀수 노드는 현재 짝수 노드의 다음 노드를 가리키고
            # 짝수 노드는 현재 짝수 노드의 다다음 노드를 가리킴
            odd_node.next = even_node.next
            even_node.next = even_node.next.next

            # 노드를 두 단계씩 접근
            odd_node = odd_node.next
            even_node = even_node.next

        # 홀수 리스트 마지막에 짝수 리스트의 헤드를 연결
        odd_node.next = first_even_node
        return head
```

