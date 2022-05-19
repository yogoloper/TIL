# [항해99 6기] 실전 프로젝트 (20) - 2022.05.19

<!-- TOC -->

- [[항해99 6기] 실전 프로젝트 20 - 2022.05.19](#%ED%95%AD%ED%95%B499-6%EA%B8%B0-%EC%8B%A4%EC%A0%84-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-20---20220519)
- [Retrospect](#retrospect)

<!-- /TOC -->

# Retrospect
예전 회사에 있을때는 폐쇄망에서 깃랩만 사용해서 깃헙을 통한 협업에 대해서 낯설다. 아니 꼭 깃헙이 아니더라도 브렌치전략이나 커밋 메시지 규칙과 같은 것들에 대해서 깊게 고민하지 않고 사용했고 팀원들도 모두 그렇게 사용했다. 회사를 나와보니 깃헙을 제외하더라도 익혀야 할 기술의 양은 너무나도 방대하고 변형 또한 자유로워 내 입맛에 맞는 것을 찾아 적용하는데 어려움이 있다. 그래서 오늘은 깃헙으로 협업할때 Pull Request를 하는 순서에 대해서 가져와 봤다.

1. Fork
2. clone, remote설정
3. branch 생성
4. 수정 작업 후 add, commit, push
5. Pull Request 생성
6. 코드리뷰, Merge Pull Reqest
7. Merge 이후 branch 삭제 및 동기화

그리고 깃 강의를 듣는데 강사가 아래 내용을 인용하였는데 나에게 필요한 내용같아서 함께 기록한다.

> 지금 상황과 상관없이 여러분은 언제나 더 나아질 수 있다.   
> 더 나아지는 일은 언제나 스스로부터 시작할 수 있다.   
> 더 나아지는 일은 언제나 오늘부터 시작할 수 있다.   
> 
> No matter the circumstances you can always improve.  
> You can always start improving with yourself.  
> You can always start improving today.  

- 익스트림 프로그래밍(2판).켄트 벡, 신시아 안드레스 지음. 김창준,정지호 옮김.인사이트