<!-- TOC -->

- [Node.js는 어떻게 동작 하는가?](#nodejs%EB%8A%94-%EC%96%B4%EB%96%BB%EA%B2%8C-%EB%8F%99%EC%9E%91-%ED%95%98%EB%8A%94%EA%B0%80)
  - [Single Thread](#single-thread)
  - [Non-Blocking I/O](#non-blocking-io)
  - [Event-Driven](#event-driven)
  - [Event Loop](#event-loop)

<!-- /TOC -->

# Node.js는 어떻게 동작 하는가?

## Single Thread
node.js는 싱글스레드이지만 엄밀히 말하자면 아니다.  
node.js를 실행하면 프로세스 하나가 생성되고, 여러 개의 스레드를 생성하게 된다.  
그 중에서 제어할 수 있는 스레드가 하나이다.  

## Non-Blocking I/O
위에서 말했듯이 node.js의 스레드 하나만을 제어 할 수 있다고 했는데,
하나의 스레드로 여러가지 요청을 동시에 받을 수 있는 것은 Non-blocking 모델로 구성된 덕분이다.  

Non-blocking이란 이전 작업이 완료되는 것을 기다리지 않고 다음 작업을 수행함을 뜻하며,
javascript 상에서 작업하는 것이 아닌 I/O 작업, File, DB 등의 Blocking 작업들을 백그라운드에서 수행하고 이를 비동기 콜백 함수로 이벤트 루프에 전달하는 것을 말한다.

## Event-Driven
이벤트 기반이란 이벤트가 발생할 때 미리 지정해 둔 작업을 수행하는 방식을 의미하며, node.js가 이벤트 리스터에 등록해둔 콜백함수를 실행하는 방식으로 동작한다.
이러한 이벤트 기반의 모델에서 이벤트에 따라 호출되는 콜백 함수를 관리하는 것을 Event Loop라고 한다.

## Event Loop
node.js는 내장 라이브러리인 V8과 libuv로 구성되어 있는데, 이벤트 기반, non-blocking I/O 모델은 모두 libuv에서 구현되어 있다. node.js에서 작성되는 거의 모든 코드들은 콜백 함수로 이루어져 있으며, 콜백 함수들은 libuv 내에 위치한 이벤트 루프에서 관리 및 처리된다. 이벤트 루프는 여러 개의 페이즈 들을 갖고 있으며 해당 페이즈들은 각자만에 큐를 가지고 있다. 이벤트 루프는 라운드 로빈 방식으로 노드 프로세스가 종료될 때까지 여러 페이지들을 계속 순회하고, 페이즈들은 각각의 큐들을 관리하고 각각의 큐는 FIFO 순서로 콜백 함수들을 처리하게 된다.