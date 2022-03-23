# Definition for a binary tree node.
from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sorted_array_to_bst(lst):
    if not lst:
        return None

    mid = len(lst) // 2

    node = TreeNode(lst[mid])
    node.left = sorted_array_to_bst(lst[:mid])
    node.right = sorted_array_to_bst(lst[mid + 1:])

    return node

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        if not nums:
            return []
        
        root = sorted_array_to_bst(nums)
        return root

nums = [-10,-3,0,5,9]
o = Solution()
print(o.sortedArrayToBST(nums))