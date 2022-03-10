# [항해99 6기] 웹미니 프로젝트 주간(2) - 2022.03.08

<!-- TOC -->

- [[항해99 6기] 웹미니 프로젝트 주간2 - 2022.03.08](#%ED%95%AD%ED%95%B499-6%EA%B8%B0-%EC%9B%B9%EB%AF%B8%EB%8B%88-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%A3%BC%EA%B0%842---20220308)
- [Learned](#learned)
  - [메인 페이지 작성](#%EB%A9%94%EC%9D%B8-%ED%8E%98%EC%9D%B4%EC%A7%80-%EC%9E%91%EC%84%B1)
    - [MongoDB](#mongodb)
- [Will learn](#will-learn)
- [Retrospect](#retrospect)

<!-- /TOC -->

# Learned
- 메인 페이지 작성

## 메인 페이지 작성

### MongoDB
1. MongoDB
MonhoDB를 처음 써봤는데  
NoSQL으로 분류되며 RDBMS와는 다음과 같은 차이가 있다.
<table>
  <thead>
    <tr>
      <th></th>
      <th>RDBMS</th>
      <th>NoSQL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>적합한 사용례</td>
      <td>데이터 정합성이 보장되어야 하는 은행 시스템</td>
      <td>낮은 지연 시간, 가용성이 중요한 SNS 시스템</td>
    </tr>
    <tr>
      <td>데이터 모델</td>
      <td>정규화와 참조 무결성이 보장된 스키마</td>
      <td>스키마가 없는 자유로운 데이터 모델</td>
    </tr>
    <tr>
      <td>트랜젝션</td>
      <td>강력한 ACID 지원</td>
      <td>완화된 ACID(BASE)</td>
    </tr>
    <tr>
      <td>확장</td>
      <td>하드웨어 강화(Scale up)</td>
      <td>수평 확장 가능한 분산 아키텍처(Scale out)</td>
    </tr>
    <tr>
      <td>API</td>
      <td>SQL 쿼리</td>
      <td>객체 기반 API 제공</td>
    </tr>
  </tbody>
</table>
2. Content Collection  
MongoDB는 자유로운 데이터 모델을 지원해서  
Collection(=table)에 JSON형태의 데이터를 넣을수 있고  
그렇기에 Object를 저장할 수 있다.  

편의점별로 맥주가격을 넣기 위에 price 안에 JSON 형태의 배열을 저장하였다.  
~~테이블을 여러 개 만들지 않아도 되니 너무 편하다..~~
``` json
{
    "_id": {
        "$oid": "6229d4719581ec8ddcd2f3eb"
    },
    "beer_num": {
        "$numberInt": "1"
    },
    "beer_name": "CASS",
    "beer_type": "밀맥주",
    "beer_company": "하이트 진로",
    "country": "한국",
    "price": [{
        "store": "CU",
        "one": {
            "$numberInt": "2500"
        },
        "four": {
            "$numberInt": "13000"
        }
    }, {
        "store": "GS",
        "one": {
            "$numberInt": "3500"
        },
        "four": {
            "$numberInt": "12000"
        }
    }, {
        "store": "MiniStop",
        "one": {
            "$numberInt": "4000"
        },
        "four": {
            "$numberInt": "13000"
        }
    }],
    "beer_date": "2022-03-02",
    "file": "file-2022-03-08-20-35-33.png"
}
```
3. Python Lambda  
~~테이블 여러개 만들지 않아도 좋다고 한거 취소..~~  
메인 페이지에서는 맥주별로 취급되는 편의점들 중에서 최저가만 노출하고자 하였고  
CASS같은 경우는 1개 가격은 CU의 2500원, 4개 가격은 GS의  12000원이 노출 되어야 한다.

    비교적 익숙한 python을 통해 뽑아온 데이터를 가공하기로 하였고   
아래의 람다식을 통해 1개와 4개의 최저가를 뽑아내 맥주 리스트에 추가해 주었다.
``` python
# 맥주 리스트 조회
    content_list = list(db.content.find({}, {'_id': False}))

    # 맥주별 최저가를 구해서 맥주 리스트에 추가
    for row in content_list:
        row['one_min'] = (min(row['price'], key=(lambda x: x['one'])))['one']
        row['four_min'] = (min(row['price'], key=(lambda x: x['four'])))['four']
```
# Will learn
- 메인 페이지 정렬 추가
- CSS 적용

# Retrospect
일한다고 미루고 논다고 미루고 뭐한다고 미루고  
하다보니 개인 공부를 안하는 습관을 지닌체 지인 회사로 이직을 했다.  
이직 후 시간이 많이 남았음에도 불구하고 나는 여전히 공부를 하지 않았다.  

이제는 다시 바뀌어야 할 때다.