# [항해99 6기] 실전 프로젝트 (26) - 2022.05.26

<!-- TOC -->

- [[항해99 6기] 실전 프로젝트 26 - 2022.05.26](#%ED%95%AD%ED%95%B499-6%EA%B8%B0-%EC%8B%A4%EC%A0%84-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-26---20220526)
- [Retrospect](#retrospect)

<!-- /TOC -->

# Retrospect
채팅방과 태그는 M:N 관계를 맺으며 그 사이에 junction 테이블이 존재한다.  
이 테이블에서는 roomID, tagId 만을 입력 받아 채팅방에 포함된 태그들을 관리한다.  

태그를 삽입할 때는 잘 됐는데, 업데이트를 하려니 막막하다.  
우선은 junction 테이블에 관한 레포지토리는 따로 정의를 할 수 없어서 커넥션 연결 후 query builer 를 사용해서 채팅방과 관련된 태그들의 연결을 끊어주고 새로운 태그들을 만들어 연결해주는 형태로 작성을 하였다.
junction 테이블에서 A라는 태그가 더이상 채팅방들과 연결이 되지 않는다면 tag 테이블에서도 삭제를 해주고 싶은데 안나오네..
``` typescript
await getConnection()
  .createQueryBuilder()
  .delete()
  .from('room_tags_tag')
  .where('roomId = :roomId', { roomId: id })
  .execute();

await getConnection()
  .createQueryBuilder()
  .insert()
  .into('room_tags_tag')
  .values(joinTags)
  .execute();
```