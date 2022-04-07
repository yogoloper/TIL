<!-- TOC -->

- [Promise](#promise)
  - [State](#state)
  - [Producer vs Consumer](#producer-vs-consumer)
    - [Producer](#producer)
    - [Consumer promise 사용하기](#consumer-promise-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0)
    - [Promise chaining](#promise-chaining)
    - [Error Handling](#error-handling)

<!-- /TOC -->

# Promise
- javascript에서 제공하는 비동기를 간편하게 처리할수 있는 Object이다.
- 처리 결과를 성공/에러로 반환한다.

## State
- Pending (대기) : 비동기 처리 로직이 아직 완료 되지 않은 상태
- Fulfilled (이행) : 비동기 처리가 완료되어 프로미스가 결과 값을 반환해준 상태
- Rejected (실패) : 비동기 처리가 실패하거나 오류가 발생한 상태

## Producer vs Consumer 
### Producer
- resolve()  
  기능을 정상적으로 수행해서 최종 데이터를 전달하는 함수
- reject()  
  기능을 수행하다가 문제가 생기면 호출하는 함수
- 프로듀서를 새로 생성하게 되면 exucutro()가 자동적으로 실행된다.
  -> resolve(), reject()
``` javascript 
// async/promise.js

// when new Promise is created, the executor runs automatically.
const promise = new Promise((resolve, reject) => {
  // doing some heavy work (network, read files)
  console.log('doing something...');
  setTimeout(() => {
    resolve('ellie');
    // reject(new Error('no network'));
  }, 2000);
});
```

### Consumer (promise 사용하기)
- then  
  promise의 resolve()에서 전달 받은 값을 사용  
- catch  
  promise의 reject()에서 전달 받은 값을 사용
- finally  
  resolve()/reject() 를 마치고 마지막으로 무조건 호출되는 함수
``` javascript 
// async/promise.js

//then, catch, finally
promise //
  .then(value => {
    console.log(value); // ellie
  })
  .catch(error => {
    console.log(error); // no network
  })
  .finally(() => {
    console.log('finally');
  });
```

### Promise chaining
``` javascript 
// async/promise.js

const fetchNumber = new Promise((resolve, reject) => {
  setTimeout(() => resolve(1), 1000);
});

fetchNumber
  .then(num => num * 2)
  .then(num => num * 3)
  .then(num => {
    return new Promise((resolve, reject) => {
      setTimeout(() => resolve(num - 1), 1000);
    });
  })
  .then(num => console.log(num)); // 5
```

### Error Handling
``` javascript 
// async/promise.js

const getHen = () =>
  new Promise((resolve, reject) => {
    setTimeout(() => resolve('🐓'), 1000);
  });
const getEgg = hen =>
  new Promise((resolve, reject) => {
    // setTimeout(() => resolve(new Error(`error! ${hen} => 🥚`)), 1000);
    setTimeout(() => reject(new Error(`error! ${hen} => 🥚`)), 1000);
  });
const cook = egg =>
  new Promise((resolve, reject) => {
    setTimeout(() => resolve(`${egg} => 🍳`), 1000);
  });

getHen() //
  .then(hen => getEgg(hen))
  .catch(error => {
    return '🎃'
  })
  .then(egg => cook(egg))
  .then(console.log(meal))
  .catch(console.log(error));
  

//  하나를 받아와서 바로 번잘 할때는 아래처럼 생략가능
//  .then(getEgg) // 생략해서 표현 가능
//  .then(cook)
//  .then(console.log)
```