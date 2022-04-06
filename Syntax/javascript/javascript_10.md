<!-- TOC -->

- [JSON](#json)
  - [JSON 개념](#json-%EA%B0%9C%EB%85%90)
    - [HTTP](#http)
    - [AJAX](#ajax)
    - [XML](#xml)
    - [XHR](#xhr)
    - [Object와 JSON](#object%EC%99%80-json)
  - [JSON 사용](#json-%EC%82%AC%EC%9A%A9)
    - [Object to JSON](#object-to-json)
    - [JSON to Object](#json-to-object)
  - [JSON 유용한 사이트](#json-%EC%9C%A0%EC%9A%A9%ED%95%9C-%EC%82%AC%EC%9D%B4%ED%8A%B8)

<!-- /TOC -->

# JSON
## JSON 개념
- 데이터를 주고 받을때 사용할는 가장 간단한 포맷
- 텍스트기반이라 가벼움
- 읽기 쉬움
- key-value 쌍으로 이루어짐
- 데이터를 주고 받을때 Serialization(직렬화) 을 위해 사용
- 특정 프로그래밍 언어나 플랫폼에 의존적이지 않음

### HTTP
- Hyptertext Transfer Protocol  
  client가 어떻게 server와 통신을 하는지에 대한 정의

### AJAX
- Asynchronous Javascript And XML  
  클라이언트에서 동적으로 서버에게 데이터를 주고 받을 수 있는 기술

### XML
- eXtensible Markup Language
- HTML은 약속한 태그만 사용이 가능한 반면  
  -> `<h1></h1>, <div></div>`
  XML은 사용자임의로 태그를 만들 수 있다.  
  ->`<JAVA></JAVA>` 같이 생성이 가능  

### XHR
- XMLHttpRequest  
  -> XML을 활용해서 데이터를 주고 받으면 불필요한 테이터들이 많아서 JSON을 주로 사용한다.

### Object와 JSON
- ECMAScript 3rd에서 공개된 오브젝트에서 영감을 받아 JSON의 형태가 만들어졌다.  
  -> { key: value }

## JSON 사용
### Object to JSON
- stringfy(obj)
  - object 내의 함수는 데이터가 아니기때문에 JSON 타입의 문자열 변환에서는 제외된다.
  - Symbole('id) 와 같은 javascirpt에서 사용되는 특별한 데이터도 문자열 변환에서는 제외된다.

``` javascript
// jaon.js
// stringfy(obj)
let json = JSON.stringify(true);
console.log(json); // true

json = JSON.stringify(['apple', 'banana']);
console.log(json); // ["apple", "banana"]

const rabbit = {
  name: 'tori',
  color: 'white',
  size: null,
  birthDate: new Date(),
  jump: function () {
    console.log(`${this.name} can jump!`);
  },
};

json = JSON.stringify(rabbit);
console.log(json); // {"name":"tori","color":"white","size":null,"birthDate":"2022-04-06T12:32:29.573Z"}

json = JSON.stringify(rabbit, ['name', 'color', 'size']);
console.log(json); // {"name":"tori","color":"white","size":null}

json = JSON.stringify(rabbit, (key, value) => {
  console.log(`key: ${key}, value: ${value}`);
  return key === 'name' ? 'ellie' : value;
});
console.log(json);
```

### JSON to Object
- parse(json)
  - JSON 타입의 문자열을 다시 객체로 만들면,  
    stringfy시 제외된 메소드는 제외된 상태로 객체로 만들어진다.  
    즉, parse()를 하게 되면 key-value 쌍의 테이터들만 존재한다.  
  - reviver callback 함수를 이용해서 타입 복구  
    -> 본래 rabbit 객체의 birthDate는 Date의 인스턴스이다.  
    parse만 하게되면 obj의 birthDate는 문자열 형태로 만들어진다.  
    이를 reviver 콜백함수를 이용하게 되면 obj2의 birthDate는 Date의 인스턴스로 만들어진다.
``` javascript
// jaon.js

// parse(json)
console.clear();
json = JSON.stringify(rabbit);
console.log(json);

const obj = JSON.parse(json);
const obj2 = JSON.parse(json, (key, value) => {
  console.log(`key: ${key}, value: ${value}`);
  return key === 'birthDate' ? new Date(value) : value;
});
console.log(obj);
rabbit.jump();
// obj.jump(); // TypeError

console.log(rabbit.birthDate.getDate()); // 날짜 출력
console.log(obj.birthDate.getDate()); // TypeError
console.log(obj2.birthDate.getDate()); // 날짜 출력
```

## JSON 유용한 사이트
- JSON Diff checker: http://www.jsondiff.com/
- JSON Beautifier/editor: https://jsonbeautifier.org/
- JSON Parser: https://jsonparser.org/
- JSON Validator: https://tools.learningcontainer.com/json-validator/