# 색 정렬

<!-- TOC -->

- [색 정렬](#%EC%83%89-%EC%A0%95%EB%A0%AC)
  - [문제](#%EB%AC%B8%EC%A0%9C)
  - [에시](#%EC%97%90%EC%8B%9C)
  - [숙고 1](#%EC%88%99%EA%B3%A0-1)
  - [코드 1](#%EC%BD%94%EB%93%9C-1)

<!-- /TOC -->

## 문제
- 문제 : https://leetcode.com/problems/sort-colors/
- 빨간색, 흰색 또는 파란색으로 색칠된 n개의 객체가 있는 배열 번호가 주어지면  
  동일한 색상의 객체가 인접하도록 제자리에서 정렬하고  
  색상은 빨간색, 흰색, 파란색으로 지정하여라.

  정수 0, 1, 2를 사용하여 빨강, 흰색, 파랑을 각각 나타낸다.

  라이브러리의 정렬 기능을 사용하지 않고 이 문제를 해결해야 한다.

## 에시
``` python
Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]
```

## 숙고 1
- 내장함수를 사용하지 말란다..  
  오늘 배운 퀵정렬을 사용해서 풀어보고자 했지만 쉽지 않다..

## 코드 1
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/17_63_sort-colors_01.py
``` python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # red, white는 0부터 증가, blue는 리스트의 길이부터 감소
        # blue는 리스트의 범위를 벗어나 있는 것에 주의
        red, white, blue = 0, 0, len(nums)
        
        # white의 인덱스가 blue 인덱스와 같거나 크다면 분류를 종료한다.
        while white < blue:
            # white가 가리키는 값이 0이라면
            # 현재 red가 가리키는 곳의 값과 교체 후
            # red, white 인덱스 둘다 +1
            if nums[white] < 1:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            # white가 가리키는 값이 2라면
            # blue의 인덱스만 +1 후
            # 현재 blue가 가리키는 곳의 값과 교체
            elif nums[white] > 1:
                blue -= 1
                nums[white], nums[blue] = nums[blue], nums[white]
            # while가 가리키는 곳의 값이 1이라면
            # 다음값을 비교하도록 white의 인덱스만 +1
            else:
                white += 1
        
        return nums
```