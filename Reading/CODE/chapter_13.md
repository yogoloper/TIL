# [CODE] Chapter13 : 그렇다면 뺄셈은 어떨까요? - 2022.03.25

<!-- TOC -->

- [[CODE] Chapter13 : 그렇다면 뺄셈은 어떨까요? - 2022.03.25](#code-chapter13--%EA%B7%B8%EB%A0%87%EB%8B%A4%EB%A9%B4-%EB%BA%84%EC%85%88%EC%9D%80-%EC%96%B4%EB%96%A8%EA%B9%8C%EC%9A%94---20220325)
  - [뺄셈](#%EB%BA%84%EC%85%88)
    - [내림수](#%EB%82%B4%EB%A6%BC%EC%88%98)
    - [보수를 이용한 뺄셈](#%EB%B3%B4%EC%88%98%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EB%BA%84%EC%85%88)
    - [이진수로 빼기](#%EC%9D%B4%EC%A7%84%EC%88%98%EB%A1%9C-%EB%B9%BC%EA%B8%B0)
    - [2의 보수 = 1의 보수 + 1](#2%EC%9D%98-%EB%B3%B4%EC%88%98--1%EC%9D%98-%EB%B3%B4%EC%88%98--1)
    - [2의 보수 만드는 법](#2%EC%9D%98-%EB%B3%B4%EC%88%98-%EB%A7%8C%EB%93%9C%EB%8A%94-%EB%B2%95)
    - [오버플로우/언더플로우](#%EC%98%A4%EB%B2%84%ED%94%8C%EB%A1%9C%EC%9A%B0%EC%96%B8%EB%8D%94%ED%94%8C%EB%A1%9C%EC%9A%B0)
    - [Signed/Unsigned](#signedunsigned)
  - [숙고](#%EC%88%99%EA%B3%A0)

<!-- /TOC -->

## `뺄셈`
### `내림수`
뺄셈은 덧셈과 달리 올림수가 아닌 내림수가 필요하다.

### `보수를 이용한 뺄셈`
253 - 176  
= 253 -176 + 1000 - 1000  
= 253 - 176 + 999 + 1 - 1000  
= 253 - (176 + 999) + 1 - 1000   

176 - 253  
= 999 - ((999 - 253) + 176)  
= 77 을 음수로 취급

### `이진수로 빼기`
176 - 253  
= 10110000 - 11111101  
= 11111111 - ((11111111 - 11111101) + 10110000)  
= 01001101 을 음수로 취급

### `2의 보수 = 1의 보수 + 1`
- 10진수 1000으로 -500 에서 499 까지 표현 **(10의 보수)**  
  -500 = 500  
  -499 = 501  
  -498 = 502  
  
  ...  
  
  -2 = 998  
  -1 = 999  
  0 = 000  
  1 = 001  
  2 = 002   
  
  ...  
  
  497 = 497  
  498 = 498  
  499 = 499  
- 8비트 2진수로 -128 에서 127까지 표현 **(2의 보수)**  
  1000 0000 = -128  
  1000 0001 = -127  
  
  ...  
  
  1111 1110 = -2  
  1111 1111 = -1  
  0000 0000 = 0  
  0000 0001 = 1  
  0000 0010 = 2  
  
  ...  
  
  0111 1101 = 125  
  0111 1110 = 126  
  0111 1111 = 127  

### `2의 보수 만드는 법`
1의 보수로 전환 후 1을 더한다. 

### `오버플로우/언더플로우`
8비트로 표현할 수 없는 덧셈/뺄셈을 하면 비트를 벗어나게 되는데  
이것을 **오버플로우/언더플로우** 라고 한다.

### `Signed/Unsigned`
8비트로 -128 ~ 127 까지 표현하면 Signed  
8비트로 0 ~ 255까지 표현하면 Unsigned

## `숙고`
곱셈과 나눗셈은 먼 나중에 공부해보자..