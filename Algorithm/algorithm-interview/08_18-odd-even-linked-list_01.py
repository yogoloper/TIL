from curses.ascii import SO
from platform import node
from typing import Optional


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

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
      
linkedList = LinkedList()
linkedList.append(1)
linkedList.append(2)
linkedList.append(3)
linkedList.append(4)
linkedList.append(5)

head = linkedList.head

o = Solution()
o.oddEvenList(head)
 