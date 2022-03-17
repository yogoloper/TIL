<!-- TOC -->

- [자료형](#%EC%9E%90%EB%A3%8C%ED%98%95)
  - [수 자료형](#%EC%88%98-%EC%9E%90%EB%A3%8C%ED%98%95)
    - [정수형](#%EC%A0%95%EC%88%98%ED%98%95)
    - [실수형](#%EC%8B%A4%EC%88%98%ED%98%95)
    - [수 자료형의 연산](#%EC%88%98-%EC%9E%90%EB%A3%8C%ED%98%95%EC%9D%98-%EC%97%B0%EC%82%B0)
  - [리스트 자료형](#%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%9E%90%EB%A3%8C%ED%98%95)
    - [리스트 만들기](#%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EB%A7%8C%EB%93%A4%EA%B8%B0)
    - [리스트의 인덱싱과 슬라이싱](#%EB%A6%AC%EC%8A%A4%ED%8A%B8%EC%9D%98-%EC%9D%B8%EB%8D%B1%EC%8B%B1%EA%B3%BC-%EC%8A%AC%EB%9D%BC%EC%9D%B4%EC%8B%B1)
    - [리스트 컴프리헨션](#%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%BB%B4%ED%94%84%EB%A6%AC%ED%97%A8%EC%85%98)
      - [언더바_의 역할](#%EC%96%B8%EB%8D%94%EB%B0%94_%EC%9D%98-%EC%97%AD%ED%95%A0)
    - [리스트 관련 기타 메서드](#%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EA%B4%80%EB%A0%A8-%EA%B8%B0%ED%83%80-%EB%A9%94%EC%84%9C%EB%93%9C)
      - [리스트 내 특정값 모두 제거](#%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EB%82%B4-%ED%8A%B9%EC%A0%95%EA%B0%92-%EB%AA%A8%EB%91%90-%EC%A0%9C%EA%B1%B0)
  - [문자열 자료형](#%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%9E%90%EB%A3%8C%ED%98%95)
    - [문자열 초기화](#%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%B4%88%EA%B8%B0%ED%99%94)
    - [문자열 연산](#%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%97%B0%EC%82%B0)
  - [튜플 자료형](#%ED%8A%9C%ED%94%8C-%EC%9E%90%EB%A3%8C%ED%98%95)
  - [사전 자료형](#%EC%82%AC%EC%A0%84-%EC%9E%90%EB%A3%8C%ED%98%95)
    - [사전 자료형 관련 함수](#%EC%82%AC%EC%A0%84-%EC%9E%90%EB%A3%8C%ED%98%95-%EA%B4%80%EB%A0%A8-%ED%95%A8%EC%88%98)
  - [집합 자료형](#%EC%A7%91%ED%95%A9-%EC%9E%90%EB%A3%8C%ED%98%95)
    - [집합 자료형의 연산](#%EC%A7%91%ED%95%A9-%EC%9E%90%EB%A3%8C%ED%98%95%EC%9D%98-%EC%97%B0%EC%82%B0)
    - [집합 자료형 관련 함수](#%EC%A7%91%ED%95%A9-%EC%9E%90%EB%A3%8C%ED%98%95-%EA%B4%80%EB%A0%A8-%ED%95%A8%EC%88%98)
- [조건문](#%EC%A1%B0%EA%B1%B4%EB%AC%B8)
  - [비교 연산자](#%EB%B9%84%EA%B5%90-%EC%97%B0%EC%82%B0%EC%9E%90)
  - [논리 연산자](#%EB%85%BC%EB%A6%AC-%EC%97%B0%EC%82%B0%EC%9E%90)
  - [파이썬 기타 연산자](#%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EA%B8%B0%ED%83%80-%EC%97%B0%EC%82%B0%EC%9E%90)
    - [한 줄 if문조건부 표현식](#%ED%95%9C-%EC%A4%84-if%EB%AC%B8%EC%A1%B0%EA%B1%B4%EB%B6%80-%ED%91%9C%ED%98%84%EC%8B%9D)
      - [한 줄 if문 통해 특정값 제거](#%ED%95%9C-%EC%A4%84-if%EB%AC%B8-%ED%86%B5%ED%95%B4-%ED%8A%B9%EC%A0%95%EA%B0%92-%EC%A0%9C%EA%B1%B0)
      - [파이썬 조건문 내에서의 부등식](#%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A1%B0%EA%B1%B4%EB%AC%B8-%EB%82%B4%EC%97%90%EC%84%9C%EC%9D%98-%EB%B6%80%EB%93%B1%EC%8B%9D)
- [반복문](#%EB%B0%98%EB%B3%B5%EB%AC%B8)
  - [while 문](#while-%EB%AC%B8)
  - [for 문](#for-%EB%AC%B8)
- [함수](#%ED%95%A8%EC%88%98)
      - [람다식 add 함수 구현](#%EB%9E%8C%EB%8B%A4%EC%8B%9D-add-%ED%95%A8%EC%88%98-%EA%B5%AC%ED%98%84)
- [입출력](#%EC%9E%85%EC%B6%9C%EB%A0%A5)
      - [sys 라이브러리를 이용한 입력쥬피터에서는 동작을 안함](#sys-%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EC%9E%85%EB%A0%A5%EC%A5%AC%ED%94%BC%ED%84%B0%EC%97%90%EC%84%9C%EB%8A%94-%EB%8F%99%EC%9E%91%EC%9D%84-%EC%95%88%ED%95%A8)
      - [출력시 오류가 발생하는 소스코드](#%EC%B6%9C%EB%A0%A5%EC%8B%9C-%EC%98%A4%EB%A5%98%EA%B0%80-%EB%B0%9C%EC%83%9D%ED%95%98%EB%8A%94-%EC%86%8C%EC%8A%A4%EC%BD%94%EB%93%9C)
      - [변수를 문자열로 바꾸어 출력하는 소스코드](#%EB%B3%80%EC%88%98%EB%A5%BC-%EB%AC%B8%EC%9E%90%EC%97%B4%EB%A1%9C-%EB%B0%94%EA%BE%B8%EC%96%B4-%EC%B6%9C%EB%A0%A5%ED%95%98%EB%8A%94-%EC%86%8C%EC%8A%A4%EC%BD%94%EB%93%9C)
      - [각 변수를 콤마,로 구분하여 출력하는 소스코드](#%EA%B0%81-%EB%B3%80%EC%88%98%EB%A5%BC-%EC%BD%A4%EB%A7%88%EB%A1%9C-%EA%B5%AC%EB%B6%84%ED%95%98%EC%97%AC-%EC%B6%9C%EB%A0%A5%ED%95%98%EB%8A%94-%EC%86%8C%EC%8A%A4%EC%BD%94%EB%93%9C)
      - [f-string 이용하여 출력하는 소스코드](#f-string-%EC%9D%B4%EC%9A%A9%ED%95%98%EC%97%AC-%EC%B6%9C%EB%A0%A5%ED%95%98%EB%8A%94-%EC%86%8C%EC%8A%A4%EC%BD%94%EB%93%9C)
- [주요 라이브러리의 문법과 유의점](#%EC%A3%BC%EC%9A%94-%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC%EC%9D%98-%EB%AC%B8%EB%B2%95%EA%B3%BC-%EC%9C%A0%EC%9D%98%EC%A0%90)
    - [내장함수](#%EB%82%B4%EC%9E%A5%ED%95%A8%EC%88%98)
    - [itertools](#itertools)
    - [heapq](#heapq)
    - [bisect](#bisect)
    - [collections](#collections)
    - [math](#math)

<!-- /TOC -->

# 자료형

## 수 자료형

### 정수형


```python
# 양의 정수
a = 1000
print(a)
```

    1000



```python
# 음의 정수
a = -7
print(a)
```

    -7



```python
# 0
a = 0
print(a)
```

    0


### 실수형


```python
# 양의 실수
a = 157.93
print(a)
```

    157.93



```python
# 음의 실수
a = -1837.2
print(a)
```

    -1837.2



```python
# 소수부가 0일 때, 0 생략
a = 5.
print(a)
```

    5.0



```python
# 정수부가 0일 때, 0 생략
a = -.7
print(a)
```

    -0.7



```python
# 10억의 지수 표현 방식
a = 1e9
print(a)
```

    1000000000.0



```python
# 752.5
a = 75.25e1
print(a)
```

    752.5



```python
# 3.954
a = 3954e-3
print(a)
```

    3.954



```python
# 컴퓨터는 실수를 정확하게 표현하지 못하기 때문에 round()를 사용
a = 0.3 + 0.6
print(a)

if a == 0.9:
    print(True)
else:
    print(False)

if round(a, 4) == 0.9:
    print(True)
else:
    print(False)    
```

    0.8999999999999999
    False
    True


### 수 자료형의 연산


```python
a = 7
b = 3

# 나누기
print( a / b )

# 나머지
print( a % b )

# 몫
print( a // b )

# 거듭제곱
a = 5
b = 3
print( a ** 3 )
```

    2.3333333333333335
    1
    2
    125


## 리스트 자료형

### 리스트 만들기


```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)

# 인덱스 4, 즉 다섯 번째 요소 접근
print(a[4])

# 빈 리스트 선언 방법 1)
a = list()
print(a)

# 빈 리스트 선언 방법 2)
a = []
print(a)
```

    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    5
    []
    []



```python
# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n
print(a)
```

    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


### 리스트의 인덱싱과 슬라이싱


```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 뒤에서 첫 번째 원소 출력
print(a[-1])

# 뒤에서 세 번째 원소 출력
print(a[-3])

# 네 번째 원소 값 변경
a[3] = 7
print(a)
```

    9
    7
    [1, 2, 3, 7, 5, 6, 7, 8, 9]



```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 두 번째 원소부터 네 번째 원소까지
print(a[1:4])
```

    [2, 3, 4]


### 리스트 컴프리헨션


```python
# 1부터 9까지의 수의 제곱 값을 포함하는 리스트
array = [i * i for i in range(1, 10)]
print(array)
```

    [1, 4, 9, 16, 25, 36, 49, 64, 81]



```python
# N * M 크기의 2차원 리스트 초기화
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)
```

    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


#### 언더바(_)의 역할

반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때 언더바를 자주 사용


```python
# N * M 크기의 2차원 리스트 초기화(잘못된 방법)
n = 3
m = 4
array = [[0]* m]] * n
print(array)

array[1][1] = 5
print(array)
```


      Input In [41]
        array = [[0]* m]] * n
                        ^
    SyntaxError: unmatched ']'



### 리스트 관련 기타 메서드


```python
a = [1, 4, 3]
print('기본 리스트: ',  a)

# 리스트에 원소 삽입 -> O(1)
a.append(2)
print('삽입: ', a)

# 오름차순 정렬 -> O(logN)
a.sort()
print('오름차순 정렬: ', a)

# 내림차순 정렬 -> O(logN)
a.sort(reverse = True)
print('내림차순 정렬: ', a)

# 리스트 원소 뒤집기 -> O(N)
a.reverse()
print('원소 뒤집기: ', a)

# 특정 인덱스에 데이터 추가 -> O(N)
a.insert(2, 3)
print('인덱스 2에 3추가: ', a)

# 특정 값인 데이터 개수 세기 -> O(N)
print('값이 3인 데이터 개수: ', a.count(3))

# 특정 값 데이터 삭제 -> O(N)
a.remove(1)
print('값이 1인 데이터 삭제: ', a)
```

    기본 리스트:  [1, 4, 3]
    삽입:  [1, 4, 3, 2]
    오름차순 정렬:  [1, 2, 3, 4]
    내림차순 정렬:  [4, 3, 2, 1]
    원소 뒤집기:  [1, 2, 3, 4]
    인덱스 2에 3추가:  [1, 2, 3, 3, 4]
    값이 3인 데이터 개수:  2
    값이 1인 데이터 삭제:  [2, 3, 3, 4]


####  리스트 내 특정값 모두 제거


```python
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

# remove_set에 포함되지 않은 값만을 저장
result = [i for i in a if i not in remove_set]
print(result)
```

    [1, 2, 4]


## 문자열 자료형

### 문자열 초기화


```python
data = 'Hello world'
print(data)

data = "Don't you know \"Python\"?"
print(data)
```

    Hello world
    Don't you know "Python"?


### 문자열 연산


```python
a = "Hello"
b = "world"

print(a + ' ' + b)
```

    Hello world



```python
a = "String"
print( a * 3 )
```

    StringStringString



```python
a = "ABCDEF"
print(a[2:4])
```

    CD


## 튜플 자료형

- 튜플은 한 번 선언된 값을 변경불가
- 리스트는 대괄호( "[", "]" )를 이용하지만, 튜플은 소괄호( "(", ")" )를 이용


```python
a = (1, 2, 3, 4)
print(a)

a[2] = 7
```

    (1, 2, 3, 4)



    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Input In [53], in <cell line: 4>()
          1 a = (1, 2, 3, 4)
          2 print(a)
    ----> 4 a[2] = 7


    TypeError: 'tuple' object does not support item assignment


## 사전 자료형

- key, value를 쌍으로 가지고 있는 자료형


```python
data = dict()
data['사과'] = "Apple"
data['바나나'] = "Banana"
data['코코넛'] = "Coconut"

print(data)
```

    {'사과': 'Apple', '바나나': 'Banana', '코코넛': 'Coconut'}



```python
data = dict()
data['사과'] = "Apple"
data['바나나'] = "Banana"
data['코코넛'] = "Coconut"

if '사과' in data:
    print("'사과'를 키로 가지고 있는 데이터가 존재합니다.")
```

    '사과'를 키로 가지고 있는 데이터가 존재합니다.


### 사전 자료형 관련 함수


```python
data = dict()
data['사과'] = "Apple"
data['바나나'] = "Banana"
data['코코넛'] = "Coconut"

# 키 데이터만 담은 리스트
print(data.keys())

# 값 데이터만 담은 리스트
print(data.values())

# 각 키에 따른 값을 하나씩 출력
for key in data:
    print(key, ': ', data[key])
```

    dict_keys(['사과', '바나나', '코코넛'])
    dict_values(['Apple', 'Banana', 'Coconut'])
    사과 :  Apple
    바나나 :  Banana
    코코넛 :  Coconut


## 집합 자료형

- 중복을 허용 불가
- 순서 없음


```python
# 집합 자료형 초기화 방법 1
data = set([1, 1, 2, 3, 4, 4, 5])
print(data)

# 집합 자료형 초기화 방법 2
data = {1, 1, 2, 3, 4, 4, 5}
print(data)
```

    {1, 2, 3, 4, 5}
    {1, 2, 3, 4, 5}


### 집합 자료형의 연산


```python
a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

print(a | b) # 합집합
print(a & b) # 교집합
print(a - b) # 차집합
```

    {1, 2, 3, 4, 5, 6, 7}
    {3, 4, 5}
    {1, 2}


### 집합 자료형 관련 함수


```python
data = set([1, 2, 3])
print(data)

# 새로운 원소 추가
data.add(4)
print(data)

# 새로운 원소 여러 개 추가
data.update([5, 6])

# 특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)
```

    {1, 2, 3}
    {1, 2, 3, 4}
    {1, 2, 4, 5, 6}


# 조건문


```python
x = 15

if x >= 10:
    print(x)
```

    15



```python
score = 85

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
else:
    print('F')
```

    B


## 비교 연산자

- X == Y
- X != Y
- X > Y
- X < Y
- X >= Y
- X <= Y

## 논리 연산자

- X and Y
- X or Y
- not X

## 파이썬 기타 연산자

- X in 리스트  
  리스트 안에 X가 있을때 True
- X not in 리스트  
    리스트 안에 X가 없을때 True

### 한 줄 if문(조건부 표현식)


```python
score = 85

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
else:
    print('F')

if score >= 80: result = "Success"
else: result = "Fail"
print(result)

result = "Success" if score >= 80 else "Fail"
print(result)
```

    B
    Success
    Success


#### 한 줄 if문 통해 특정값 제거


```python
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = []
for i in a:
    if i not in remove_set:
        result.append(i)
print(result)
```

    [1, 2, 4]



```python
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

# remove_set에 포함되지 않은 값만을 저장
result = [i for i in a if i not in remove_set]
print(result)
```

    [1, 2, 4]


#### 파이썬 조건문 내에서의 부등식


```python
x = 15
if x > 0 and x < 20:
    print("15")

if 0 < x < 20:
    print("15")
```

    15
    15


# 반복문

## while 문


```python
i = 1
result = 0

while i <= 9:
    result += 1
    i += 1
print(result)
```

    9



```python
i = 1
result = 0

while i <= 9:
    if i % 2 == 1:
        result += 1
    i += 1
print(result)
```

    5


## for 문


```python
result = 0

for i in range(1, 10):
    result += i
print(result)
```

    45



```python
scores = [90, 85, 77, 65, 97]
cheating_list = {2, 4}

for i in range(len(scores)):
    if  i + 1 in cheating_list:
        continue
    if scores[i] >= 80:
        print(i+1, '번 학생 합격')
    
```

    1 번 학생 합격
    5 번 학생 합격



```python
for i in range(2, 10):
    for j in range(1, 10):
        print(i, 'X', j, '=', i * j )
# 구구단 실행결과 생략
```

# 함수


```python
def add(a, b):
    return a + b
print(add(b=3, a=7))
```

    10



```python
a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()
    
print(a)
```

    10



```python
# 일반적인 add() 메서드 사용
def add(a, b):
    return a + b
print(add(3, 7))
```

    10


#### 람다식 add() 함수 구현


```python
# 람다 표현식으로 구현한 add() 메서드
print((lambda a, b: a + b)(3, 7))
```

    10


# 입출력


```python
# 데이터 개수 입력
n = int(input())
# 각 데이터를 공백으로 구분하여 입력
data = list(map(int, input().split()))

data.sort(reverse = True)
print(data)
```

    5
    65 90 75 34 99
    [99, 90, 75, 65, 34]



```python
# n, m k를 공백으로 구분하여 적은 수의 데이터 입력
n, m, k = map(int, input().split())

print(n, m, k)
```

    1 2 3
    1 2 3


#### sys 라이브러리를 이용한 입력(쥬피터에서는 동작을 안함)


```python
import sys
sys.stdin.readline().rstrip()
```




    ''




```python
import sys
data = sys.stdin.readline().rstrip()
print(data)
```

    


#### 출력시 오류가 발생하는 소스코드


```python
answer = 7
print('정답은 ' + answer + '입니다.')
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Input In [119], in <cell line: 2>()
          1 answer = 7
    ----> 2 print('정답은 ' + answer + '입니다.')


    TypeError: can only concatenate str (not "int") to str


#### 변수를 문자열로 바꾸어 출력하는 소스코드


```python
answer = 7
print('정답은 ' + str(answer) + '입니다.')
```

    정답은 7입니다.


#### 각 변수를 콤마(,)로 구분하여 출력하는 소스코드


```python
answer = 7
print('정답은 ', answer, '입니다.')
```

    정답은  7 입니다.


#### f-string 이용하여 출력하는 소스코드


```python
answer = 7
print(f'정답은 {answer}입니다.')
```

    정답은 7입니다.


# 주요 라이브러리의 문법과 유의점

- 표준 라이브러리  
  특정한 프로그래밍 언어에서 자주 사용되는 표준 소스코드를 미리 구현해 놓은 라이브러리
- 내장 함수: print(), input()과 같은 기본 입출력 기능부터 sorted()와 같은 정렬 기능을 포함하고 있는 기본 내장 라이브러리
- itertools: 파이썬에서 반복되는 형태의 데이터를 처리하는 기능을 제공하는 라이브러리
- heapq: 힙 기능을 제공하는 라이브러리, 우선순위 큐 기능을 구현하기 위해 사용
- bisect: 이진탐색 기능을 제공하는 라이브러리
- collections: 덱(deque), 카운터(counter) 등의 유용한 자료구조를 포함하고 있는 라이브러리
- math: 필수적인 수학적 기능을 제공하는 라이브러리, 팩토리얼, 제곱근, 최대공약수, 삼각함수 관련 함수부터 파이 같은 상수도 포함

### 내장함수


```python
result = sum([1, 2, 3, 4, 5])
print('sum', result)

result = min(7, 3, 5, 2)
print('min', result)

result = max(7, 3, 5, 2)
print('max', result)

# 수학식이 문자열로 들어오면 처리
result = eval("(3+5)*7")
print('eval', result)

# 오름차순 정렬
result = sorted([9, 1, 8, 5, 4])
print(result)

# 내림차순 정렬
result = sorted([9, 1, 8, 5, 4], reverse = True)
print(result)

# 람다식 정렬
result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key = lambda x: x[1], reverse = True)
print(result)

# 리스트 내부값 정렬
data = [9, 1, 8, 5, 4]
data.sort()
print(data)
```

    sum 15
    min 2
    max 7
    eval 56
    [1, 4, 5, 8, 9]
    [9, 8, 5, 4, 1]
    [('이순신', 75), ('아무개', 50), ('홍길동', 35)]
    [1, 4, 5, 8, 9]


### itertools


```python
from itertools import permutations

# 데이터 준비
data = ['A', 'B', 'C']

# 모든 순열 구하기
result = list(permutations(data, 3))

print(result)
```

    [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]



```python
from itertools import combinations

# 데이터 준비
data = ['A', 'B', 'C']

# 2개를 뽑는 모든 조합 구하기
result = list(combinations(data, 2))

print(result)
```

    [('A', 'B'), ('A', 'C'), ('B', 'C')]



```python
from itertools import product

# 데이터 준비
data = ['A', 'B', 'C']

# 2개를 뽑는 모든 순열 구하기(중복 허용)
result = list(product(data, repeat = 2))

print(result)
```

    [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]



```python
from itertools import combinations_with_replacement

# 데이터 준비
data = ['A', 'B', 'C']

# 2개를 뽑는 모든 순열 구하기(중복 허용)
result = list(combinations_with_replacement(data, 2))

print(result)
```

    [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]


### heapq


```python
# 힙에 넣었다 빼는것만으로도 O(NlogN의 오름차순 정렬이 완료

import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 요소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



```python
# 힙에 -로 넣었다 -로 빼는것만으로도 O(NlogN의 내림차순 정렬이 완료


import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 요소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
    
```

    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


### bisect


```python
# bisect_left, bisect_right 는 O(logN)으로 삽입한
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))
```

    2
    4



```python
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인  데이터틔 개수를 반환하는 함수
def county_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 리스트 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(county_by_range(a, 4, 4))

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(county_by_range(a, -1, 3))
```

    2
    6


### collections


```python
from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data)) # 리스트 자료형으롭 변환

```

    deque([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]



```python
from collections import Counter

counter = Counter(['red', 'blue', 'green', 'blue', 'blue'])

print(counter['blue'])  # 'blue'가 등장한 횟수 출력
print(counter['green']) # 'green'이 등장한 횟수 출력
print(dict[counter])    # 사전 자료형으로 변환
```

    3
    1
    dict[Counter({'blue': 3, 'red': 1, 'green': 1})]


### math


```python
import math

print(math.factorial(5)) # 5 팩토리얼을 출력
```

    120



```python
import math

print(math.sqrt(7)) # 7의 제곱근을 출력
```

    2.6457513110645907



```python
import math

print(math.gcd(21, 14)) # 최대 공약수
```

    7



```python
import math

print(math.pi) # 파이(pi) 출력
print(math.e)  # 자연 상수 e 출력
```

    3.141592653589793
    2.718281828459045

