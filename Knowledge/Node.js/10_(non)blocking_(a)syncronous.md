<!-- TOC -->

- [Blocking vs Non-blocking](#blocking-vs-non-blocking)
  - [Blocking](#blocking)
  - [Non-blocking](#non-blocking)
- [Syncronous vs Asyncronous](#syncronous-vs-asyncronous)
  - [Syncronous](#syncronous)
  - [Asyncronous](#asyncronous)
- [조합](#%EC%A1%B0%ED%95%A9)
  - [sync-blocking](#sync-blocking)
  - [sync-nonblocking](#sync-nonblocking)
  - [async-blocking](#async-blocking)
  - [async-nonblocking](#async-nonblocking)

<!-- /TOC -->

# Blocking vs Non-blocking
작업의 제어권에 초점
## Blocking
작업을 진행하다가 다른 주체의 작업이 시작되면 완료까지 기다렸다가 돌아와 작업하는 것
## Non-blocking
다른 주체의 작업에 관련없이 작업 하는 것

# Syncronous vs Asyncronous
순서와 결과 처리에 초점
## Syncronous
작업을 동시에 수행하거나, 동시에 끝나거나, 끝나는 동시에 시작함을 의미
## Asyncronous
시작, 종료가 일치하지 않으며, 끝나는 동시에 시작하지 않음을 의미

# 조합
## sync-blocking
제어권을 다른 주체에게 넘겨주고 응답이 옴과 동시에 동작
## sync-nonblocking
제어권을 가지고 있되 요청한 작업을 중간중간 계속 물어봄, 응답이 옴과 동시에 그 응답을 통한 처리
## async-blocking
잘 사용하지 않음
제어권을 다른 주체에게 넘기고 처리가 끝나면 제어권을 돌려 받음 응답을 여유가 될 때 처리
## async-nonblocking
제어권을 가지고 있고 작업을 계속 하는중에 다른 주체에게 맡겨놓은 처리의 응답을 여유가 될 때 처리