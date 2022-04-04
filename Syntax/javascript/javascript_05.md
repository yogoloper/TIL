<!-- TOC -->

- [함수 선언식, 함수 표현식, Arrow Function](#%ED%95%A8%EC%88%98-%EC%84%A0%EC%96%B8%EC%8B%9D-%ED%95%A8%EC%88%98-%ED%91%9C%ED%98%84%EC%8B%9D-arrow-function)
  - [function](#function)
  - [function 정의 방법](#function-%EC%A0%95%EC%9D%98-%EB%B0%A9%EB%B2%95)
  - [Function declaration](#function-declaration)
    - [Parameters](#parameters)
    - [Default parameters added in ES6](#default-parameters-added-in-es6)
    - [Rest parameters added in ES6](#rest-parameters-added-in-es6)
    - [Local scope](#local-scope)
    - [Return a value](#return-a-value)
    - [Early return, early exit](#early-return-early-exit)
  - [Function expression](#function-expression)
    - [Callback function using function expression](#callback-function-using-function-expression)
    - [anonymous function](#anonymous-function)
    - [named function](#named-function)
    - [IIFE: Immediately Invoked Function Expression](#iife-immediately-invoked-function-expression)
  - [Arrow function](#arrow-function)

<!-- /TOC -->

# 함수 선언식, 함수 표현식, Arrow Function
## function
- 프로그램을 구성하는 빌딩 블럭
- sub-program 이라고도 불리며,  
  프로그램 안에서 각각의 작은 단위의 기능들을 수행
- input을 받아 연산 후 output을 반환
- 재사용성 용이

## function 정의 방법
- 한 가지 기능만 수행 하도록 만들어야 한다.
- 명령형(동사형)으로 이름을 지어야 한다.
- **함수는 Object** 이기 때문에 변수에 넣을 수도 있고,  
  파라미터로 전달, 함수에서의 반환이 가능하다.

## Function declaration
- **함수 선언식**
- **호이스팅**  
  -> 함수 선언식은 함수를 정의하기 이전에 호출하더라도 함수 호출이 가능하다.
``` javascript 
// function.js

// function name(param1, param2) { body... return; }
// one function === one thing
// naming: doSomething, command, verb
// e.g. createCardAndPoint -> createCard, createPoint
// function is object in JS
function printHello() {
  console.log('Hello');
}
printHello();

function log(message) {
  console.log(message);
}
log('Hello@');
log(1234);
```

### Parameters
- primitive 타입은 값을 전달,  
  object 타입은 레퍼런스를 전달한다.  
``` javascript 
// function.js

// primitive parameters: passed by value
// object parameters: passed by reference
function changeName(obj) {
  obj.name = 'coder';
}
const ellie = { name: 'ellie' };
changeName(ellie);
console.log(ellie);
```

### Default parameters (added in ES6)
- 기본 파라미터 설정  
  파라미터가 전달되지 않으면 기본 값으로 대체된다.  
``` javascript 
// function.js

function showMessage(message, from = 'unknown') {
  console.log(`${message} by ${from}`);
}
showMessage('Hi!');
```

### Rest parameters (added in ES6)
- ...args를 하면 파라미터를 변수 형태로 전달한다.  
``` javascript 
// function.js

function printAll(...args) {
  for (let i = 0; i < args.length; i++) {
    console.log(args[i]);
  }

  for (const arg of args) {
    console.log(arg);
  }

  args.forEach((arg) => console.log(arg));
}
printAll('dream', 'coding', 'ellie');
```

### Local scope
- 밖에서는 안을 볼 수 없고,  
  안에서만 밖을 볼 수 있다.  
  -> 블록 안에서만 밖의 변수에 접근이 가능하다.  
``` javascript 
// function.js

let globalMessage = 'global'; // global variable
function printMessage() {
  let message = 'hello'; // local variable
  console.log(message); 
  console.log(globalMessage);
  function printAnother() {
    console.log(message);
    let childMessage = 'hello';
  }
  // console.log(childMessage); //error
}
printMessage();
```

### Return a value
- 리턴 타입이 없는 함수들은 사실 **return undefined** 가 생략되어 있다.  
``` javascript 
// function.js

function sum(a, b) {
  return a + b;
}
const result = sum(1, 2); // 3
console.log(`sum: ${sum(1, 2)}`);
```

### Early return, early exit
- 조건이 맞지 않을 때는 함수를 빨리 종료 시킨다.  
``` javascript 
// function.js

// bad
function upgradeUser(user) {
  if (user.point > 10) {
    // long upgrade logic...
  }
}

// good
function upgradeUser(user) {
  if (user.point <= 10) {
    return;
  }
  // long upgrade logic...
}
```

## Function expression
- **함수 표현식**  
  함수를 변수에 담는 형태
- 함수 표현식은 할당 된 다음부터 사용이 가능하다.
``` javascript
// function.js

// a function declaration can be called earlier than it is defined. (hoisted)
// a function expression is created when the execution reaches it.
const print = function () { 
  // anonymous function
  console.log('print');
};
print();
const printAgain = print;
printAgain();
const sumAgain = sum;
console.log(sumAgain(1, 3));
```

### Callback function using function expression
- 함수를 파라미터로 전달해서 상황에 맞게 전달된 함수를 호출한다.
``` javascript
// function.js

function randomQuiz(answer, printYes, printNo) {
  if (answer === 'love you') {
    printYes();
  } else {
    printNo();
  }
}
```
### anonymous function
- 함수에 이름이 없는 함수(익명함수)  
  -> 보통 변수에 담아서 사용한다.
``` javascript
// function.js

// anonymous function
const printYes = function () {
  console.log('yes!');
};
```
### named function
- 함수에 이름이 있는 함수
  -> 디버깅할때 함수 이름을 볼 수 있어 용이하다.
- 함수 내부에서 **재귀호출**을 하기 위해서는 함수의 이름을 지정해 주어야 한다.
``` javascript
// function.js

// named function
// better debugging in debugger's stack traces
// recursions
const printNo = function print() {
  console.log('no!');
  // print()
};
randomQuiz('wrong', printYes, printNo);
randomQuiz('love you', printYes, printNo);
```

### IIFE: Immediately Invoked Function Expression
- 함수 선언과 동시에 호출
``` javascript 
// function.js

// named function
(function hello() {
  console.log('IIFE');
})();

// anonymous function
(function () {
  console.log('IIFE');
})();
```

## Arrow function
- **화살표 함수**
- 화살표 형태로 간결하게 함수를 만든다.  
- 화살표 함수는 **항상 익명함수 형태** 이다.
``` javascript 
// function.js

// always anonymous
// const simplePrint = function () {
//   console.log('simplePrint!');
// };
const simplePrint = () => console.log('simplePrint!');
const add = (a, b) => a + b;
const simpleMultiply = (a, b) => {
  // do something more
  return a * b;
};
```