# [항해99 6기] Node.js 주특기 주간(19) - 2022.04.26

<!-- TOC -->

- [[항해99 6기] Node.js 주특기 주간19 - 2022.04.26](#%ED%95%AD%ED%95%B499-6%EA%B8%B0-nodejs-%EC%A3%BC%ED%8A%B9%EA%B8%B0-%EC%A3%BC%EA%B0%8419---20220426)
- [Learned](#learned)
  - [CQRS Command Query Reponsibility Segregation](#cqrs-command-query-reponsibility-segregation)
    - [명령 Command](#%EB%AA%85%EB%A0%B9-command)
    - [쿼리 Query](#%EC%BF%BC%EB%A6%AC-query)
    - [책임 Responsibility](#%EC%B1%85%EC%9E%84-responsibility)
    - [분리 Segregation](#%EB%B6%84%EB%A6%AC-segregation)
  - [왜 CQRS](#%EC%99%9C-cqrs)
  - [CQRS 구현방법](#cqrs-%EA%B5%AC%ED%98%84%EB%B0%A9%EB%B2%95)
    - [동일 프로세스, 동일 DB](#%EB%8F%99%EC%9D%BC-%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4-%EB%8F%99%EC%9D%BC-db)
    - [-2. 동일 프로세스, 동일 DB, 다른 테이블](#-2-%EB%8F%99%EC%9D%BC-%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4-%EB%8F%99%EC%9D%BC-db-%EB%8B%A4%EB%A5%B8-%ED%85%8C%EC%9D%B4%EB%B8%94)
    - [다른 프로세스, 동일 DB](#%EB%8B%A4%EB%A5%B8-%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4-%EB%8F%99%EC%9D%BC-db)
    - [동일 프로세스, 다른 DB](#%EB%8F%99%EC%9D%BC-%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4-%EB%8B%A4%EB%A5%B8-db)
    - [다른 프로세스, 다른 DB](#%EB%8B%A4%EB%A5%B8-%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4-%EB%8B%A4%EB%A5%B8-db)
- [Retrospect](#retrospect)

<!-- /TOC -->

# Learned

- CQRS

## CQRS (Command Query Reponsibility Segregation)

애플리케이션을 구성하는 아키텍쳐의 하나의 패턴으로,  
번역하면 말 그래도 **명령 조회 책임 분리**이다.

애플리케이션을 구현함에 있어 명령과 조회를 구분해서 분리하라는건데 명령은 뭐고 쿼리는 뭘까?  
명령은 데이터를 변경하는 것을 말하고,  
쿼리는 데이터를 조회하는 것을 말한다.

그러면 책임 분리는?  
책임은 구성 요소의 역할이며,  
분리는 그 역할에 따라 구성 요소를 나눈 것을 말한다.

즉, CQRS는 명령 역할과 쿼리 역할을 수행하는 구성요소를 나누는 것이다.

### 명령 (Command)

시스템의 데이터를 변경하는 것

- Create, Update, Delete

### 쿼리 (Query)

시스템의 데이터를 조회하는 것

- Read

### 책임 (Responsibility)

구성 요소의 역할

### 분리 (Segregation)

역할에 따른 구성 요소 분리

## 왜 CQRS

간단한 예로, 기존의 아키텍쳐에서는 CRUD를 모두 동일한 모델을 사용하는데,  
기능이 추가될 수록 이전에 만들어둔 클래스에 기능 추가를 계속 하게된다.
잡탕이 된 클래스는 역할이나 의미가 모호해지고 유지보수가 힘들어진다.

정리하자면,

1. 명령과 쿼리는 다루는 데이터가 다르다.
2. 명령과 쿼리는 코드의 변경 빈도, 사용자가 다르다.
3. 기능마다 성능 요구가 다르다.

## CQRS 구현방법

CQRS는 프로세스의 분리 여부, DB의 분리 여부로 네 가지 정도로 구분을 할 수 있다.

<table>
  <tbody>
    <tr>
      <td>동일 프로세스</br>동일 DB</td>
      <td>다른 프로세스</br>동일 DB</td>
    </tr>
    <tr>
      <td>동일 프로세스</br>다른 DB</td>
      <td>다른 프로세스</br>다른 DB</td>
    </tr>
  </tbody>
</table>

### 1. 동일 프로세스, 동일 DB
- 가장 단순, 명령/쿼리 동일 데이터 보장
### 1-2. 동일 프로세스, 동일 DB, 다른 테이블
- 쿼리 전용 테이블 사용
- 명령이 쿼리 전용 데이터 변경 유발
### 2. 다른 프로세스, 동일 DB
- 잘 사용되지 않는 구조
### 3. 동일 프로세스, 다른 DB
- 명령이 데이터를 변경하면, 쿼리쪽 디비에 데이터를 전달
### 4. 다른 프로세스, 다른 DB
- 명령이 데이터를 변경하면, 쿼리쪽 디비에 데이터를 전달
- 마이크로 서비스 추세에 맞는 형태

# Retrospect
nest를 검색하다보면 CQRS가 자주 눈에 띄길래 찾아보았다.  
아직 기본적인 CRUD만 학습하고 있는데,  
CQRS를 보니 아직 와닿지 않는것 같다.  
nest에서는 createDTO, updateDTO를 구분해서 사용하는데  
create나 update 모두 명령에 해당하지만 CQRS가 조금 적용이 된 부분이 아닌가 싶다.