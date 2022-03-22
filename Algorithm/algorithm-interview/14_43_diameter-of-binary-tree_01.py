from typing import Optional

# Definition for a binary tree node.
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
    longest: int = 0
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1
            # 왼쪽, 오른쪽의 각 리프 노드까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 가장 긴 경로
            self.longest = max(self.longest, left + right + 2)
            #상태값
            return max(left, right) + 1
        
        dfs(root)
        return self.longest

root = [1,
        2, 3,
        4,5, None,None,
        6,7,8,9, None,None,None,None,
        None,None,None,None,None,None,None,10, None,None,None,None,None,None,None,None]
o = Solution()
print(o.diameterOfBinaryTree(make_tree_by(root, 0)))