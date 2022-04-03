<!-- TOC -->

- [자바스크립트의 역사와 현재 그리고 미래](#%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8%EC%9D%98-%EC%97%AD%EC%82%AC%EC%99%80-%ED%98%84%EC%9E%AC-%EA%B7%B8%EB%A6%AC%EA%B3%A0-%EB%AF%B8%EB%9E%98)
  - [Javascript 탄생배경](#javascript-%ED%83%84%EC%83%9D%EB%B0%B0%EA%B2%BD)
    - [Javascript 탄생](#javascript-%ED%83%84%EC%83%9D)
    - [Javascript, JScript, ECAMScript](#javascript-jscript-ecamscript)
    - [AJAX, jQuery](#ajax-jquery)
    - [JavaScript Engines](#javascript-engines)
    - [BABEL](#babel)
  - [Javascript 동향](#javascript-%EB%8F%99%ED%96%A5)
    - [SPA](#spa)
  - [Jacascript의 미래](#jacascript%EC%9D%98-%EB%AF%B8%EB%9E%98)
    - [Back-end](#back-end)
    - [Mobile](#mobile)
    - [Desktop](#desktop)

<!-- /TOC -->

# 자바스크립트의 역사와 현재 그리고 미래

## Javascript 탄생배경
### Javascript 탄생
- 1993년, 일리노이 대학교 어배너-섐페인의 NCSA는 최초의 대중적인 그래픽 웹 브라우저인 **NCSA 모자이크(Mosaic Web Browser)** 를 출시하였다.
- 1994년, **Netscape의 Marc Andreessen가 Netscape Navigator를 만들게 되었고** , 시장의 80%를 점유하였다.
- 1994년 9월, Brendan Eich 영입하여 sheme scripting 을 변형하여 **모카(Mocha)** 를 만들게 되었고, 추후 **라이브 스크립트(LiveScript)** 로 변경하였다.  
  넷스케이프 네비게이터 안에는 라이브 스크립트 엔젠인 **인터프리터** 를 탑재하여 출시하였다.  
  이후, 개발자들은 라이브 스크립트를 통해 **DOM** 요소의 조작이 가능해졌다.  
  Java의 인기가 치솟아 LiveScript의 이름을 JavaScript로 이름을 변경하였다.  
  ### Javascript, JScript, ECAMScript
- 1995년, Microtsoft는 Javascript의 리버스 엔지니어링을 통해 자신들만의 언어인 JScript를 출시하였다.  
  이와 더불의 InternetExplorer를 함께 출시하였다.
  - **리버스 엔지니어링** - 바이너리 코드를 분석하여 소스를 복원  
- 1996년, Javascript와 JScript의 대립으로 개발자들의 고충이 되었다.
- 1996년 11월, 넷스케이프는 표준화 기구인 ECMA International에 표준화 요청을 하게 되었다.
- 1997년 7월, **ECAMScript 1** 출시하게 되었다.  
  이후 매년 ECAMScript는 업데이트 되었고, 3에서는 Error handling, 4에서는 optional type annotation, class 등이 추가 되었다.
- 2000년, 95%의 시장점유율을 확보한 MS사는 ECMAScript 표준화 참여에서 빠지게 되었고, 표준화 진행은 더디게 되었다.
- 2004년, Mozila는 ActionScript3 언어와 Tamarin 엔진을 탑재한 Firefox를 출시하였고,  
  표준화를 두고 넷스케이프, 마이크로소프트, 모질라의 신경전이 치열했다.
### AJAX, jQuery
- 2004년, Jess James Garrett에 의해서 **AJAX(Asynchronous JavaScript and XML** 가 도입되었다.
- 이후 개발자들 사이에서 커뮤니티가 형성되었고, jQuery, dojo, mootools와 같은 라이브러리가 생겨나게 되며,  
  이러한 라이브러리들은 개발자들이 APIs를 통해서 브라우저 종류에 상관없이 개발에 전념할 수 있게 되었고,  
  그중 jQeury가 가장 많은 사랑을 받았다.
### Chrome 등장
- 2008년, google이 엄청난 Javascript 실행 속도를 가진 **JIT(just-in-time compliation)** 엔진을 탑재한 **크롬(Chrome)** 브라우저를 출시하였다.
- 2008년 7월, 모든 브라우저들이 모여 표준화를 다시 진행하게 되었다.
- 2009년, **ECMAScript 5출시**
- 2015년, **ECMAScript 6출시**
- 이후 매년 새로운 버전이 출시되지만, 5, 6을 기반으로 JavaScript는 잘 정착 되었다.

### JavaScript Engines
- Chrome - V8
  - node.js, Electron 에서도 사용
- Firefox - SpiderMonkey
- Safari - JSCOre
- ME Edge - Chakra
  - 2020년 2월, V8도입
- Opera - Carakan
- Adobe Flash - Tamarin

### BABEL
- 개발자들은 최신 버전의 ECMAScript를 사용하고, clienct의 버전에 맞게 변환해 주는 **JavaScript Transcompiler**

## Javascript 동향
### SPA
- Single Page Application
- SPA를 위해 React, Angular, Vue 등이 출시

## Jacascript의 미래
### Back-end
- node.js를 활용
### Mobile
- Native, Cold
### Desktop
- Electron 활용