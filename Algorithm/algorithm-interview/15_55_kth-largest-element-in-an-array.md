# 배열의 k번째 큰 요소

<!-- TOC -->

- [배열의 k번째 큰 요소](#%EB%B0%B0%EC%97%B4%EC%9D%98-k%EB%B2%88%EC%A7%B8-%ED%81%B0-%EC%9A%94%EC%86%8C)
  - [문제](#%EB%AC%B8%EC%A0%9C)
  - [에시](#%EC%97%90%EC%8B%9C)
  - [숙고 1](#%EC%88%99%EA%B3%A0-1)
  - [코드 1](#%EC%BD%94%EB%93%9C-1)
  - [숙고 2](#%EC%88%99%EA%B3%A0-2)
  - [코드 3](#%EC%BD%94%EB%93%9C-3)

<!-- /TOC -->

## 문제
- 문제 : https://leetcode.com/problems/kth-largest-element-in-an-array/
- 숫자 배열과 숫자 k가 주어지면, 배열중 k번째로 큰 요소를 반환하여라.  
  k번째 고유한 요소가 아니라 정렬된 순서에서 k번째로 큰 요소이다.

## 에시
``` python
Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

## 숙고 1
- 힙을 이해한다면 크게 어렵지 않을 문제이다.  
  구현한 최대 힙을 통해서 풀어보자면 힙에 요소들을 차례로 넣고,  
  입력된 k까지 반복을 하고 K번째 추출된 요소를 출력하면 된다.
  
## 코드 1
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/15_55_kth-largest-element-in-an-array_01.py
``` python
class Heap:
    def __init__(self):
        self.items = [None]
    
    def __len__(self):
        return len(self.items) - 1

    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    def extract(self):
        if len(self) < 1:
            return None

        root = self.items[1]
        self.items[1] = self.items[-1]
        self.items.pop()
        self._percolate_down(1)

        return root

    def _percolate_up(self):
        cur = len(self)

        parent = cur // 2

        while parent > 0:
            if self.items[cur] > self.items[parent]:
                self.items[cur], self.items[parent] = self.items[parent], self.items[cur]
                
                cur = parent
                parent = cur // 2

    def _percolate_down(self, cur):
        biggest = cur
        left = cur * 2
        right = cur * 2 + 1

        if left <= len(self) and self.items[left] > self.items[biggest]:
            biggest = left

        if right <= len(self) and self.items[right] > self.items[biggest]:
            biggest = right

        if biggest != cur:
            self.items[cur], self.items[biggest] = self.items[biggest], self.items[cur]
            self._percolate_down(cur)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = Heap()
        
        for elem in nums:
            heap.insert(elem)
        
        return [heap.extract() for _ in range(k)][k - 1]
```

## 숙고 2
내장된 힙큐를 사용하면 아래와 같다.
## 코드 3
``` python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
       return heapq.nlargest(k, nums)[-1]
```