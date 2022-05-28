# [항해99 6기] 실전 프로젝트 (28) - 2022.05.28

<!-- TOC -->

- [[항해99 6기] 실전 프로젝트 28 - 2022.05.28](#%ED%95%AD%ED%95%B499-6%EA%B8%B0-%EC%8B%A4%EC%A0%84-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-28---20220528)
- [Retrospect](#retrospect)

<!-- /TOC -->

# Retrospect
nestjs에는 여러 기능이 있는데 미들웨어 까지는 괜찮은데 예외 필터, 파이프, 인터셉터가 나오면서부터 어떤걸 어디에 적용 시켜야 하는지 헷갈리게 된다.  
아래는 리퀘스트의 리이프 사이클이다.  
1. Incoming request
1. Globally bound middleware
1. Module bound middleware
1. Global guards
1. Controller guards
1. Route guards
1. Global interceptors (pre-controller)
1. Controller interceptors (pre-controller)
1. Route interceptors (pre-controller)
1. Global pipes
1. Controller pipes
1. Route pipes
1. Route parameter pipes
1. Controller (method handler)
1. Service (if exists)
1. Route interceptor (post-request)
1. Controller interceptor (post-request)
1. Global interceptor (post-request)
1. Exception filters (route, then controller, then global)
1. Server response

통틀어서 보자면 아래와 같다.
request - middleware - guards - pre interceptor - pipes - constroller - service - post interceptor - exception filters - response   

순서도 알겠는데.. 어떤걸 보면 로그를 인터셉터로 구현하고 어떤걸 보면 로그를 미들웨어로 구현하고 그러는데 이런데서 혼란이 온다.  
자유도에 맡기는건지.. 아직 저런 함수들을 보면 어떻게 적용하면 효율좋은 코드를 짤수 있는지 고민이 된다.