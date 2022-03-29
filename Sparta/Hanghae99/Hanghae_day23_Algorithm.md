# [항해99 6기] 알고리즘 주간(19) - 2022.03.29

<!-- TOC -->

- [[항해99 6기] 알고리즘 주간19 - 2022.03.29](#%ED%95%AD%ED%95%B499-6%EA%B8%B0-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%A3%BC%EA%B0%8419---20220329)
- [Learned](#learned)
  - [병합 정렬](#%EB%B3%91%ED%95%A9-%EC%A0%95%EB%A0%AC)
    - [시간 복잡도](#%EC%8B%9C%EA%B0%84-%EB%B3%B5%EC%9E%A1%EB%8F%84)
    - [구현](#%EA%B5%AC%ED%98%84)
  - [구간 병합 - 더 공부하기](#%EA%B5%AC%EA%B0%84-%EB%B3%91%ED%95%A9---%EB%8D%94-%EA%B3%B5%EB%B6%80%ED%95%98%EA%B8%B0)
  - [[이코테]실패율](#%EC%9D%B4%EC%BD%94%ED%85%8C%EC%8B%A4%ED%8C%A8%EC%9C%A8)
  - [[boj]단어 정렬](#boj%EB%8B%A8%EC%96%B4-%EC%A0%95%EB%A0%AC)
- [Retrospect](#retrospect)

<!-- /TOC -->

# Learned
- 병합 정렬
- 구간 병합
- [이코테]실패율
- [boj]단어 정렬

## 병합 정렬
- 존 폰 노이만(John von Neumann)이 제안한 방법  
  분할 정복 알고리즘의 하나 이다.  
  
<div style="background-color: white;">
<image src="./images/Hanghae_day23_Algorithm_01.png">
</div>

### 과정
1. 리스트의 길이가 0 또는 1이면 이미 정렬된 것으로 본다. 그렇지 않은 경우에는
2. 정렬되지 않은 리스트를 절반으로 잘라 비슷한 크기의 두 부분 리스트로 나눈다.
3. 각 부분 리스트를 재귀적으로 합병 정렬을 이용해 정렬한다.
4. 두 부분 리스트를 다시 하나의 정렬된 리스트로 합병한다

### 시간 복잡도
- O(NlogN)

### 구현
``` python
def merge(arr1, arr2):
    result = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    while i < len(arr1):
        result.append(arr1[i])
        i += 1
    while j < len(arr2):
        result.append(arr2[j])
        j += 1
    
    return result

def sort(lst):
    if len(lst) <= 1:
        return lst
    
    mid = len(lst) // 2
    l = lst[:mid]
    r = lst[mid:]
    return merge(sort(l), sort(r))

```
## 구간 병합 - 더 공부하기
- 문제 : https://leetcode.com/problems/merge-intervals/
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/programmers/17_59_merge-intervals.md  

## [이코테]실패율
- 문제 : https://programmers.co.kr/learn/courses/30/lessons/42889
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/pyhon-for-coding-test/14_25.md  

## [boj]단어 정렬
- 문제 : https://www.acmicpc.net/problem/1181
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/Baekjoon-Online-Judge/1181.md  

# Retrospect
https://www.youtube.com/watch?v=3H4umWD5bwI  
오늘 공유 영상으로 "배달의민족 CEO에게 뽑고 싶은 개발자를 물어보았다" 영상을 보게 되었다.  

개발자라고 한다면 스스로를 코딩 하는 사람이 아닌  
우리에게 주어진 비즈니스 모델을 해결하는 사람이라고 생각했으면 좋겠다라는  
우아한형제들의 김범준 대표님의 얘기를 듣고  
나는 언제부터 시키는 것만 하는 사람이 되었는가에 대한 깊은 고민을 하게 되었다.  

학부생때는 그렇게 하고 싶은 것도, 이루고 싶은 것도 많았는데  
어쩌다 보니 그런 방향과는 멀게만 걷게 되었다.  

생각하는 대로 살지 않으면, 사는 대로 생각하게 된다고 했던가  
스스로 생각하고 스스로 행동하자