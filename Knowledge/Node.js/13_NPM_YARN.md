<!-- TOC -->

- [NPM과 Yarn의 차이?](#npm%EA%B3%BC-yarn%EC%9D%98-%EC%B0%A8%EC%9D%B4)

<!-- /TOC -->

# NPM과 Yarn의 차이?
우선은 두 가지 모두 node의 패키지 매니저이다.  
전 세계 개발자들이 다양한 패키지를 만들어 온라인 DB에 올리면, npm이나 yarn을 통해서 다른 개발자들이 설치를 할 수 있다.

npm의 속도와 보안성을 개선하기 위해서 Facebook에서 yarn을 개발했다.  

패키지 설치시 npm은 순차적으로 설치하는 반면, yarn은 병렬로 설치한다.  
또한 npm은 패키지가 설치될 때 자동으로 코드와 의존성을 실행할 수 있도록 허용하였는데 이 편리성이 안정성을 위협할 수 있다.  
yarn은 yarn.lock이나 package.json의 기재된 파일만 설치한다.