# 가장 긴 동일 값의 경로

<!-- TOC -->

- [가장 긴 동일 값의 경로](#%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EB%8F%99%EC%9D%BC-%EA%B0%92%EC%9D%98-%EA%B2%BD%EB%A1%9C)
  - [문제](#%EB%AC%B8%EC%A0%9C)
  - [예시](#%EC%98%88%EC%8B%9C)
  - [숙고 1](#%EC%88%99%EA%B3%A0-1)
  - [코드 1](#%EC%BD%94%EB%93%9C-1)

<!-- /TOC -->

## 문제
- 문제 : https://leetcode.com/problems/longest-univalue-path/
- 이진 트리의 루트가 주어지면  
  경로의 각 노드가 동일한 값을 갖는 가장 긴 경로의 길이를 반환하여라.  
  이 경로는 루트를 통과할 수도 있고 통과하지 않을 수도 있다.

  두 노드 사이의 경로 길이는 두 노드 사이의 모서리 수로 표시된다.
  
## 예시
![Example 1](./images/14_44_longest-univalue-path_01.jpeg)
``` python
Example 1:
Input: root = [5,4,5,1,1,5]
Output: 2
```
![Example 2](./images/14_44_longest-univalue-path_02.jpeg)
``` python
Example 2:
Input: root = [1,4,5,4,4,5]
Output: 2
```

## 숙고 1
- 풀이를 보면,  
  리프 노드까지 탐색해서 내려간 다음 올라오면서 값이 일치할 경우  
  최대 거리값 증가시키면서 올라온다.

## 코드 1
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/14_44_longest-univalue-path_01.py
``` python
class Solution:
    result: int = 0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode):
            if node is None:
                return 0

            # 존재하지 않는 노드까지 DFS 재귀 탐색
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 현재 노드가 자식 노드와 동일한 경우 거리 1 증가
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            # 왼쪽과 오른쪽 자식 노드 간 거리의 합 최댓값이 결과
            self.result = max(self.result, left + right)
            # 자식 노드 상태값 중 큰 값 리턴
            return max(left, right)
          
        dfs(root)
        return self.result
```