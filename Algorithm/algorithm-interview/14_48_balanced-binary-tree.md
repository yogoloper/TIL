# 균형 이진 트리

<!-- TOC -->

- [균형 이진 트리](#%EA%B7%A0%ED%98%95-%EC%9D%B4%EC%A7%84-%ED%8A%B8%EB%A6%AC)
  - [문제](#%EB%AC%B8%EC%A0%9C)
  - [에시](#%EC%97%90%EC%8B%9C)
  - [숙고 1](#%EC%88%99%EA%B3%A0-1)
  - [코드 1](#%EC%BD%94%EB%93%9C-1)

<!-- /TOC -->

## 문제
- 문제 : https://leetcode.com/problems/balanced-binary-tree/
- 이진 트리가 주어지면 높이 균형이 맞는지 확인한다.  
  높이 균형 이진 트리는 모든 노드의 왼쪽 및 오른쪽 하위 트리의 높이가 1이하로 다른 이진 트리

## 에시
![Example 1](./images/14_48_balanced-binary-tree_01.jpeg)
``` python
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true
```
![Example 2](./images/14_48_balanced-binary-tree_02.jpeg)
``` python
Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true
```

## 숙고 1
- 풀이를 보면  
  재귀를 통해서 자식 노드가 없을 경우에는 깊이를 0으로 반환하고  
  노두가 있을경우 좌우 노드의 맥스+1 을 해서 반환한다.  
  이를 통해서 한쪽 자식의 깊이 레벨이 2 이상일 경우 -1을 반환한다.

  결과로 -1을 반환 받게 되면 해당 트리는 균형 이진 트리가 아니라는 의미이다.

## 코드 1
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/14_48_balanced-binary-tree_01.py
``` python
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            # None 이면 0 반환
            if not root:
                return 0

            # 좌우 자식노드 깊이 레벨 확인
            left = check(root.left)
            right = check(root.right)
            
            # 자식 노들을의 값이 -1이거나
            # 자식 노드들의 깊이 레벨이 2이상이면 -1 반환
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            # 자식들중 깊이 레벨이 높은 것에 +1 하여 반환
            return max(left, right) + 1
        
        # check 함수를 통해 -1이 반환되면 균형 트리가 아니다.
        return check(root) != -1
```