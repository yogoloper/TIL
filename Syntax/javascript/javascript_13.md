<!-- TOC -->

- [Async & Await, Promise APIs](#async--await-promise-apis)
  - [async](#async)
  - [await](#await)
  - [useful APIs](#useful-apis)
    - [Promise.all](#promiseall)
    - [Promise.pickOnlyOne](#promisepickonlyone)

<!-- /TOC -->

# Async & Await, Promise APIs
## async
- 함수 앞에 asnyc로 하면 함수 코드 블록이 자동으로 promise로 변환된다.
``` javascript 
// async/async.js
function fetchUser() {
  // do network reqeust in 10 secs....
  return 'ellie';
}
const user = fetchUser();
console.log(user); // 10초 뒤 동기적으로 데이터 받아와서 ellie 출력

async function fetchUser() {
  // do network reqeust in 10 secs....
  return 'ellie';
}
const user = fetchUser();
user.then(console.log);
console.log(user); // 10초 뒤 비동기적으로 데이터 받아와서 ellie 출력
```

## await
- async가 붙은 함수 안에서만 사용 가능
``` javascript 
// async/async.js

function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function getApple() {
  await delay(2000); // 딜레이가 끝날때까지 기다렸다가
  return '🍎'; // 반환
}

async function getBanana() {
  await delay(1000);
  return '🍌';
}

// 프로미스도 너무 중첩을 하게 되면 아래와 같이 콜백지옥이 펼쳐진다.  
function pickFruits() {
  return getApple().then(apple => {
    return getBanana().then(banana => `${apple} + ${banana}`);
  });
}

async function pickFruits() {
  const apple = await getApple(); // 기다려
  const banana = await getBanana(); // 기다려
  return `${apple} + ${banana}`; // 사과를 기다려서 데이터 받고 바나나를 기다려서 데이터를 받는다 -> 비효율적

  // 아래와 같이 병렬하면 병렬적으로 실행이 가능하다.
  // 사과와 바나나는 서로 관련이 없으므로 코드를 각각 미리 실행시켜서 병렬처리 가능 한 것
  const applePromise = getApple(); // 프로미스를 만들면 프로미스의 코드블럭은 바로 실행된다.
  const bananaPromise = getBanana();
  const apple = await applePromise; // 동기화
  const banana = await bananaPromise; // 동기화
  return `${apple} + ${banana}`;
}

pickFruits().then(console.log);
```

## useful APIs
- 병렬적으로 처리가 가능한 경우에는 Promise APIs를 사용하면 더 깔끔하다.
### Promise.all()
- 프로미스 배열을 담아주면 프로미스들이  
  각 함수들이 데이터들을 병렬적으로 받을떄까지 모아주는 API
- 데이터들을 다 모으면 배열로 반환한다.
### Promise.pickOnlyOne()
- 프로미스 배열중에서 제일 먼저 반환되는 프로미스를 반환한다.
- 첫 번째
``` javascript 
// async/async.js

function pickAllFruits() {
  return Promise.all([getApple(), getBanana()]).then(fruits =>
    fruits.join(' + ')
  );
}
pickAllFruits().then(console.log);

function pickOnlyOne() {
  return Promise.race([getApple(), getBanana()]);
}

pickOnlyOne().then(console.log); // 사과는 2초, 바나나는 1초 이므로 바나나 프로미스가 전달
```