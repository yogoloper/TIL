from typing import List, Optional

# Definition for singly-linked list.
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
        
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = root = ListNode(None)
        
        while head:
            while ans.next and ans.next.val < head.val:
                ans = ans.next
            
            ans.next, head.next, head = head, ans.next, head.next

            ans = root
        return ans.next


# head = [-1,5,3,4,0]
linkedList = LinkedList()
linkedList.append(-1)
linkedList.append(5)
linkedList.append(3)
linkedList.append(4)
linkedList.append(0)
head = linkedList.head

o = Solution()
o.insertionSortList(head)