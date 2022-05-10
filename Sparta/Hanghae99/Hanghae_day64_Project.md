# [항해99 6기] 실전 프로젝트 (11) - 2022.05.10

<!-- TOC -->

- [[항해99 6기] 실전 프로젝트 11 - 2022.05.10](#%ED%95%AD%ED%95%B499-6%EA%B8%B0-%EC%8B%A4%EC%A0%84-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-11---20220510)
- [Retrospect](#retrospect)

<!-- /TOC -->

# Retrospect
오늘은 TypeORM의 ManyToMany를 구현한다고 꽤 많은 시간을 소비하였다.  
채팅방을 개설할때 태그를 설정할 수 있는데 이 부분을 연결 테이블을 사용해서 ManyToMany로 작성하였다.  

채팅방 엔티티에서만 아래와 같이 관계를 연결해주면 room_tags_tag 테이블이 생성된다.
``` typescript
// room.entity.ts

  @ManyToMany(() => Tag)
  @JoinTable()
  tags: Tag[];
```

['tag1', 'tag2'] 와 같이 온 tags를 Tag 테이블에 차례로 삽입(있으면 조회)하고  
삽입(조회) 내용을 Tag[] 배열로 반환한다.
``` typescript
@EntityRepository(Tag)
export class TagRepository extends Repository<Tag> {
  async findOrInsert(tags: String[]): Promise<Tag[]> {
    let roomTags: Tag[] = [];

    for (const tag of tags) {
      const findTag = await this.findOne({
        name: tag.toString(),
      });

      if (findTag) {
        roomTags.push(findTag);
      } else {
        const insertTag = this.create({
          name: tag.toString(),
        });
        await this.save(insertTag);
        roomTags.push(insertTag);
      }
    }

    return roomTags;
  }
}
```

Tag[] 배열을 받아와서 Room 엔티티에서 정의한대로 입력해주면 연결 테이블에도 데이터가 잘 들어간다.
``` typescript
async createRoom(createRoomDto: CreateRoomDto): Promise<void> {
    const {
      title,
      positionX,
      positionY,
      startDate,
      endDate,
      categoryId,
      maxUser,
      imageUrl,
      regionAId,
      regionBId,
      tags,
    } = createRoomDto;

    const roomTags = await this.tagRepository.findOrInsert(tags);

    const room = this.roomRepository.create({
      userId: 1,
      title,
      positionX,
      positionY,
      startDate,
      endDate,
      categoryId,
      maxUser,
      imageUrl,
      regionAId,
      regionBId,
      status: new Date(startDate) <= new Date() ? 1 : 0,
      tags: roomTags,
    });

    await this.roomRepository.save(room);
  }
``` 

오늘 애를 먹은 부분을 정확히 얘기하면 CreateRoomDto에서도 tags의 타입을 Tag[]로 지정했는데 원하는 데이터를 제대로 뽑아올수 없었다. CreateRoomDto의 tags를 String[] 타입으로 변환하여서 처리가 가능했다.