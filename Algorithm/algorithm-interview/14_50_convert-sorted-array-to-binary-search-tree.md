# 정렬된 배열의 이진 탐색 트리 변환

<!-- TOC -->

- [정렬된 배열의 이진 탐색 트리 변환](#%EC%A0%95%EB%A0%AC%EB%90%9C-%EB%B0%B0%EC%97%B4%EC%9D%98-%EC%9D%B4%EC%A7%84-%ED%83%90%EC%83%89-%ED%8A%B8%EB%A6%AC-%EB%B3%80%ED%99%98)
  - [문제](#%EB%AC%B8%EC%A0%9C)
  - [에시](#%EC%97%90%EC%8B%9C)
  - [숙고 1](#%EC%88%99%EA%B3%A0-1)
  - [코드 1](#%EC%BD%94%EB%93%9C-1)

<!-- /TOC -->

## 문제
- 문제 : https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
- 오름차순으로 정렬된 정수 배열 num이 주어지면, 높이 균형 이진 트리로 변환하여라.  
  높이 균형 이진 트리는 모든 노드의 두 하위 트리 깊이가 1 이상 차이나지 않는 이진트리이다.

  모든 MHT의 루트 레이블 목록을 반환한다. 순서는 상관 없다.  

  뿌리 나무의 높이는 뿌리와 잎 사이의 가장 긴 하향 경로의 가장자리 수이다.

## 에시
![Example 1](./images/14_50_convert-sorted-array-to-binary-search-tree_01.jpeg)
![Example 1](./images/14_50_convert-sorted-array-to-binary-search-tree_02.jpeg)
``` python
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:
```

![Example 2](./images/14_50_convert-sorted-array-to-binary-search-tree_03.jpeg)
``` python
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
```

## 숙고 1
- 숫자 배열을 받으면 이진 탐색 트리로 만들고,  
  이진 탐색 트리를 다시 숫자 배열로 만들어서 반환하자
- 이진 탐색 트리 만들기  
  배열은 이미 정렬이 된 상태이므로 트리의 길이를 반으로 나눠 몫을 루트인덱스로 잡는다.  
  왼쪽 자식에게는 배열의 0번 인덱스부터 루트 인덱스 전까지 주며 반복하고
  오른쪽 자식에게는 루트 인덱스 + 1부터 배열의 길이까지 반복한다.

## 코드 1
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/14_50_convert-sorted-array-to-binary-search-tree_01.py
``` python
# 배열을 이진 트리로 반환하는 함수
def sorted_array_to_bst(lst):
    # 빈 리스트라면 None을 반환
    if not lst:
        return None

    # 배열의 가운데를 상위노드로 삼기위해 2로 나눈 몫을 mid로 지정한다.
    mid = len(lst) // 2

    # 상위 노드 설정
    node = TreeNode(lst[mid])
    # 왼쪽 자식 노드는 0부터 상위 노드의 인덱스 전까지
    node.left = sorted_array_to_bst(lst[:mid])
    # 오른쪽 자식 노드는 상위 노드의 인덱스 + 1부터 인덱스 끝까지
    node.right = sorted_array_to_bst(lst[mid + 1:])

    return node

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        if not nums:
            return []
        
        root = sorted_array_to_bst(nums)
        return root
```