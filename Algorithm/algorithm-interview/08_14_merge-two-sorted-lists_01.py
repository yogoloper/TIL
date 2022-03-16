from curses.ascii import SO
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        result = ListNode(0)
        
        if not list1:
            return list2
        elif not list2:
            return list1
        elif not list1 and not list2:
            return None
         
        if list1.val <= list2.val:
            result.val = list1.val
            list1 = list1.next
        else:
            result.val = list2.val
            list2 = list2.next
        
        temp = result
        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = ListNode(list1.val)
                list1 = list1.next
            else:
                temp.next = ListNode(list2.val)
                list2 = list2.next
            temp = temp.next
        if list1:
            temp.next = list1
        else:
            temp.next = list2
        
        return result
        
linkedList = LinkedList()
linkedList.append(1)
linkedList.append(2)
linkedList.append(4)

linkedList2 = LinkedList()
linkedList2.append(1)
linkedList2.append(3)
linkedList2.append(4)

o = Solution()
print(o.mergeTwoLists(linkedList.head, linkedList2.head))