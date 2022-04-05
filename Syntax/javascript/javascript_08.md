<!-- TOC -->

- [Array](#array)
  - [자료구조](#%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0)
  - [Declaration](#declaration)
  - [Index position](#index-position)
  - [Looping over an array](#looping-over-an-array)
  - [Addtion, deletion, copy](#addtion-deletion-copy)
  - [Searching](#searching)

<!-- /TOC -->

# Array
- 칸칸이 모여있는 자료구조
## 자료구조
- 자료구조 vs object
  - 자료구조 : 비슷한 종류의 object를 묶음
  - object : 서로 연관된 특징과 행동을 묶음

## Declaration
- 선언 방법
  - object 생성 방식
  - 대괄호 통해서 생성
``` javascript
// array.js

const arr1 = new Array();
const arr2 = [1, 2];
```

## Index position
- 인덱스
``` javascript
// array.js

const fruits = ['🍎', '🍌'];
console.log(fruits); // 🍎, 🍌
console.log(fruits.length); // 2
console.log(fruits[0]); // 🍎
console.log(fruits[1]); // 🍌
console.log(fruits[2]); // undefined
console.log(fruits[fruits.length - 1]); // 🍌
console.clear();
```

## Looping over an array
- for  
  이전에 많이 사용했던 방식
- for of  
- forEach  
  배열 안에 들어있는 원소들마다 전달한 (콜백)함수를 출력한다.
  주로 arrow function을 통해서 콜백 함수를 호출
``` javascript
// array.js

// print all fruits
// a. for
for (let i = 0; i < fruits.length; i++) {
  console.log(fruits[i]);
}

// b. for of
for (let fruit of fruits) {
  console.log(fruit);
}

// c. forEach
fruits.forEach((fruit) => console.log(fruit));

// fruits.forEach(function(fruit, index, array) {
//   console.log(fruit, index, array); // (🍎, 0, ['🍎', '🍌']), (🍌, 1, ['🍎', '🍌'])
// });
```

## Addtion, deletion, copy
- addition  
  push(a)  
  unshift(a) : 앞에서부터 데이터 입력 (재정렬하므로 매우 느린 연산)
  splice(a, b, c, d) : a인덱스에서 b개의 원소 삭제 후, c, d 삽입
- delettion
  pop() : 지우면서 지운 원소 반환
  shift() : 앞에서부터 데이터 삭제 (재정렬하므로 매우 느린 연산)
  splice(a, b) : a 인덱스에서 b개의 원소를 삭제, b 없으면 a부터 모두 삭제
- copy
  a.concat(b) : a 배열 뒤에 b 배열 추가
``` javascript
// array.js

// push: add an item to the end
fruits.push('🍓', '🍑');
console.log(fruits);

// pop: remove an item from the end
const poped = fruits.pop();
fruits.pop();
console.log(fruits);

// unshift: add an item to the benigging
fruits.unshift('🍓', '🍋');
console.log(fruits);

// shift: remove an item from the benigging
fruits.shift();
fruits.shift();
console.log(fruits);

// note!! shift, unshift are slower than pop, push
// splice: remove an item by index position
fruits.push('🍓', '🍑', '🍋');
console.log(fruits);
fruits.splice(1, 1);
console.log(fruits);
fruits.splice(1, 0, '🍏', '🍉');
console.log(fruits);

// combine two arrays
const fruits2 = ['🍐', '🥥'];
const newFruits = fruits.concat(fruits2);
console.log(newFruits);
```

## Searching
- indexOf(a) : a가 **앞에서부터** 몇 번째 있는지 확인, 없으면 -1 반환
- includes(a) : a가 배열에 있으면 true, 없으면 false
- lastIndexOf(a) : a가 **뒤에서부터** 몇 번째 있는지 확인, 없으면 -1 반환
``` javascript
// array.js

// indexOf: find the index
console.clear();
console.log(fruits);
console.log(fruits.indexOf('🍎'));
console.log(fruits.indexOf('🍉'));
console.log(fruits.indexOf('🥥'));

// includes
console.log(fruits.includes('🍉'));
console.log(fruits.includes('🥥'));

// lastIndexOf
console.clear();
fruits.push('🍎');
console.log(fruits);
console.log(fruits.indexOf('🍎'));
console.log(fruits.lastIndexOf('🥥'));
```