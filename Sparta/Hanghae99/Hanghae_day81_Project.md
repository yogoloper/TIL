# [항해99 6기] 실전 프로젝트 (27) - 2022.05.27

<!-- TOC -->

- [[항해99 6기] 실전 프로젝트 27 - 2022.05.27](#%ED%95%AD%ED%95%B499-6%EA%B8%B0-%EC%8B%A4%EC%A0%84-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-27---20220527)
- [Retrospect](#retrospect)

<!-- /TOC -->

# Retrospect
코드를 작성하면서 파일 구조나 예외처리, 에러코드 관리 등에 대한게 기억이 어렴풋이만 나서 어려움을 겪고 있는데 공부가 부족한 것 같다. 패턴도 같이 알려주는 강의를 하나 보는 중인데 nodejs의 싱글톤 패턴에 대해서 다뤘다. 예전에 스프링 공부할 때 db connection은 자원을 엄청 소비하는 동작이며, 한 번 연결해서 공동으로 사용하기 위해 싱글톤 패턴을 적용했다.  
강의에서는 app을 한 번만 생성하여 공유하기 위해서 Server 클래스에 멤버로 app을 가지고 Server를 한 번만 생성하여서 싱글톤 패턴을 적용하였다.  

싱글톤 패턴을 사용하는데 장점은 크게 두 가지가 있다.  
1. 메모리 효율성
2. 프로그램에서 해당 인스턴스가 절대적으로 한 개만 존재한다는 것을 보장