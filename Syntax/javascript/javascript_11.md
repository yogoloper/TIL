<!-- TOC -->

- [Callback](#callback)
  - [Syncronous vs Ascyncronous](#syncronous-vs-ascyncronous)
  - [asyncronous 에시](#asyncronous-%EC%97%90%EC%8B%9C)
    - [Synchronous callback](#synchronous-callback)
    - [Asynchronous callback](#asynchronous-callback)
  - [Callback Hell example](#callback-hell-example)

<!-- /TOC -->

# Callback
## Syncronous vs Ascyncronous
- 자바스크립트는 동기 언어로써,  
  호이스팅이 이루어진 이후부터는 코드가 작성된 순서대로 동작한다.
- Syncronous  
  서버에 요청을 보냈을때 응답이 돌아와야 다음 동작을 수행한다.  
  즉, A 작업이 모두 진행될때까지 B작업은 대기한다.
- Asyncronous  
  서버에 요청을 보내고 응답 상태와 상관없이 다음 동작을 수행한다.  
  즉, A 작업과 B 작업이 병렬로 진행 될 수 있다. 

## asyncronous 에시
``` javascript
// async/callback.js

console.log('1');
setTimeout(() => console.log('2'), 1000);
console.log('3');

// 1
// 3
// 2
```

### Synchronous callback
- 콜백함수를 동기적으로 사용
``` javascript
// async/callback.js

console.log('1');
setTimeout(() => console.log('2'), 1000);
console.log('3');

function printImmediately(print) { // 호이스팅돼서 상단으로 올라감
  print();
}
printImmediately(() => console.log('hello')); // 동기

// 1
// 3
// hello
// 2
```

### Asynchronous callback
- 콜백함수를 비동기적으로 사용
``` javascript
// async/callback.js

console.log('1');
setTimeout(() => console.log('2'), 1000); // 비동기
console.log('3');

function printImmediately(print) { // 호이스팅돼서 상단으로 올라감
  print();
}

function printWithDelay(print, timeout) { // 호이스팅돼서 상단으로 올라감
  setTimeout(print, timeout);
}
printImmediately(() => console.log('hello')); // 동기
printWithDelay(() => console.log('async callback'), 2000); // 비동기

// 1
// 3
// hello
// 2
// async callbacl
```

## Callback Hell example
- UserStorage 클래스에는 loginUser, getRoles라는 메소드가 존재  
  네트워크 통신을 setTimeoutd으로 표현
``` javascript
// async/callback.js

class UserStorage {
  loginUser(id, password, onSuccess, onError) {
    setTimeout(() => {
      if (
        (id === 'ellie' && password === 'dream') ||
        (id === 'coder' && password === 'academy')
      ) {
        onSuccess(id);
      } else {
        onError(new Error('not found'));
      }
    }, 2000);
  }

  getRoles(user, onSuccess, onError) {
    setTimeout(() => {
      if (user === 'ellie') {
        onSuccess({ name: 'ellie', role: 'admin' });
      } else {
        onError(new Error('no access'));
      }
    }, 1000);
  }
}

// 사용자 인스턴스 생성
const userStorage = new UserStorage();
// 사용자 정보 입력
const id = prompt('enter your id');
const password = prompt('enter your passrod');

// 로그인(아이디, 비밀번호)
userStorage.loginUser(
  id,
  password,
  // 로그인 성공시 - 사용자 정보를 받아와 처리 하는 콜백
  user => {
    // 사용자 역할 조회(유저정보)
    userStorage.getRoles(
      user,
      // 사용자 역할 조회 성공시 - 사용자 역할을 받아와 출력하는 콜백
      userWithRole => {
        alert(
          `Hello ${userWithRole.name}, you have a ${userWithRole.role} role`
        );
      },
      // 사용자 역할 조회 실패시 에러 콜백
      error => {
        console.log(error);
      }
    );
  },
  // 로그인 실패시 에러 콜백
  error => {
    console.log(error);
  }
);
``