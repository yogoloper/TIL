<!-- TOC -->

- [Data types, let vs var, Hoisting](#data-types-let-vs-var-hoisting)
  - [Data types](#data-types)
    - [Variable type](#variable-type)
    - [Variable 선언 방법](#variable-%EC%84%A0%EC%96%B8-%EB%B0%A9%EB%B2%95)
      - [let ES6에서부터 추가](#let-es6%EC%97%90%EC%84%9C%EB%B6%80%ED%84%B0-%EC%B6%94%EA%B0%80)
      - [Block scope](#block-scope)
      - [var 사용하면 안되는 이유](#var-%EC%82%AC%EC%9A%A9%ED%95%98%EB%A9%B4-%EC%95%88%EB%90%98%EB%8A%94-%EC%9D%B4%EC%9C%A0)
      - [constants](#constants)
    - [Primitive type](#primitive-type)
      - [number](#number)
      - [string](#string)
      - [boolean](#boolean)
      - [null](#null)
      - [undefined](#undefined)
      - [symbol](#symbol)
    - [Object type](#object-type)
      - [object](#object)
    - [Dynamic typing: dynamicaaly typed language](#dynamic-typing-dynamicaaly-typed-language)

<!-- /TOC -->

# Data types, let vs var, Hoisting

## Data types
### Variable type
- primitive, single item: number, string, boolean, null, undefined, symbol
- object, box container
- function, first-class function
### Variable 선언 방법
#### let (ES6에서부터 추가)
- Mutable Type  
  변수 선언 후 변수의 값을 계속 변경할 수 있다.
``` javascript
// variable.js

let name = 'apple';
console.log(name);
name = 'banana';
console.log(name);
```
#### Block scope
- Block 내부에 작성한 변수에는 외부에서 접근 불가능 하며,  
  Block 밖의 전위에서 사용하는 것을 **Global Scope**라고 한다.
``` javascript 
// variable.js

let globalName = 'global apple';
{
  let name = 'apple';
  console.log(name);
  name = 'banana';
  console.log(name);
  console.log(globalName);
}
console.log(name);
console.log(globalName);
```

#### var (사용하면 안되는 이유)
- Hoisting  
  -> 어디에 선언했는지 상관없이 제일 위로 선언을 올려준다.
- no Block scope  
  -> block을 무시하고 block 내의 변수를 외부에서 호출이 가능하다.

#### constants
- Immtable Type  
  선언과 동시에 값을 한 번 할당하면 변수의 값을 변경할 수 없다.
- 장점  
  - 보안성 향상
  - 쓰레드 안정성
  - 사용자의 실수 방지
``` javascript
// variable.js

const daysInWeek = 7;
const maxNumber = 5;
```

### Primitive type
#### number
- number
``` javascript
// variable.js

const count = 17; // integer
const size = 17.1; // decimal number
console.log(`value: ${count}, type: ${typeof count}`);
console.log(`value: ${size}, type: ${typeof size}`);
```

- infinity, -infinity, NaN
``` javascript
// variable.js

const infinity = 1 / 0;
const negativeInfinity = -1 / 0;
const nAn = 'not a number' / 2;
console.log(infinity);
console.log(negativeInfinity);
console.log(nAn);
```

- bigInt (새롭게 추가 되었지만 아직 사용하진 않음)  
  숫자 마지막에 n을 추가
``` javascript
// variable.js
const bigInt = 1234567890123456789012345678901234567890n; // over (-2**53) ~ 2*53)
console.log(`value: ${bigInt}, type: ${typeof bigInt}`);
```

#### string
- string
``` javascript
// variable.js

const char = 'c';
const brendan = 'brendan';
const greeting = 'hello ' + brendan;
console.log(`value: ${greeting}, type: ${typeof greeting}`);
// backtick(`) -  템플릿 리터럴(Template literals)에 사용
const helloBob = `hi ${brendan}!`; //template literals (string)
console.log(`value: ${helloBob}, type: ${typeof helloBob}`);
console.log('value: ' + helloBob + ' type: ' + typeof helloBob);
```

#### boolean
- boolean  
  - false: 0, null, undefined, NaN, ''
  - true: false를 제외한 모든 값
``` javascript
// variable.js

const canRead = true;
const test = 3 < 1; // false
console.log(`value: ${canRead}, type: ${typeof canRead}`);
console.log(`value: ${test}, type: ${typeof test}`);
```

#### null
- 명확하게 지정되지 않은 값을 의미  
  -> null로 값이 할당된 경우
``` javascript
// variable.js

let nothing = null;
console.log(`value: ${nothing}, type: ${typeof nothing}`);
```

#### undefined
- 선언은 되었지만 아무것도 값이 지정되지 않은 상태  
  -> 값이 비어있는 건지도 모르는 상태
``` javascript
// variable.js

let x;
console.log(`value: ${x}, type: ${typeof x}`);
```

#### symbol
- 자료구조에서 **고유한 식별자**가 필요하거나,  
  동시에 다발적으로 일어나는 코드에서 우선순위를 주고 싶을때 사용
``` javascript
// variable.js

// 동일한 id string으로 작성하였어도 고유한 식별자 생성
const symbol1 = Symbol('id');
const symbol2 = Symbol('id');
console.log(symbol1 === symbol2);
// id string의 동일한 심볼 할당
const gSymbol1 = Symbol.for('id');
const gSymbol2 = Symbol.for('id');
console.log(gSymbol1 === gSymbol2); // true
console.log(`value: ${symbol1.description}, type: ${typeof symbol1}`);
```

### Object type
#### object
``` javascript
// variable.js

const yogoloper = { name: 'yogoloper', age: 20 };
yogoloper.age = 21;
```

### Dynamic typing: dynamicaaly typed language
- 자바스크립트는 선언할때 타입을 선언하지 않고  
  동작할때 값에 따라서 변수의 타입이 변경될 수 있다는 의미
``` javascript
// variable.js

// string 타입
let text = 'hello';
console.log(text.charAt(0)); //h
console.log(`value: ${text}, type: ${typeof text}`);
// number로 변경
text = 1;
console.log(`value: ${text}, type: ${typeof text}`);
// string으로 변환
text = '7' + 5;
console.log(`value: ${text}, type: ${typeof text}`);
// number로 변경
text = '8' / '2';
console.log(`value: ${text}, type: ${typeof text}`);
// number로 변경된 줄 모르고 string 함수를 사용하면 런타임 타입에러 발생
console.log(text.charAt(0));
```