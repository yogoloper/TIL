# [항해99 6기] 실전 프로젝트 (2) - 2022.04.29

<!-- TOC -->

- [[항해99 6기] 실전 프로젝트 2 - 2022.04.29](#%ED%95%AD%ED%95%B499-6%EA%B8%B0-%EC%8B%A4%EC%A0%84-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-2---20220429)
- [Learned](#learned)
  - [Web Socket](#web-socket)
    - [Polling](#polling)
    - [SSE Server Sent Event](#sse-server-sent-event)
- [Retrospect](#retrospect)

<!-- /TOC -->

# Learned
- Web Socket

## Web Socket
웹 소켓은 HTML5에 새로 추가된 스펙으로 실시간 양방향 데이터 전송을 위한 기술이다. HTTP와는 다르게 WS라는 프로토콜을 사용한다.  
따라서 브라우저에서 WS 프로토콜을 지원하면 사용 가능하다.  
Node에서는 ws나 Socket.IO 같은 패키지를 통해 웹 소켓을 사용한다.

### Polling
폴링은 웹 소켓 이전에 HTTP를 사용한 실시간 요청 기술이다.  
HTTP는 클라이언트에서 서버로 단방향 요청을 보내는 통신이므로,  이를 주기적으로 요청하여 새로운 업데이트가 있는지 확인하는 방법이었다.

### SSE (Server Sent Event)
서버센트 이벤트는 처음에 한번만 연결하면 서버가 클라이언트에 지속적으로 데이터를 보내는 기술이다.  
웹 소켓과 다른 점은 클라이언트에서 서버로는 데이터를 보낼수 없다는 점이다.  
즉, 서버에서 클라이언트로 보내는 단방향 서비스 이다.

# Retrospect
어제도 TIL을 빠뜨렸다..  
요즘들어 조금 소홀해진거 같은데 끊기있게 작성하고 습관을 들이자!