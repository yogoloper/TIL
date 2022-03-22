# 이진 트리 반전

<!-- TOC -->

- [이진 트리 반전](#%EC%9D%B4%EC%A7%84-%ED%8A%B8%EB%A6%AC-%EB%B0%98%EC%A0%84)
  - [문제](#%EB%AC%B8%EC%A0%9C)
  - [에시](#%EC%97%90%EC%8B%9C)
  - [숙고 1](#%EC%88%99%EA%B3%A0-1)
  - [코드 1](#%EC%BD%94%EB%93%9C-1)

<!-- /TOC -->

## 문제
- 문제 : https://leetcode.com/problems/invert-binary-tree/
- 이진 트리의 루트가 주어지면, 트리를 반전시겨서 반환하여라.

## 에시
![Example 1](./images/14_45_invert-binary-tree_01.jpeg)
``` python
Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
```
![Example 2](./images/14_45_invert-binary-tree_02.jpeg)
``` python
Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []
```

## 숙고 1
- BFS 구조를 이용해서 루트를 제외하고  
  아래로 내려가면서 같은 레벨의 좌우 노드를 바꿔주면 될듯 하다.
## 코드 1
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/14_45_invert-binary-tree_01.py
``` python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 트리의 루트를 큐에 삽입
        q = deque([root])
        
        # 큐가 있는 동안 반복
        while q:
            # 큐에서 노드를 추출
            node = q.popleft()
            
            # 노드가 있으면 좌우 노드 스왑
            if node:
                node.left, node.right = node.right, node.left
                
                # 현재 노드의 자식들을 큐에 넣어서 반복
                q.append(node.left)
                q.append(node.right)
        
        return root
```