# Definition for a binary tree node.
from collections import deque
import collections
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        root = make_tree_by(root, 0)
        if not root:
            return 0
  
        q = deque([root])
        depth = 0

        while q:
            depth += 1
            for _ in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

          
        return depth
      

root = [3,9,20,None,None,15,7]
o = Solution()
print(o.maxDepth(root))