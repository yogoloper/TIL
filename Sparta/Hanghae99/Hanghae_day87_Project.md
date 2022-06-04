# [항해99 6기] 실전 프로젝트 (33) - 2022.06.02

<!-- TOC -->

- [[항해99 6기] 실전 프로젝트 33 - 2022.06.02](#%ED%95%AD%ED%95%B499-6%EA%B8%B0-%EC%8B%A4%EC%A0%84-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-33---20220602)
- [Retrospect](#retrospect)

<!-- /TOC -->

# Retrospect
채팅방의 상태를 수동으로 업데이트를 하면서 테스트 했는데 프로젝트 기간도 끝났고 해서 MySQL의 이벤트를 활용해서 10분 마다 채팅방의 유효 시간을 확인하고 확성화, 비활성화 하도록 설정하였다.

우선 이벤트 스케쥴러가 동작중인지 확인한다.
``` SQL
show variables like 'event%';
SET GLOBAL event_scheduler = ON;
```

이벤트 리스트 확인
``` SQL
SELECT * FROM information_schema.events;
```

이벤트 생성
``` SQL
CREATE EVENT Active_Room 
ON SCHEDULE EVERY 10 MINUTE
STARTS '2022-06-01 00:00:00'
COMMENT '채팅방 활성화'
DO
UPDATE room SET status = 1
WHERE startdate <= NOW() AND NOW() <= enddate AND status = 0

CREATE EVENT InActive_Room 
ON SCHEDULE EVERY 10 MINUTE
STARTS '2022-06-01 00:00:00'
COMMENT '채팅방 비활성화'
DO
UPDATE room SET status = 2
WHERE enddate <= NOW() AND status = 1
```

이벤트 삭제
``` SQL
DROP EVENT Active_Room
DROP EVENT InActive_Room
```

그리고 대부분의 DB들의 시간을 이용하다보면 시간 차이가 발생하게 되는데 MySQL도 예외는 아니다.  
따라서 타임좀 설정이 필요하다.  

타임존 설정 확인
``` SQL
select @@global.time_zone, @@session.time_zone,@@system_time_zone;
```

타임존 설정
``` SQL
SET GLOBAL time_zone = 'Asia/Seoul'
SET time_zone = 'Asia/Seoul'
```