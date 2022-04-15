# [항해99 6기] Node.js 주특기 주간(8) - 2022.04.15

<!-- TOC -->

- [[항해99 6기] Node.js 주특기 주간8 - 2022.04.15](#%ED%95%AD%ED%95%B499-6%EA%B8%B0-nodejs-%EC%A3%BC%ED%8A%B9%EA%B8%B0-%EC%A3%BC%EA%B0%848---20220415)
- [Learned](#learned)
  - [쿠키 & 세션](#%EC%BF%A0%ED%82%A4--%EC%84%B8%EC%85%98)
    - [쿠키](#%EC%BF%A0%ED%82%A4)
    - [세션](#%EC%84%B8%EC%85%98)
  - [express - middleware 개념](#express---middleware-%EA%B0%9C%EB%85%90)
  - [ES6 - 구조 분해 할당 문법](#es6---%EA%B5%AC%EC%A1%B0-%EB%B6%84%ED%95%B4-%ED%95%A0%EB%8B%B9-%EB%AC%B8%EB%B2%95)
  - [JWT](#jwt)
    - [JWT 정리](#jwt-%EC%A0%95%EB%A6%AC)
    - [JWT 구조](#jwt-%EA%B5%AC%EC%A1%B0)
    - [JWT 특성](#jwt-%ED%8A%B9%EC%84%B1)
    - [JWT 쿠키, 세션과의 차이](#jwt-%EC%BF%A0%ED%82%A4-%EC%84%B8%EC%85%98%EA%B3%BC%EC%9D%98-%EC%B0%A8%EC%9D%B4)
- [Retrospect](#retrospect)

<!-- /TOC -->

# Learned
- 쿠키 & 세션
- express - middleware 개념
- ES6
- rest API
- JWT

## 쿠키 & 세션
### 쿠키
브라우저가 서버로부터 응답으로 Set-Cookie 헤더를 받은 경우 해당 데이터를 저장한 뒤 모든 요청에 포함하여 보낸다.  
데이터를 여러 사이트에 공유할 수 있기 때문에 보안에 취약한 단점이 있다.  
### 세션
쿠키를 기반으로 구성된 기술로, 클라이언트가 마음대로 데이터를 확인 할 수 있던 쿠키와 달리,  
세션은 데이터를 서버에만 저장하기 때문에 보안이 좋다.  
사용자가 많을 경우 서버에 저장해야 할 데이터 또한 많아지기 때문에 서버 컴퓨터에 부하가 커진다.

## express - middleware 개념
express에서 미들웨어는 어떠한 요청에 대해서 공통적으로 처리하는 로직을 모아둔 코드 덩어리 이다.  
express.static, express.json, express.urlcenoded 같은 함수도 사실은 미들웨어를 만들어주는 함수들이다.  
- express.static(path)  
  path에 입력한 경로에 있는 파일을 그대로 서빙해 주는 기능을 수행하는 미들웨어  
- express.json  
  HHTP Request Body에 담긴 JSON 형식의 데이터를 express tjqjdptj 사용할 수 있게 해주는 미들웨어  
- express.urlcenoded  
  HTTP Request Body에 담긴 Form(URL Encoded) 형식의 데이터를 exrpess 서버에서 사용할 수 있게 해주는 미들웨어

## ES6 - 구조 분해 할당 문법
구조 분해 할당 구문은 배열이나 객체의 속성을 해체하여 그 값을 개별 변수에 담을 수 있게 하는 JavaScript 표현식이다.  
``` javascript
let a, b, rest;
[a, b] = [10, 20];
```

## JWT
### JWT 정리
- 복호화가 가능해서 중요하지 않은 정보를 저장한다.  
- JSON 형태의 데이터를 안전하게 교환하여 사용할 수 있게 해준다.
- 인터넷 표준으로 자리잡은 규격이다.
- 여러가지 암호화 알고리즘을 사용할 수 있다.
- header.payload.signature의 형식으로 3가지의 데이터를 포함한다.  
  JWT 형식으로 변환된 데이터는 항상 2개의 (".") 이 포함된 데이터여야 한다.
### JWT 구조
- header: signature에서 어떤 암호화를 사용하여 생성된 데이터인지 표현
- payload: 개발자가 원하는 데이터를 저장
- signature: 토큰이 변조되지 않은 정상적인 토큰인지 확인하는데 사용
### JWT 특성
- JWT는 암호키를 몰라도 Decode가 가능하다.  
  변조만 불가능 할 뿐, 누구나 복호화 가능

### JWT 쿠키, 세션과의 차이
데이터를 교환하고 관리하는 방식인 쿠키/세션과 달리, JWT는 단순히 데이터를 표현하는 방식이다.
- JWT로 만든 데이터를 브라우저로 보내도 쿠키처럼 자동으로 저장되지는 않지만, 변조가 거의 불가능하고 서버에 데이터를 저장하지 않기 때문에  
  서버를 stateless(무상태)로 관리 할 수 있다.
- stateless(무상태)와 stateful(상태 보존)의 차이는,  
  nodejs가 죽었다 살아나도 언제나 같은 동작을 하면 stateless,  
  조금이라도 다른 동작을 하면 sTateful이다.
- 로그인 정보를 서버에 저장하게 되면 stateful이라고 볼 수 있다.

# Retrospect
기존에 작업했던 게시판 예제를 MongoDB에서 MySQL로 전환하는 작업을 진행하고 로그인 기능을 추가하려고 하는데,  
뭐부터 손봐야 할지 몰라서 이거 조금 저거 조금 손대다가 하루가 지났다.  

내일은 DB부터 접근해서 체계적으로 진행을 해봐야 겠다.
