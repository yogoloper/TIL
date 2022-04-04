<!-- TOC -->

- [Operator, Condition, Loop](#operator-condition-loop)
  - [Operator](#operator)
    - [String concatenation](#string-concatenation)
    - [Numeric operators](#numeric-operators)
    - [Increment and decrement operators](#increment-and-decrement-operators)
    - [Assignment operators](#assignment-operators)
    - [Comparison operators](#comparison-operators)
    - [Logical operators: || or, && and, ! not](#logical-operators--or--and--not)
      - [쇼트 서킷 Short Circuit](#%EC%87%BC%ED%8A%B8-%EC%84%9C%ED%82%B7-short-circuit)
    - [Equality](#equality)
  - [Condition](#condition)
    - [Conditional operators: if](#conditional-operators-if)
    - [Ternary operator: ?](#ternary-operator-)
    - [Switch statement](#switch-statement)
  - [Loop](#loop)
    - [while / do while](#while--do-while)
    - [for](#for)
    - [continue / break](#continue--break)

<!-- /TOC -->

# Operator, Condition, Loop

## Operator
### String concatenation  
- `+` 기호를 통해서 문자열을 합칠 수 있다.
``` javascript
// operator.js

console.log('my' + ' cat');
console.log('1' + 2);
console.log(`string literals: 1 + 2 = ${1 + 2}`);
```

### Numeric operators
- Number의 기본 연산
``` javascript
// operator.js

console.log(1 + 1); // add
console.log(1 - 1); // substract
console.log(1 / 1); // divide
console.log(1 * 1); // multiply
console.log(5 % 2); // remainder
console.log(2 ** 3); // exponentiation
```

### Increment and decrement operators
- Number의 전위증가, 후위증가
``` javascript
// operator.js

let counter = 2;
const preIncrement = ++counter;
// counter = counter + 1;
// preIncrement = counter;
console.log(`preIncrement: ${preIncrement}, counter: ${counter}`);
const postIncrement = counter++;
// postIncrement = counter;
// counter = counter + 1;
console.log(`postIncrement: ${postIncrement}, counter: ${counter}`);
const preDecrement = --counter;
console.log(`preDecrement: ${preDecrement}, counter: ${counter}`);
const postDecrement = counter--;
console.log(`postDecrement: ${postDecrement}, counter: ${counter}`);
```

### Assignment operators
- 할당 연산자
``` javascript
// operator.js

let x = 3;
let y = 6;
x += y; // x = x + y;
x -= y;
x *= y;
x /= y;
```

### Comparison operators
- 비교 연산자
``` javascript
// operator.js

console.log(10 < 6); // less than
console.log(10 <= 6); // less than or equal
console.log(10 > 6); // greater than
console.log(10 >= 6); // greater than or equal
```

### Logical operators: || (or), && (and), ! (not)
- 논리 연산자  
``` javascript
// operator.js

const value1 = true;
const value2 = 4 < 2;

// || (or), finds the first truthy value
console.log(`or: ${value1 || value2 || check()}`);

// && (and), finds the first falsy value
console.log(`and: ${value1 && value2 && check()}`);

// often used to compress long if-statement
// nullableObject && nullableObject.something

function check() {
  for (let i = 0; i < 10; i++) {
    //wasting time
    console.log('😱');
  }
  return true;
}

// ! (not)
console.log(!value1);
```
#### 쇼트 서킷( Short Circuit )
- and, or 같은 논리연산자에서 이미 경정난 값에 대해서  
  불피요한 연산을 하지 않음으로써 실행 속도를 높이는 기술
- and는 첫 값이 false, or는 첫 값이 true면 뒤의 연산을 진행하지 않는다.  
  따라서, 쉽게 조사 할 수 있는 조건을 앞쪽에 두어야 한다.


### Equality
- 비교연산
``` javascript
// operator.js

const stringFive = '5';
const numberFive = 5;

// == loose equality, with type conversion
// 타입을 변경해서 비교해준다.
console.log(stringFive == numberFive);
console.log(stringFive != numberFive);

// === strict equality, no type conversion
// 타입을 변경하지 않은 상태에서 비교해준다.
console.log(stringFive === numberFive);
console.log(stringFive !== numberFive);

// object equality by reference
const ellie1 = { name: 'ellie' };
const ellie2 = { name: 'ellie' };
const ellie3 = ellie1;
console.log(ellie1 == ellie2); // false: 각각 다른 레퍼런스가 있기 때문
console.log(ellie1 === ellie2); // false: 레퍼런스 값이 다르기 때문
console.log(ellie1 === ellie3); // true: 같은 레퍼런스를 보기 때문

// equality - puzzler
console.log(0 == false);  // true
console.log(0 === false); // false
console.log('' == false); // true
console.log('' === false); // false
console.log(null == undefined); // true
console.log(null === undefined); // false
``` 

## Condition
### Conditional operators: if
``` javascript
// operator.js

// if, else if, else
const name = 'df';
if (name === 'ellie') {
  console.log('Welcome, Ellie!');
} else if (name === 'coder') {
  console.log('You are amazing coder');
} else {
  console.log('unkwnon');
}
```

### Ternary operator: ?
- 삼항 연산자
``` javascript
// operator.js
// condition ? value1 : value2;
console.log(name === 'ellie' ? 'yes' : 'no');
```

### Switch statement
``` javascript
// operator.js

// use for multiple if checks
// use for enum-like value check
// use for multiple type checks in TS
const browser = 'IE';
switch (browser) {
  case 'IE':
    console.log('go away!');
    break;
  case 'Chrome':
  case 'Firefox':
    console.log('love you!');
    break;
  default:
    console.log('same all!');
    break;
}
```

## Loop
### while / do while

``` javascript
// operator.js

// while loop, while the condition is truthy,
// body code is executed.
let i = 3;
while (i > 0) {
  console.log(`while: ${i}`);
  i--;
}

// do while loop, body code is executed first,
// then check the condition.
do {
  console.log(`do while: ${i}`);
  i--;
} while (i > 0);

```

### for
``` javascript 
// operator.js

// for loop, for(begin; condition; step)
for (i = 3; i > 0; i--) {
  console.log(`for: ${i}`);
}

for (let i = 3; i > 0; i = i - 2) {
  // inline variable declaration
  console.log(`inline variable for: ${i}`);
}

// nested loops
for (let i = 0; i < 10; i++) {
  for (let j = 0; j < 10; j++) {
    console.log(`i: ${i}, j:${j}`);
  }
}

```
### continue / break
``` javascript
// operator.js

// Q1. iterate from 0 to 10 and print only even numbers (use continue)
for (let i = 0; i < 11; i++) {
  if (i % 2 === 0) {
    continue;
  }
  console.log(`q1. ${i}`);
}

// Q2. iterate from 0 to 10 and print numbers until reaching 8 (use break)
for (let i = 0; i < 11; i++) {
  if (i > 8) {
    break;
  }
  console.log(`q2. ${i}`);
}
```