# [항해99 6기] 실전 프로젝트 (13) - 2022.05.12

<!-- TOC -->

- [[항해99 6기] 실전 프로젝트 13 - 2022.05.12](#%ED%95%AD%ED%95%B499-6%EA%B8%B0-%EC%8B%A4%EC%A0%84-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-13---20220512)
- [Retrospect](#retrospect)

<!-- /TOC -->

# Retrospect
TypeORM과 며칠째 씨름하는 중인데 좀처럼 친해지질 않는다.  
테이블 간의 관계를 지정하려고 OntToMany 등과 같은 데코레이터를 사용했는데,  
관계는 걸렸는데 참조테이블에 없는 데이터를 넣어도 에러가 발생하지 않았다.  

원인은 엔티티에서 관계를 설정하면 TypeORM에서 자동으로 이름이나 컬럼을 지정하게 되는데 내가 참조테이블에 없는 데이터를 넣어도 사실 TypeORM에서 지정해준 컬럼이 아니기에 에러가 발생하지 않았다.  

아래와 같은 방식으로 관계가 설정되는 컬럼명을 명시해 주는것이 좋을 것 같다.
``` typescript
  @ManyToOne(() => Category, (category) => category.id )
  @JoinColumn({
    name:'categoryId',
    referencedColumnName:'id'
  })
  categoryId: Category;
```