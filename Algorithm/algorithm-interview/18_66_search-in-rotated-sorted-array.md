# 회전 정렬된 배열 검색

<!-- TOC -->

- [회전 정렬된 배열 검색](#%ED%9A%8C%EC%A0%84-%EC%A0%95%EB%A0%AC%EB%90%9C-%EB%B0%B0%EC%97%B4-%EA%B2%80%EC%83%89)
  - [문제](#%EB%AC%B8%EC%A0%9C)
  - [예시](#%EC%98%88%EC%8B%9C)
  - [숙고 1](#%EC%88%99%EA%B3%A0-1)
  - [코드 1](#%EC%BD%94%EB%93%9C-1)

<!-- /TOC -->

## 문제
- 문제 : https://leetcode.com/problems/search-in-rotated-sorted-array/
- 오름차순 정렬된 정수 배열 nums가 있다.  
  함수에 전달되기 전에 배열이 nums[k], nums[k+1], ... , nums[n-1], nums[0], nums[1], ..., nums[k-1]](0-인덱싱됨). 예를 들어, [0,1,2,4,5,6,7]은 피벗 인덱스 3에서 회전되어 [4,5,6,7,0,1,2]가 될 수 있다.  

  가능한 회전 후 배열 nums와 정수 대상이 주어지면  
  대상이 nums에 존재하면 대상 인덱스를 반환하고,  
  그렇지 않다면 -1을 반환하여라.

  시간 복잡도 O(logN) 제한

## 예시
``` python
Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1
```

## 숙고 1
- 배열을 다시 정렬해서 bisect_Left()를 활용하고 싶지만  
  시간 복잡도 제한이 있다.  
- 풀이를 보자..

## 코드 1
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/18_66_search-in-rotated-sorted-array_01.py  
``` python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(lst, start, end):
            if start > end:
                return -1

            mid = (start + end) // 2
            if lst[mid] < target:
                return bs(lst, mid + 1, end)
            elif lst[mid] > target:
                return bs(lst, start, mid - 1)
            else:
                return mid
        
        # 배열이 비어있으면 -1 반환
        if not nums:
            return -1

        # 좌우측 끝의 인덱스를 가져온다.
        left = 0
        right = len(nums) - 1
        # 왼쪽 오른쪽의 인덱스가 같아지면 종료
        while left < right:
            # 가운데 인덱스를 찾고
            mid = (left + right) // 2
            # 중간 인덱스 값이 오른쪽보다 크면
            # 최소값은 중간인덱스보다 오른쪽에 있다는 얘기이므로
            # 왼쪽 인덱스에 중간 인덱스 + 1
            if nums[mid] > nums[right]:
                left = mid + 1
            # 중간 인덱스 값이 오른쪽보다 작다면 왼쪽에 있다는 얘기이므로
            # 오른쪽 인덱스에 중간 인덱스 저장
            else:
                right = mid

        # 최저값의 인덱스를 찾으면 
        # 입력된 배열의 첫 부분부터 인덱스 전까지의 요소들을
        # 맨뒤에 추가 해준다. 
        added = nums + nums[:left]

        # 반복문을 나오면 왼쪽 인덱스가 최소 값의 인덱스를 가지고 있으므로,  
        # 최소값 인덱스 를 시작지점으로, 합병된 배열의 마지막 인덱스를 끝지점으로  
        # 이진탐색을 진행한다.
        result = bs(added, left, len(added) - 1)
        
        # 결과가 -1이 아니라면  
        # 합병된 배열을 입력 배열로 나머지 연산을 해서 인덱스를 반환한다.
        return result if result == -1 else result % len(nums)
```