# [항해99 6기] 웹미니 프로젝트 주간 (3) - 2022.03.09

<!-- TOC -->

- [[항해99 6기] 웹미니 프로젝트 주간 3 - 2022.03.09](#%ED%95%AD%ED%95%B499-6%EA%B8%B0-%EC%9B%B9%EB%AF%B8%EB%8B%88-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%A3%BC%EA%B0%84-3---20220309)
- [Learned](#learned)
  - [메인 페이지 정렬 추가](#%EB%A9%94%EC%9D%B8-%ED%8E%98%EC%9D%B4%EC%A7%80-%EC%A0%95%EB%A0%AC-%EC%B6%94%EA%B0%80)
- [Will learn](#will-learn)
- [Retrospect](#retrospect)

<!-- /TOC -->

# Learned
- 메인 페이지 정렬 추가
- CSS 적용

## 메인 페이지 정렬 추가
1. Python Lambda
맥주 리스트 전체를 대상으로 람다식을 적용해서 필요에 맞게 정렬하였다.  
~~이제와서 보니 align_type 보다는 sort_type으로 작명하는게 좋겠네..~~
``` python
# 맥주 리스트 정렬
    if align_type == 0: # 기본 정렬
        content_list = content_list
    elif align_type == 1:   # 최근 상품순
        content_list = sorted(content_list, key=(lambda x: x['beer_date']))
    elif align_type == 2:   # 오래된 상품순
        content_list = sorted(content_list, key=(lambda x: x['beer_date']), reverse=True)
    elif align_type == 3:   # 1개 가격 낮은순
        content_list = sorted(content_list, key=(lambda x: x['one_min']))
    elif align_type == 4:   # 1개 가격 높은순
        content_list = sorted(content_list, key=(lambda x: x['one_min']), reverse=True)
    elif align_type == 5:   # 4개 가격 낮은순
        content_list = sorted(content_list, key=(lambda x: x['four_min']))
    elif align_type == 6:   # 4개 가격 높은순
        content_list = sorted(content_list, key=(lambda x: x['four_min']), reverse=True)
    elif align_type == 7:   # 별점 높은순
        content_list = sorted(content_list, key=(lambda x: x['star_point']), reverse=True)
    elif align_type == 8:   # 별점 낮은순
        content_list = sorted(content_list, key=(lambda x: x['star_point']))
    elif align_type == 9:   #  랜덤
        random.shuffle(content_list)
```

# Will learn
- AWS EC2 배포

# Retrospect
내가 작업해야 하는 부분은 90% 완료했다.  
팀원들에게 도움이 필요하면 언제든 요청해도 괜찮다고 했는데  
초반에만 조금 물어보고 나중에는 스스로 해결하는 것 같았다.

요즘 친구들은 스스로 문제 해결을 할 수 있는 역량이 대단한가 보다.  
팀원들은 나보다 한참이나 어린 친구들인데  
그 나이때의 나는 어떻게 문제해결을 했는지 되돌아 보게 된다.