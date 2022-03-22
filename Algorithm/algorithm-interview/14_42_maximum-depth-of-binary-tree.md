# 이진 트리의 최대 깊이

<!-- TOC -->

- [이진 트리의 최대 깊이](#%EC%9D%B4%EC%A7%84-%ED%8A%B8%EB%A6%AC%EC%9D%98-%EC%B5%9C%EB%8C%80-%EA%B9%8A%EC%9D%B4)
  - [문제](#%EB%AC%B8%EC%A0%9C)
  - [예시](#%EC%98%88%EC%8B%9C)
  - [숙고 1](#%EC%88%99%EA%B3%A0-1)
  - [코드 1](#%EC%BD%94%EB%93%9C-1)

<!-- /TOC -->

## 문제
- 문제 : https://leetcode.com/problems/maximum-depth-of-binary-tree/
- 이진 트리의 루트가 주어지면 최대 깊이를 반환하여라.  
  이진 트리의 최대 깊이는 루트 노드에서 가장 먼 잎의 노드까지 가장 긴 경로를 따라 있는 노드의 수이다.
  
## 예시
![Example 1](./images/14_42_maximum-depth-of-binary-tree_01.jpeg)
``` python
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
```

## 숙고 1
- 루트부터 리프노드까지의 최대 노드수를 높이로 반환해아 한다.
  -> 레벨의 수를 반환하여라와 같은 의미


## 코드 1
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/14_42_maximum-depth-of-binary-tree_01.py
``` python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 리스트를 이진 트리로 변환해주는 함수
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
        # 리스트를 트리로 변환하고
        # 루트가 없으면 0으 반환한다.
        root = make_tree_by(root, 0)
        if not root:
            return 0

        # 루트를 큐에 넣고
        # depth를 0으로 초기화 해준다.
        q = deque([root])
        depth = 0

        # 큐가 있는동안 BFS로 반복한다.
        while q:
            # depth를 증가시키고
            depth += 1
            # 큐에 있는길이만큼 좌/우 자식을 탐색
            # 해당 레벨을 모두 탐색
            for _ in range(len(q)):
                # 큐에서 추출하고 자식이 있는 경우에만 추가
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
          
        return depth 
```