# [항해99 6기] 실전 프로젝트 (22) - 2022.05.21

<!-- TOC -->

- [[항해99 6기] 실전 프로젝트 22 - 2022.05.21](#%ED%95%AD%ED%95%B499-6%EA%B8%B0-%EC%8B%A4%EC%A0%84-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-22---20220521)
- [Retrospect](#retrospect)

<!-- /TOC -->

# Retrospect
MVP 중간 발표에 대한 피드백을 들었는데, 예상한 것들 가운데에서 피드백이 나온것도 있지만 예상 범위를 벗어난 피드백이 있었는데 그 중 하나가 엔티티 그대로 반환하지 말 것 이었다. ORM을 써서 받은거 그대로 넣고 출력하도록 작성했는데 한 번 필터링을 해서 내보내 주라는 말에 동의를 하면서도 갸우뚱 하기도 했다. 그렇게 한다면 조회 할 때의 ORM은 독이 되는 느낌이랄까.. 무언가 반환타입을 또 편하게 해주는 게 있을것 같으니 찾아보자.