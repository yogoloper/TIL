# [항해99 6기] 알고리즘 주간(22) - 2022.04.01

<!-- TOC -->

- [[항해99 6기] 알고리즘 주간22 - 2022.04.01](#%ED%95%AD%ED%95%B499-6%EA%B8%B0-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%A3%BC%EA%B0%8422---20220401)
- [Learned](#learned)
  - [이진 탐색](#%EC%9D%B4%EC%A7%84-%ED%83%90%EC%83%89)
    - [시간 복잡도](#%EC%8B%9C%EA%B0%84-%EB%B3%B5%EC%9E%A1%EB%8F%84)
    - [구현](#%EA%B5%AC%ED%98%84)
    - [내장함수](#%EB%82%B4%EC%9E%A5%ED%95%A8%EC%88%98)
  - [이진 검색](#%EC%9D%B4%EC%A7%84-%EA%B2%80%EC%83%89)
  - [회전 정렬된 배열 검색 - 더 공부하기](#%ED%9A%8C%EC%A0%84-%EC%A0%95%EB%A0%AC%EB%90%9C-%EB%B0%B0%EC%97%B4-%EA%B2%80%EC%83%89---%EB%8D%94-%EA%B3%B5%EB%B6%80%ED%95%98%EA%B8%B0)
  - [두 배열의 교집합](#%EB%91%90-%EB%B0%B0%EC%97%B4%EC%9D%98-%EA%B5%90%EC%A7%91%ED%95%A9)
  - [[이코테]범위를 반씩 좁혀가는 탐색](#%EC%9D%B4%EC%BD%94%ED%85%8C%EB%B2%94%EC%9C%84%EB%A5%BC-%EB%B0%98%EC%94%A9-%EC%A2%81%ED%98%80%EA%B0%80%EB%8A%94-%ED%83%90%EC%83%89)
  - [[이코테]부품 찾기](#%EC%9D%B4%EC%BD%94%ED%85%8C%EB%B6%80%ED%92%88-%EC%B0%BE%EA%B8%B0)
- [Retrospect](#retrospect)

<!-- /TOC -->

# Learned
- 이진 탐색
- 이진 검색
- 회전 정렬된 배열 검색
- 두 배열의 교집합
- [이코테]범위를 반씩 좁혀가는 탐색
- [이코테]부품 찾기

## 이진 탐색
- 배열이 정렬되어있을 경우, 절반씩 줄여나가면서 탐색하는 기법

### 시간 복잡도
- O(logN)의 시간 복잡도를 가지며,  
  1억개의 목록을 이진탐색으로 탐색한다면 27번 안에 찾을 수 있다.

### 구현
- 이미 정렬된 리스트 이므로 반씩 잘라가면서 타겟을 찾는다.  
  인덱스의 값과 타겟의 값이 크거나 작지 않다면 해당 타겟을 반환한다.
``` python
def binary_search(nums, target):
    def bs(start, end):
        if start > end:
            return -1

        mid = (start + end) // 2

        if nums[mid] < target:
            return bs(mid + 1, end)
        elif nums[mid] > target:
            return bs(start, mid - 1)
        else:
            return mid

    return bs(0, len(nums) - 1)
```
### 내장함수
- 파이썬에는 내장함수 bisect가 존재한다.
- bisect_left(nums, target)  
  nums 리스트에서 타켓보다 작은값과 같거나 큰 값으로 구분  
  같거나 큰값의 인덱스를 반환  
  같은 값이 여러개 있으면 제일 왼쪽 인덱스를 반환

  [-1, 1, 2, 2, 2, 3] 2 => 2 인덱스 반환  
  [-1, 1, 3, 3, 5] 2 => 2 인덱스 반환  
  -> 처음으로 나오는 3이 타겟인 2보다 크거나 같은 값중 제일 왼쪽 인덱스 반환  
  [-5, -4, -3, -2, -1] 2 => 5  
  -> 크거나 같은 값이 없으므로 리스트의 인덱스를 벗어난 5번 인덱스 반환  
  [3, 4, 5, 6, 7] 2 =>  0
  -> 3이 2보다 크거나 같은 값이므로 0번 인덱스 반환

- bisect_right(nums, target)  
  nums 리스트에서 타겟의 인덱스 + 1을 반환
```python
def binary_search_builtin(nums, target):
    idx = bisect.bisect_left(nums, target)
		# idx == len(nums) 가능하기 떄문.
		"""Return the index where to insert item x in list a, assuming a is sorted.

    The return value i is such that all e in a[:i] have e < x, and all e in
    a[i:] have e >= x.  So if x already appears in the list, a.insert(x) will
    insert just before the leftmost x already there.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """
    if idx < len(nums) and nums[idx] == target:
        return idx
    else:
        return -1
```

## 이진 검색
- 문제 : https://leetcode.com/problems/binary-search/
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/18_65_binary-search.md  

## 회전 정렬된 배열 검색 - 더 공부하기
- 문제 : https://leetcode.com/problems/search-in-rotated-sorted-array/
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/18_66_search-in-rotated-sorted-array.md  

## 두 배열의 교집합
- 문제 : https://leetcode.com/problems/intersection-of-two-arrays/
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/18_67_intersection-of-two-arrays.md  

## [이코테]범위를 반씩 좁혀가는 탐색
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/pyhon-for-coding-test/07_01.md  

## [이코테]부품 찾기
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/pyhon-for-coding-test/07_02.md  

# Retrospect
학부때도 이진탐색 자체을 어려워 하지는 않았는데  
응용 문제를 직면하게 되면 조금 어려운 것 같다.  

아직도 리스트의 인덱스를 가지고 놀기가 버겁다.  