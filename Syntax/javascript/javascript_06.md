<!-- TOC -->

- [Class, Object, OOP](#class-object-oop)
  - [Class](#class)
  - [Class와 Object의 관계](#class%EC%99%80-object%EC%9D%98-%EA%B4%80%EA%B3%84)
    - [Class declarations](#class-declarations)
    - [Getter and Setter](#getter-and-setter)
      - [getter, setter 주의 할 점](#getter-setter-%EC%A3%BC%EC%9D%98-%ED%95%A0-%EC%A0%90)
    - [Fields public, private](#fields-public-private)
    - [Static properties and methods](#static-properties-and-methods)
    - [Inheritance & Polymorphism](#inheritance--polymorphism)
      - [inheritance](#inheritance)
      - [Polymorphism](#polymorphism)
    - [Class checking: instanceOf](#class-checking-instanceof)
      - [Object](#object)

<!-- /TOC -->

# Class, Object, OOP

## Class
- 연관있는 데이터를 한데 묶어 놓은 것  
  -> fields(속성)와 methods(행동)가 종합적으로 묶여져 있다.
- 자바스크립트에는 **ES6부터 적용** 되었다.  
  -> 기존의 **prototype** 문법을 베이스로 만들어졌다.

## Class와 Object의 관계
- Class
  - template
  - declare once
  - no data in
- Object
  - instance of a class
  - created many times
  - data in

### Class declarations
- 클래스 선언
``` javascript
// class.js

class Person {
  // constructor
  constructor(name, age) {
    // fields
    this.name = name;
    this.age = age;
  }

  // methods
  speak() {
    console.log(`${this.name}: hello!`);
  }
}

// create object
const ellie = new Person('ellie', 20);

console.log(ellie.name);
console.log(ellie.age);
ellie.speak();
```

### Getter and Setter
#### getter, setter 주의 할 점
- `this.age` 를 하게 되면 메모리에 있는 값을 바로 가져오는 것이 아닌,  
  getter age() 함수를 호출하게 된다.  
  `= age`를 통해 field에 값을 할당할 때 메모리에 값을 바로 업데이트하는 것이 아닌,   
  setter age(value) 를 호출해서 값을 할당하게 된다.  

  이때 getter, setter에서 field의 변수 이름을 그대로 쓰게 되면 재귀호출이 일어나게 된다.  
  따라서 getter, setter 내에서는 변수 이름을 조금 다르게 바꾸어 주어야 한다.  
  -> ex) _age

- 클래스 내부에서 혹은 오브젝트에서 .연산이 가능한 이유는  
  내부적으로 getter와 setter를 호출하기 때문에 가능하다.
``` javascript
// class.js

class User {
  constructor(firstName, lastName, age) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.age = age;
  }

  get age() {
    return this._age;
  }

  set age(value) {
    // if (value < 0) {
    //   throw Error('age can not be negative');
    // }
    this._age = value < 0 ? 0 : value;
  }
}

const user1 = new User('Steve', 'Job', -1);
console.log(user1.age);
```

### Fields (public, private)
``` javascript
// class.js

// Too soon!
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Class_fields
class Experiment {
  publicField = 2; // public
  #privateField = 0; // private
}
const experiment = new Experiment();
console.log(experiment.publicField); // 2
console.log(experiment.privateField); // undefined
```

### Static properties and methods
- static은 object마다 생성되는 것이 아닌 class 자체에 연결되어 있다.  
  -> static을 사용하게 되면 object를 생성하지 않고도 클래스 내의 field나 method를 사용 할 수 있다.
``` javascript
// class.js

// Too soon!
class Article {
  static publisher = 'Dream Coding';
  constructor(articleNumber) {
    this.articleNumber = articleNumber;
  }

  static printPublisher() {
    console.log(Article.publisher);
  }
}

const article1 = new Article(1);
const article2 = new Article(2);
console.log(article1.publisher); // undefined
console.log(Article.publisher); // Dream Coding
Article.printPublisher(); // Dream Coding
```

### Inheritance & Polymorphism
#### inheritance
- extends 키워드를 통해 상속이 가능하다.
#### Polymorphism
- Overriding을 통해 부모 클래스의 method를 재구현이 가능하다.
- Overrifing후 부모의 method를 호출하고 싶으면 super 키워드를 사용하여 호출한다.
``` javascript
// class.js

// a way for one class to extend another class.
class Shape {
  constructor(width, height, color) {
    this.width = width;
    this.height = height;
    this.color = color;
  }

  draw() {
    console.log(`drawing ${this.color} color!`);
  }

  getArea() {
    return this.width * this.height;
  }
}

class Rectangle extends Shape {}
class Triangle extends Shape {
  draw() {
    super.draw();
    console.log('🔺');
  }
  getArea() {
    return (this.width * this.height) / 2;
  }

  // Object 클래스의 toString()을 Overrifing
  toString() {
    return `Triangle: color: ${this.color}`;
  }
}

const rectangle = new Rectangle(20, 20, 'blue');
rectangle.draw();
console.log(rectangle.getArea()); // 400
const triangle = new Triangle(20, 20, 'red');
triangle.draw();
console.log(triangle.getArea()); // 200
```

### Class checking: instanceOf
#### Object
- 자바스크립트에서 만든 모든 object의 class 들은 자바스크립트의 Object를 상속받는다.
``` javascript
// class.js

console.log(rectangle instanceof Rectangle); // true
console.log(triangle instanceof Rectangle); // false
console.log(triangle instanceof Triangle); // true
console.log(triangle instanceof Shape); // true
console.log(triangle instanceof Object); // true
console.log(triangle.toString()); // [object Object] --Overrifing--> `Triangle: color: ${this.color}`

let obj = { value: 5 };
function change(value) {
  value.value = 7;
}
change(obj);
```
