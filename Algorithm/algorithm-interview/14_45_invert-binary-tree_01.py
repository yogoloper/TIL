# Definition for a binary tree node.
from collections import deque
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        
        while q:
            node = q.popleft()
            
            if node:
                node.left, node.right = node.right, node.left
                
                q.append(node.left)
                q.append(node.right)
        
        return root

root = [4,2,7,1,3,6,9]
o = Solution()
print(o.invertTree(make_tree_by(root, 0)))