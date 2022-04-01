# [항해99 6기] 알고리즘 주간(16) - 2022.03.26

<!-- TOC -->

- [[항해99 6기] 알고리즘 주간16 - 2022.03.26](#%ED%95%AD%ED%95%B499-6%EA%B8%B0-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%A3%BC%EA%B0%8416---20220326)
- [Learned](#learned)
  - [정렬](#%EC%A0%95%EB%A0%AC)
    - [버블 정렬](#%EB%B2%84%EB%B8%94-%EC%A0%95%EB%A0%AC)
    - [선택 정렬](#%EC%84%A0%ED%83%9D-%EC%A0%95%EB%A0%AC)
    - [삽입 정렬](#%EC%82%BD%EC%9E%85-%EC%A0%95%EB%A0%AC)
  - [삽입 정렬 리스트 - 더 공부하기](#%EC%82%BD%EC%9E%85-%EC%A0%95%EB%A0%AC-%EB%A6%AC%EC%8A%A4%ED%8A%B8---%EB%8D%94-%EA%B3%B5%EB%B6%80%ED%95%98%EA%B8%B0)
  - [가장 큰 수](#%EA%B0%80%EC%9E%A5-%ED%81%B0-%EC%88%98)
  - [[이코테]성적이 낮은 순서로 학생 출력하기](#%EC%9D%B4%EC%BD%94%ED%85%8C%EC%84%B1%EC%A0%81%EC%9D%B4-%EB%82%AE%EC%9D%80-%EC%88%9C%EC%84%9C%EB%A1%9C-%ED%95%99%EC%83%9D-%EC%B6%9C%EB%A0%A5%ED%95%98%EA%B8%B0)
  - [[이코테]두 배열의 원소 교체 - 더 공부하기](#%EC%9D%B4%EC%BD%94%ED%85%8C%EB%91%90-%EB%B0%B0%EC%97%B4%EC%9D%98-%EC%9B%90%EC%86%8C-%EA%B5%90%EC%B2%B4---%EB%8D%94-%EA%B3%B5%EB%B6%80%ED%95%98%EA%B8%B0)
  - [[boj]전화번호 목록 - 더 공부하기](#boj%EC%A0%84%ED%99%94%EB%B2%88%ED%98%B8-%EB%AA%A9%EB%A1%9D---%EB%8D%94-%EA%B3%B5%EB%B6%80%ED%95%98%EA%B8%B0)
- [Retrospect](#retrospect)

<!-- /TOC -->


# Learned
- 정렬
  - 버블 정렬
  - 선택 정렬
  - 삽입 정렬
- 삽입 정렬 리스트
- 가장 큰 수 
- [이코테]성적이 낮은 순서로 학생 출력하기
- [이코테]두 배열의 원소 교체
- [boj] 전화번호 목록

## 정렬
- 테이터를 효율적으로 탐색할 수 있게 데이터를 순서대로 나열하는 방법
- 정렬의 포크 댄스 : https://www.youtube.com/user/megaovermoc/videos

### 버블 정렬
- 0번 1번 비교, 1번 2번 비교, 2번 3번 비교, n-1번 n번 비교하며  
  한바퀴 돌았을 때 제일 큰값이 제일 뒤로 간다.  
- 다음 바퀴부터는 정렬된 요소 전까지만 비교한다.

``` python
def bubblesort(lst):
    # 최댓값을 구하는 알고리즘을 len(lst) - 1 만큼 반복한다.
    iters = len(lst) - 1
    for iter in range(iters):
        # 이미 구한 최댓값은 범위에서 제외한다.
        wall = iters - iter
        for cur in range(wall):
            if lst[cur] > lst[cur + 1]:
                lst[cur], lst[cur + 1] = lst[cur + 1], lst[cur]
    return lst
```

### 선택 정렬
- 제일 작은 값을 찾아서 0번과 교체  
  0번을 제외한 제일 작은 값을 찾아서 1번과 교체하며  
  작은 값을 먼저 찾아서 정렬한다.
- 최소값을 선택하여 맨 앞으로 보내는 정렬 

```python
def selectionsort(lst):
    iters = len(lst) - 1
    for iter in range(iters):
        minimun = iter
        for cur in range(iter + 1, len(lst)):
            if lst[cur] < lst[minimun]:
                minimun = cur

        if minimun != iter:
            lst[minimun], lst[iter] = lst[iter], lst[minimun]

    return lst
```
### 삽입 정렬
- 0번 요소는 정렬된 상태라고 취급하고 1번 요소부터 자리를 찾아 삽입한다.    
  1번 요소는 1번, 0번 중에 자기 자리를 찾아서 정렬된다.  
  2번 요소는 2, 1, 0번 중에서 자기 자리를 찾아서 정렬된다.
```python
def insertionsort(lst):
    # 0번째 요소는 이미 정렬되어있으니, 1번째 ~ lst(len)-1 번째를 정렬하면 된다.
    for cur in range(1, len(lst)):
        # 비교지점이 cur-1 ~ 0(=cur-cur)까지 내려간다.
        for delta in range(1, cur + 1):
            cmp = cur - delta
            if lst[cmp] > lst[cmp + 1]:
                lst[cmp], lst[cmp + 1] = lst[cmp + 1], lst[cmp]
            else:
                break
    return lst

def insertionsort_2(lst):
    for idx in range(1, len(lst)):
        val = lst[idx]
        cmp = idx - 1

        while lst[cmp] > val and cmp >= 0:
            lst[cmp + 1] = lst[cmp]
            cmp -= 1

        lst[cmp + 1] = val

    return lst
```

## 삽입 정렬 리스트 - 더 공부하기
- 문제 : https://leetcode.com/problems/insertion-sort-list/
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/17_60_insertion-sort-list.md  

## 가장 큰 수
- 문제 : https://leetcode.com/problems/largest-number/
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/17_61_largest-number.md  

## [이코테]성적이 낮은 순서로 학생 출력하기
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/pyhon-for-coding-test/06_03.md  

## [이코테]두 배열의 원소 교체 - 더 공부하기
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/pyhon-for-coding-test/06_04.md  

## [boj]전화번호 목록 - 더 공부하기
- 문제 : https://www.acmicpc.net/problem/5052
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/Baekjoon-Online-Judge/5052.md  

# Retrospect
정렬을 오랜만에 봤더니 가물가물한 것 같다.  
버블은 앞뒤로 비교하며 큰 값부터 정렬  
선택은 작은값을 찾아서 앞에서 부터 정렬  
삽입은 압 요소들은 정렬된 상태로 취급하고 뒤의 요소가 자리르 찾아가서 정렬  