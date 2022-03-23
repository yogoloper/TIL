from collections import deque


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

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = []
        
        q = deque([root])
        
        while q:
            node = q.popleft()
            if node:
                ans.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                ans.append('None')

        return ' '.join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split()
        
        if nodes[0] == 'None':
            return None
        
        root = TreeNode(int(nodes[0]))
        q = deque([root])
        index = 1
        
        while q:
            node = q.popleft()
            if nodes[index] != 'None':
                node.left = TreeNode(int(nodes[index]))
                q.append(node.left)
            index += 1
            
            if nodes[index] != 'None':
                node.right = TreeNode(int(nodes[index]))
                q.append(node.right)
            index += 1
            
        return root

# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
root = [1,2,3,None,None,4,5]
# root = []


# ser.serialize(make_tree_by(root, 0))
              
ans = deser.deserialize(ser.serialize(make_tree_by(root, 0)))