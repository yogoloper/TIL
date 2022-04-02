# 코스 스케줄

<!-- TOC -->

- [코스 스케줄](#%EC%BD%94%EC%8A%A4-%EC%8A%A4%EC%BC%80%EC%A4%84)
  - [문제](#%EB%AC%B8%EC%A0%9C)
  - [예시](#%EC%98%88%EC%8B%9C)
  - [숙고 1](#%EC%88%99%EA%B3%A0-1)
  - [코드 1](#%EC%BD%94%EB%93%9C-1)

<!-- /TOC -->

## 문제
- https://leetcode.com/problems/course-schedule/
- 수강해야 하는 총 numCourses 과정이 있으며 0에서 numCourses - 1 까지 레이블이 지정된다.  
  전제 조건 [i] = [ai, bi]는 수강하려는 경우 bi과정을 먼저 수강해야 함을 나타내는 배열 전제조건이 제공된다.  

  예를 들어 [0, 1] 쌍은 코스 0을 수강하려면 코스 1을 수강해야 함을 나타낸다.  
  모든 과정을 마칠수 있으면 True, 그렇지 않으면 False를 반환하여라.
## 예시
``` python
Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
```

## 숙고 1
## 코드 1
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/12_39_course-schedule_01.py
``` python
```