# 두 이진 트리 병합

<!-- TOC -->

- [두 이진 트리 병합](#%EB%91%90-%EC%9D%B4%EC%A7%84-%ED%8A%B8%EB%A6%AC-%EB%B3%91%ED%95%A9)
  - [문제](#%EB%AC%B8%EC%A0%9C)
  - [에시](#%EC%97%90%EC%8B%9C)
  - [숙고 1](#%EC%88%99%EA%B3%A0-1)

<!-- /TOC -->

## 문제
- 문제 : https://leetcode.com/problems/merge-two-binary-trees/
- 두 이진 트리의 root1, root2가 주어진다.  
  그들 중 하나를 다른 하나를 덮기 위해 배치할 때 두 트리의 일부 노드는 겹치고  
  다른 노드는 겹치지 않는다.  
  두 트리를새로운 이진트리로 병합해야 한다.  
  
  병합 규칙은 두 노드가 겹치면 노드 값을 합산하여 병합된 노드의 새 값으로 합산하고,  
  그렇지 않으면 NOT Null 노드가 새 트리의 노드로 사용된다.

## 에시
![Example 1](./images/14_46_merge-two-binary-trees_01.jpeg)
``` python
Example 1:
Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]

Example 2:
Input: root1 = [1], root2 = [1,2]
Output: [2,2]
```

## 숙고 1
- 두 트리의 노드가 None 이면 None을 반환하고
  한 트리 노드만 존재할경우 덮어쓰고 반환한다.
  결과 트리를 담을 노드를 만들고  
  두 노드의 합을 값으로 하고,  
  자식 노드는 재귀를 통해 두 노드의 왼쪽/오른쪽 자식들을 넣어준다.

- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/14_46_merge-two-binary-trees.py
``` python
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # 노드가 빈 경우에 대한 처리
        if root1 is None and root2 is None:
            return None
        if root1 is None and root2:
            return root2
        elif root1 and root2 is None:
            return root1
        
        # 결과를 반환할 노드 생성하고
        # 입력 받은 노드들을 통해 값과 자식들을 구한다.
        ans = TreeNode()
        ans.val = root1.val + root2.val
        ans.left = self.mergeTrees(root1.left, root2.left)
        ans.right = self.mergeTrees(root1.right, root2.right)

        return ans
```