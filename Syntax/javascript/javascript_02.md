

# 콘솔에 출력, script async 와 defer의 차이점

## Hello world 출력
``` javascript
// main.js

console.log('Hello world!')
```
``` javascript
// index.html

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <script src="async/async.js" defer></script>
  </head>
  <body></body>
</html>
```

### Console API
- Web API중에 하나로 자바스크립트에서 제공하는 함수가 아닌  
  브라우저에서 제공하는 함수 중에 하나이다.
- node 에서도 동작하는 이유는 통상적으로 사용되는 API이기 때문에 동일한 인터페이스로 만들어졌다.

## 환경 설정
### 자바스크립트 참고 사이트
- 공식 사이트    
  https://ecma-international.org
- 
  **https://developer.mozilla.org**

### Live Server 설치  
- VSCode Extentions에서 Live Server 설치  
  -> HTML 코드가 변경되면 브라우저에서 바로바로 보여준다.  
  -> [CMD + L] + [CMD + O]

## async와 defer의 차이점
- HTML에 자바스크립트 파일을 포함할 때의 동작 비교

### head 안에 포함
- 브라우저가 HTML을 한줄한줄 parsing 하다가 script 태그를 만나면 해당 main.js를 다운받게 된다.
- HTML parsing을 멈춘 상태에서 main.js 다운, main.js 실행 그리고 다시 HTML parsing을 진행
- 인터넷이 느리고, main.js의 용량이 크다면 사용자에게 문서를 노출하는데 많은 시간이 소요되게 된다.
``` javascript
<!DOCTYPE html>
<html lang="en">
  <head>
    <script src="main.js" defer></script>
  </head>
  <body>
  </body>
</html>
```

### body 안 끝부분에 포함
- 브라우저가 HTML parsing을 완료 후에 main.js를 다운, 실행을 하게 된다.
- 사용자가 문서는 빨리 볼수 있겠지만, 자바스크립트 의존도가 높은 페이지라면 문서를 정상적으로 노출하는데 오랜 시간이 걸리게 된다.
``` javascript
<!DOCTYPE html>
<html lang="en">
  <head>
  </head>
  <body>
    ...
    <script src="main.js" defer></script>
  </body>
</html>
```

### async 사용
- async(=true)사용하게 되면 main.js를 병렬로 다운로드 받게 되고,  
  다운로드가 된 후 main.js를 실행할때만 HTML parsing을 멈추게 된다.
- parsing이 끝나지 않은 상태에서 main.js가 실행되면 DOM이 정의 되지 않았을 가능성이 크다.
``` javascript
<!DOCTYPE html>
<html lang="en">
  <head>
    <script async src="main.js" defer></script>
  </head>
  <body>
  </body>
</html>
```

### defer 사용
- defer를 만나게 되면, HTML parsing을 하면서 모든 main.js를 다운받고,  
  parsing완료되면 바로이어서 main.js를 실행한다.
``` javascript
<!DOCTYPE html>
<html lang="en">
  <head>
    <script defer src="main.js" defer></script>
  </head>
  <body>
  </body>
</html>
```

## use strict
- 자바스크립트는 매우 **유연**하기 떄문에 **위험**도 있다.  
  -> 선언되지 않은 변수에 값을 할당하는 행위 등
- 자바스크립트를 상식적으로 사용 할수 있도록 제한하는 기능이며,  
  자바스크립트 엔진이 효율적으로 자바스크립트를 분석할 수 있도록 도와준다.