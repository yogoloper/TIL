# [항해99 6기] 알고리즘 주간(1) - 2022.03.11

<!-- TOC -->

- [[항해99 6기] 알고리즘 주간1 - 2022.03.11](#%ED%95%AD%ED%95%B499-6%EA%B8%B0-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%A3%BC%EA%B0%841---20220311)
- [Learned](#learned)
  - [알고리즘이란?](#%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%B4%EB%9E%80)
    - [점근 표기법](#%EC%A0%90%EA%B7%BC-%ED%91%9C%EA%B8%B0%EB%B2%95)
    - [시간복잡도](#%EC%8B%9C%EA%B0%84%EB%B3%B5%EC%9E%A1%EB%8F%84)
    - [공간복잡도](#%EA%B3%B5%EA%B0%84%EB%B3%B5%EC%9E%A1%EB%8F%84)
    - [흔히 말하는 표기법](#%ED%9D%94%ED%9E%88-%EB%A7%90%ED%95%98%EB%8A%94-%ED%91%9C%EA%B8%B0%EB%B2%95)
  - [알고리즘](#%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)
    - [예제 - 알파벳찾기](#%EC%98%88%EC%A0%9C---%EC%95%8C%ED%8C%8C%EB%B2%B3%EC%B0%BE%EA%B8%B0)
    - [애너그램 그룹](#%EC%95%A0%EB%84%88%EA%B7%B8%EB%9E%A8-%EA%B7%B8%EB%A3%B9)
    - [가장 긴 팰린드롬 부분 문자열](#%EA%B0%80%EC%9E%A5-%EA%B8%B4-%ED%8C%B0%EB%A6%B0%EB%93%9C%EB%A1%AC-%EB%B6%80%EB%B6%84-%EB%AC%B8%EC%9E%90%EC%97%B4)
    - [세 수의 합](#%EC%84%B8-%EC%88%98%EC%9D%98-%ED%95%A9)
    - [배열 파티션](#%EB%B0%B0%EC%97%B4-%ED%8C%8C%ED%8B%B0%EC%85%98)
- [Retrospect](#retrospect)

<!-- /TOC -->

# Learned
- 알고리즘
- 애너그램 그룹
- 가장 긴 팰린드롬 부분 문자열
- 세 수의 합
- 배열 파티션

## 알고리즘이란?
 - 같은 문제라도 시간적, 공간적으로 효율적인 방법으로 해결하기 위한 방법  

### 점근 표기법  
- 빅오(Big-O)표기법  
최악의 성능이 나올때  
- 빅 오메가(Big-Ω) 표기법  
최선의 성능이 나올때  

### 시간복잡도  
- 입력값을 통해 문제를 해결하는데 걸리는 시간과의 상관관계  

### 공간복잡도  
- 입력값을 통해 문제를 해결하는데 걸리는 공간과의 상관관계  

### 흔히 말하는 표기법  
- 요즘은 하드웨어들의 메모리 공간이 커져서 임베디드를 제외한 경우  
시간복잡도를 빅오 표기법으로 표현  

## 알고리즘  

### 예제 - 알파벳찾기  
https://www.acmicpc.net/problem/10809/  
```python
def get_idx_naive(word):
    result = [-1]*len(string.ascii_lowercase)
    for i in range(len(word)):
        char = word[i]
        for j in range(len(string.ascii_lowercase)):
            lo = string.ascii_lowercase[j]
            if result[j] == -1 and char == lo:
                result[j] = i
    print(' '.join([str(num) for num in result]))

def get_idx(word):
    # point 1. ord
    # point 2. O(n^2) -> O(n)
    result = [-1]*len(string.ascii_lowercase)
    for i in range(len(word)):
        idx = ord(word[i]) - 97
        if result[idx] == -1:
            result[idx] = i
    print(' '.join([str(num) for num in result]))

get_idx_naive('baekjoon')
get_idx('baekjoon')
```

### 애너그램 그룹
https://leetcode.com/problems/group-anagrams/  
https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/06_05_group-anagrams.md  

### 가장 긴 팰린드롬 부분 문자열  
https://leetcode.com/problems/longest-palindromic-substring/  
https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/06_06_longest-palindromic-substring.py  

> [문제]  
> 문자열이 주어지면 문자열 중에서 가장 긴 회문을 반환한다.
>
> [부연설명]
> 회문이란 "수박이박수", "다시합창합시다"와 같이  
> 문자열의 가운데를 기준으로 앞뒤가 같은 것을 말한다.
>
> Example 1:  
> Input: s = "babad"
> Output: "bab"
> Explanation: "aba" is also a valid answer.
>
> Example 2:  
> Input: s = "cbbd"
> Output: "bb"

> [풀이 1차]  
> 

### 세 수의 합  
https://leetcode.com/problems/3sum/  
https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/07_09_3sum.py  

> [문제]  
> 숫자열 배열이 세 개의 항목을 더해 0이 되는 트리플 셋을 반환한다.
> 트리플 셋의 중복은 없어야 한다.
>
> Example 1:  
> Input: nums = [-1,0,1,2,-1,-4]  
> Output: [[-1,-1,2],[-1,0,1]]  
>
> Example 2:  
> Input: nums = []  
> Output: []  
>
> Example 3:  
> Input: nums = [0]
> Output: []

> [풀이 1차]  
> 간단하게 반복문을 세바퀴를 돌렸더니 당연하게 타임 리밋에 걸리게 된다..

``` python

```

### 배열 파티션  
https://leetcode.com/problems/array-partition-i  
https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/07_10_array-partition-i.md

# Retrospect
코딩테스트를 위해서 알고리즘을 공부해본적이 드문 나에게  
갑자기 이런 많은 양의 문제를 풀라고 해서 과부하가 걸린것 같다..

사실 알고리즘보다 문서 정리에 재미를 들린건지  
이 파일을 몇 시간째 잡고 있는지 모르겠다.  

~~그래서 어제의 내용을 다 정리하지 못했다..~~  
소스 코드를 별도로 작성하는게 좋을지 .md 파일에 다 올리지 아직도 고민중이다.

알고리즘 문제를 풀다보니 학부시절 시험 공부하던 것이 생각나서 마냥 즐겁다.