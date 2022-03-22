# 이진 트리의 직경

<!-- TOC -->

- [이진 트리의 직경](#%EC%9D%B4%EC%A7%84-%ED%8A%B8%EB%A6%AC%EC%9D%98-%EC%A7%81%EA%B2%BD)
  - [문제](#%EB%AC%B8%EC%A0%9C)
  - [예시](#%EC%98%88%EC%8B%9C)
  - [숙고 1](#%EC%88%99%EA%B3%A0-1)
  - [코드 1](#%EC%BD%94%EB%93%9C-1)

<!-- /TOC -->

## 문제
- 문제 : https://leetcode.com/problems/diameter-of-binary-tree/
- 이진 트리의 루트가 주어지면 트리 지름의 길이를 반환하여라.  
- 지름은 두 노드 사이에서 가장 긴 경로의 길이이다.  
  이 경로는 루트를 통과할 수도 있고 통과하지 않을 수도 있다.  

  두 노드 사이의 경로 길이는 두 노드 사이의 모서리 수로 표시 된다.

## 예시
![Example 1](./images/14_43_diameter-of-binary-tree_01.jpeg)
``` python
Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1
```

## 숙고 1
- 풀이를 보면,  
  리프 노드까지 탐색한 다음 부모로 거슬러 올라가면서  
  각각의 거리를 계산해 상태값을 업데이트하면서 누적해 나간다.

## 코드 1
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/14_43_diameter-of-binary-tree_01.py
``` python
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
            # 왼쪽과 오른쪽의 경로를 구해야 하므로 +2를 해준다.
            self.longest = max(self.longest, left + right + 2)
            # 상태값
            return max(left, right) + 1
        
        dfs(root)
        return self.longest
```