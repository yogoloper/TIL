# [항해99 6기] 실전 프로젝트 (14) - 2022.05.13

<!-- TOC -->

- [[항해99 6기] 실전 프로젝트 14 - 2022.05.13](#%ED%95%AD%ED%95%B499-6%EA%B8%B0-%EC%8B%A4%EC%A0%84-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-14---20220513)
- [Retrospect](#retrospect)

<!-- /TOC -->

# Retrospect
어제도 작성을 안하고 잤는데..  
주먹 구구식으로 시도하다보니 내가 하루 동안 어떤게 문제였고, 어떤것을 시도했고, 결국 어떻게 해결했다 를 정리하기가 쉽지 않은것 같다.

어제는 auth 서버에서 발급한 토큰을 사용해서 room 서버에서 유효성 검사와 userId를 꺼내서 사용할 수 있도록 작성하였는데, authGuard와 커스텀 데코레이터를 이용했다. 작성이 완료되지 않아서 오늘 마저 작업하고 내용을 정리해 보려고 한다.