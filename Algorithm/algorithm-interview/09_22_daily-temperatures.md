# 일일 온도
<!-- TOC -->

- [일일 온도](#%EC%9D%BC%EC%9D%BC-%EC%98%A8%EB%8F%84)
  - [문제](#%EB%AC%B8%EC%A0%9C)
  - [예시](#%EC%98%88%EC%8B%9C)
  - [숙고 1](#%EC%88%99%EA%B3%A0-1)
  - [코드 1](#%EC%BD%94%EB%93%9C-1)
  - [숙고 2](#%EC%88%99%EA%B3%A0-2)
  - [코드 2](#%EC%BD%94%EB%93%9C-2)

<!-- /TOC -->

## 문제
- https://leetcode.com/problems/daily-temperatures/
- 일별 온도를 나타내는 정수 배열이 주어지면 answer[i]가 더 따뜻한 온도를 얻기 위해  
i 번째 날 이후에 기다려야 하는 일수가 되도록 배열 반환한다.
- 더 따뜻한 날이 없다면 answer[i] == 0 을 유지하여라.

## 예시
``` python
Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
```
## 숙고 1
- 이중 배열로 돌리면 짜기는 편할거 같은데  
  타임리밋..

## 코드 1
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/09_22_daily-temperatures_01.py  
``` python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(0, len(temperatures)):
            after_days = 0
            flag = False

            for j in range(i + 1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    flag = True
                    after_days += 1
                    break
                else:
                    after_days += 1

            if flag is not True:
                after_days = 0
            result.append(after_days)
        return result
```

## 숙고 2
- 어떻게 하면 오늘 공부한 스택을 이용할 수 있을까?  
  풀이를 보면 enumerate로 문자열 리스트의 인덱스와 값을 같이 사용하며,  
  반복문과 -1 인덱스를 통해 스택의 탑을 가져와서 비교하는 식으로 풀이 되어있다.

## 코드 2
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/09_22_daily-temperatures_02.py  

``` python 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 값을 반환할 배열 할당
        answer = [0] * len(temperatures)
        # 스택 배열 할당
        stack = []
        
        # 온도 리스트 반복문을 enumerate로 해서 인덱스와 값을 같이 사용
        for i, cur in enumerate(temperatures):
            # 스택에는 온도 리스트의 인덱스 값을 쌓아주며
            # 스택이 존재하고 나중온도가 이전온도보다 높을 경우
            # 그 둘의 인덱스의 차이를 결과 배열에 넣어준다.
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
            
        return answer
```