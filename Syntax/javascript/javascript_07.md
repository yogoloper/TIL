<!-- TOC -->

- [Object](#object)
  - [Literals and properties](#literals-and-properties)
  - [Computed properties](#computed-properties)
  - [Property value shorthand](#property-value-shorthand)
  - [Constructor Function](#constructor-function)
  - [in operator: property existence check key in obj](#in-operator-property-existence-check-key-in-obj)
  - [for..in vs for..of](#forin-vs-forof)
  - [Fun cloning](#fun-cloning)

<!-- /TOC -->

# Object
- 자바스크립트의 데이터 타입중 하나이다.
- 관련 데이터/기능의 모음이며, 자바스크립트의 대부분의 객체는 Object의 인스턴스이다.
- **Object는 key와 value의 집합체**  
  -> **JOSN 형태**
## Literals and properties
- Object 생성 방법
  - object literal syntax vs object constructor syntax
  - class 없이 바로 object 생성
  - properties add / delete  
    -> 이렇게 동적으로 추가/삭제를 하게되면 프로그램 작성에 혼동을 주게 된다.
``` javascript
// object.js

// object = { key : value };
const obj1 = {}; // 'object literal' syntax
const obj2 = new Object(); // 'object constructor' syntax

function print(person) {
  console.log(person.name);
  console.log(person.age);
}

// class 없이 바로 object 생성
const ellie = { name: 'ellie', age: 4 };
print(ellie);

// with JavaScript magic (dynamically typed language)
// can add properties later
ellie.hasJob = true;
console.log(ellie.hasJob);

// can delete properties later
delete ellie.hasJob;
console.log(ellie.hasJob);
```

## Computed properties
- 계산된 프로퍼티
- object의 키에는 .연산 또는 ['string'] 로 접근이 가능하다.
  - . 연산 : 해당하는 키에 값을 받아올때 사용
  - conputed properties : 정확히 어떤 키가 필요한지 모를때 사용 -> 런타임에서 결정해야 할때 사용
``` javascript
// object.js

// key should be always string
console.log(ellie.name);
console.log(ellie['name']);
ellie['hasJob'] = true;
console.log(ellie.hasJob);

// 사용자에게 카를 입력 받을때 .연산을 사용하면 에러가 난다.
// conputed properties를 사용하면 
function printValue(obj, key) {
  console.log(obj.key); // undefined
  console.log(obj[key]); // ellie / 4 정상 출력
printValue(ellie, 'name');
printValue(ellie, 'age');
```


## Property value shorthand
- key와 value의 이름이 같다면 한 번만 적는다. 
  -> return { name : name } => return { name }
``` javascript
// object.js

const person1 = { name: 'bob', age: 2 };
const person2 = { name: 'steve', age: 3 };
const person3 = { name: 'dave', age: 4 };
console.log(person4);

fucntion makePerson(name, age) {
  return {
    // Property value shorthand
    // this.name: name,
    // this.age: age
    name,
    age
  }
}
```

## Constructor Function
- 생성자 함수
  - 대문자로 시작
``` javascript
// object.js

function Person(name, age) {
  // this = {};
  this.name = name;
  this.age = age;
  // return this;
}
const person4 = new Person('elile', 30);
```

## in operator: property existence check (key in obj)
- object 안에 해당 key가 있는지 확인
``` javascript
// object.js

console.log('name' in ellie);
console.log('age' in ellie);
console.log('random' in ellie);
console.log(ellie.random);
```

## for..in vs for..of
- 반복
- for (key in obj)  
  object 안의 모든 키들을 출력
- for (value of iterable)  
  iterable object 안의 모든 값들을 출력

``` javascript
// object.js

// for (key in obj)
console.clear();
for (let key in ellie) {
  console.log(key);
}

// for (value of iterable)
const array = [1, 2, 4, 5];
for (let value of array) {
  console.log(value);
}
```

## Fun cloning
- object 복제
  - old way
  - Object.assign()
``` javascript
// object.js

// Object.assign(dest, [obj1, obj2, obj3...])
const user = { name: 'ellie', age: '20' };
const user2 = user; // user의 레퍼런스를 저장 -> 레퍼런스는 object를 가리킴
console.log(user);

// old way
// 오브젝트를 통째로 반복하며 복사
const user3 = {};
for (let key in user) {
  user3[key] = user[key];
}
console.clear();
console.log(user3);

const user4 = Object.assign({}, user);
console.log(user4);

// another example
const fruit1 = { color: 'red' };
const fruit2 = { color: 'blue', size: 'big' };
const mixed = Object.assign({}, fruit1, fruit2); // fruit1을 먼저 복제하고 fruite2를 복제하기 때문에 coloer는 blue가 된다.
console.log(mixed.color);
console.log(mixed.size);
```