# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def make_tree_by(lst, idx):
    parent = None
    if idx < len(lst):
        value = lst[idx]
        if value is None:
            return

        parent = TreeNode(value)
        parent.left = make_tree_by(lst, 2 * idx + 1)
        parent.right = make_tree_by(lst, 2 * idx + 2)

    return parent

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None
        if root1 is None and root2:
            return root2
        elif root1 and root2 is None:
            return root1
          
        ans = TreeNode()
        ans.val = root1.val + root2.val
        ans.left = self.mergeTrees(root1.left, root2.left)
        ans.right = self.mergeTrees(root1.right, root2.right)

        return ans

root1 = [1,3,2,5]
root2 = [2,1,3,None,4,None,7]
o = Solution()
o.mergeTrees(root1, root2)