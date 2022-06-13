<!-- TOC -->

- [호이스팅](#%ED%98%B8%EC%9D%B4%EC%8A%A4%ED%8C%85)

<!-- /TOC -->

# 호이스팅
~~함수가 실행되기 전에 함수 안에 있는 선언들을 모두 끌어올려서 해당 함수 유효 범위 최상단에 선언하는 것을 말한다.~~

**인터프리터가 변수와 함수의 메모리 공간을 선언 전에 미리 할당하는 것을 의미한다.**  
var로 선언한 변수의 경우 호이스팅 시 undefined로 변수를 초기화한다. 반면 let과 const로 선언한 변수의 경우 호이스팅 시 변수를 초기화하지 않는다.

띠라서 var를 함수 표현식으로 작성하게 되면 호이스팅 시 undefiend가 할당되므로 'func is not a function' 에러가 발생한다.
``` javascript 
func();

var func = function () {
  console.log('hello world');
};
```
let으로 함수 표현식을 작성하게 되면 호이스팅 시 변수를 초기화 하지 않아, 'Cannot access 'func' before initialization' 초기화 에러가 발생한다.
``` javascript
func();

let func = function () {
  console.log('hello world');
};
```