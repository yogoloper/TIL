from typing import Optional

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




linkedlist = LinkedList()
linkedlist.append(4)
linkedlist.append(2)
linkedlist.append(1)
linkedlist.append(3)

o = Solution()
o.sortList(linkedlist.head)