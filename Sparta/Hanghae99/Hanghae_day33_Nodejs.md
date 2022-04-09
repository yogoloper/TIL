# [항해99 6기] Node.js 주특기 주간(2) - 2022.04.09

<!-- TOC -->

- [[항해99 6기] Node.js 주특기 주간2 - 2022.04.09](#%ED%95%AD%ED%95%B499-6%EA%B8%B0-nodejs-%EC%A3%BC%ED%8A%B9%EA%B8%B0-%EC%A3%BC%EA%B0%842---20220409)
- [Learned](#learned)
  - [- MongoDB](#--mongodb)
- [Will learn](#will-learn)
- [Retrospect](#retrospect)

<!-- /TOC -->

# Learned
- Template Engine
  경로: https://github.com/yogoloper/TIL/blob/master/Knowledge/Web/02.md
  - template engine을 가지고 
- MongoDB
  경로 : https://github.com/yogoloper/TIL/blob/master/Knowledge/Database/01.md
  - 

# Will learn
- DNS
- gRPC 프로토콜

# Retrospect
리액트, 뷰, 앵귤러 같은 front-end의 프레임워크가 있는데 템플릿 엔진을 사용해야 하는 걸까?  
닷넷 개발할때는 프론트엔드에서 백엔드엔드까지 한 사람이 다 작업을 했는데  
그때 당시에도 리액트 같은 프레임워크를 사용하진 않았다.  
사용자에게 보여지는 부분이 크지 않아서 프론트엔드 작업 비중이 낮았어서 그런걸로 기억된다.  

지금은 ejs라는 노드의 템플릿 엔진을 사용해보려고 하는데,  
html의 문법과 비슷하다고는 하나 이 역시 ejs를 별도로 찾아봐야 하는 수고가 있다.  
혼자서 개발하는게 아니라면 템플릿 엔진의 필요에 대해서 좀 더 조사를 해봐야 할 것 갇다.

항해의 웹개발 기초반을 들으면 파이썬으로 사이트 몇 개를 만드는데,  
이때 MongoDB를 처음 접하게 되었다. 정화히는 NoSQL을 처음 접하게 되었다.  

RDB만 사용해왔기에 테이블도 만들지 않고서 데이터를 넣으면 자동으로 콜렉션이 만들어지고  
데이터 형식도 자유롭게 들어가는게 너무 당황스러웠다.  
다행이도 노드에서는 mongoose라는 패키지가 MongoDB의 이러한 자유도를 낮춰주는데  
내 입장에서는 정말 감사하다.