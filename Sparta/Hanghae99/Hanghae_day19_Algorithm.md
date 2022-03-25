# [항해99 6기] 알고리즘 주간(14) - 2022.03.24

<!-- TOC -->

- [[항해99 6기] 알고리즘 주간14 - 2022.03.24](#%ED%95%AD%ED%95%B499-6%EA%B8%B0-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%A3%BC%EA%B0%8414---20220324)
- [Learned](#learned)
  - [heap](#heap)
    - [heap 구현 방법최대 힙](#heap-%EA%B5%AC%ED%98%84-%EB%B0%A9%EB%B2%95%EC%B5%9C%EB%8C%80-%ED%9E%99)
    - [heap 구현 코드최대 힙](#heap-%EA%B5%AC%ED%98%84-%EC%BD%94%EB%93%9C%EC%B5%9C%EB%8C%80-%ED%9E%99)
    - [heapq](#heapq)
  - [배열의 k번째 큰 요소](#%EB%B0%B0%EC%97%B4%EC%9D%98-k%EB%B2%88%EC%A7%B8-%ED%81%B0-%EC%9A%94%EC%86%8C)
  - [[boj]최소 힙](#boj%EC%B5%9C%EC%86%8C-%ED%9E%99)
  - [[boj]최대 힙](#boj%EC%B5%9C%EB%8C%80-%ED%9E%99)
- [Retrospect](#retrospect)

<!-- /TOC -->

# Learned
- heap
- 배열의 k번째 큰 요소
- [boj]최소 힙
- [boj]최소 대

## heap
- 완전 이진 트리의 일종으로 우선순위 큐를 위하여 만들어진 자료구조이다.
- 여러 개의 값들 중에서 최대값/최소값을 빠르게 찾아내도록 만들어진 자료구조이다.
- 힙은 일종의 반정렬 상태(느슨한 정렬 상태) 를 유지한다.  
  큰(작은) 값이 상위 레벨에 있고 작은(큰) 값이 하위 레벨에 있다는 정도이며,  
  좌우 자식의 대소비교는 하지 않는다.
- 힙 트리에서는 중복된 값을 허용한다.
- 계산 편의를 위해 인덱스는 1부터 사용한다. (parent: x, left: 2x, right: 2x+1)

### heap 구현 방법(최대 힙)
- 파이썬에서는 0번 인덱스 부터 사용하도록 구현되어있지만,  
  강의 내용 처럼 인덱스 사용에 혼동을 줄이기 위해서 0번 인덱스에는 None을 넣고  
  1번 인덱스를 루트로 사용하도록 한다.
- __init__()  
  하나의 None 요소를 가진 멤버 리스트를 초기화한다.  

- __len__()  
  매직 메서드를 오버라이딩 하기 위해 __len__로 한수 선언  

  멤버 리스트의 첫 번재 요소 None은 사용하지 않는 요소이기 때문에  
  멤버 리스트의 길이 - 1을 하여 반환한다.  

- _percolate_up()  
  heap에 요소를 추가하게 되면 제일 뒷 부분에 추가하게 되는데  
  입력된 마지막 요소와 그 부모의 요소값을 비교하여 마지막 요소가 크다면 두 요소를 바꿔준다.  
  바뀐 자리에서의 부모 요소와 값을 비교하고 교체하며 반복된다.  
  부모 요소의 인덱스가 1일때까지만 진행한다.  
  -> 부모 요소가 1 미만이라는 얘기는 현재 요소가 루트라는 의미이다.

- _percolate_down(cur)  
  heap에서 요소를 추출하려면 제일 위의 요소와 제일 아래요소를 바꾼뒤  
  제일 위 였던 요소가 추출된다.  
  제일 아래에 있던 요소를 제자리로 찾아주기 위해서 두 자식들과 비교하여  
  제일 높은 요소를 위로 올리며 자리를 찾아 내려간다.
  
  다음 바퀴는 재귀를 통해 진행한다.
  
- insert(k)  
  멤버 리스트 마지막에 요소를 추가하고,  
  percolate_up()을 통해 순서에 맞는 자리를 찾아 올라간다.

- extract()  
  첫 요소를 뽑아내기 내기 위해 끝에 있던 요소와 자리를 바꾸고 추출한다.  
  percolate_down()를 통해서 힙의 정렬을 진행한다.

### heap 구현 코드(최대 힙)
``` python
class Heap:
    # None을 요소로 가진 리스트 할당
    def __init__(self):
        self.items = [None]
    
    # 0번 인덱스는 사용하지 않을거기 때문에
    # magic method OverRiding 해서 멤버 리스트 전체 길이에서 -1을 하여 반환
    def __len__(self):
        return len(self.items) - 1

    # 리스트에 마지막에 요소 추가 후 자리를 찾아주려 올려보낸다.
    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    # 요소를 제거하기 위해 첫요소와 마지막요소 변경후
    # 마지막 요소였던 요소의 자리를 찾아주러 내려보낸다.
    # 첫요소였던 요소를 반환한다.
    def extract(self):
        # 리스트의 길이가 1 미만이라는 것은 힙 요소가 없다는 뜻
        if len(self) < 1:
            return None

        # 반환하기 위헤 주소 복사
        root = self.items[1]
        # 첫요소와 마지막 요소 자리 변경
        self.items[1] = self.items[-1]
        # 첫요소였던 요소를 제거
        self.items.pop()
        # 마지막 요소였던 요소의 자리 찾기
        self._percolate_down(1)

        return root

    # 자리 찾아 올려보내기
    def _percolate_up(self):
        # 추가된 요소는 최대 길이를 가지고 있으며
        cur = len(self)

        # 길이의 나누기를 하면 부모 요소를 가리키게 된다.
        parent = cur // 2

        # 부모가 0이라는 것은 자신이 루트라는 의미이다.
        while parent > 0:
            # 자신이 부모요소의 값보다 큰경우
            if self.items[cur] > self.items[parent]:
                # 두 요소를 바꿔준다.
                self.items[cur], self.items[parent] = self.items[parent], self.items[cur]
            
            # 요소를 다시 올려보내기 위해 자신의 인덱스와
            # 그 위의 부모 인덱스를 구해온다.
            cur = parent
            parent = cur // 2

    # 자리 찾아 내려보내기
    def _percolate_down(self, cur):
        # 첫 요소를 제일 큰값으로 지정
        biggest = cur
        # 자식 요소들은 현재 요소 인덱스에 *2, *2+1하면 좌우 자식 요소를 가져올수 있다.
        left = cur * 2
        right = cur * 2 + 1

        # 상위 요소값과 왼쪽 자식 요소값을 비교하여 큰값을 올려준다.
        if left <= len(self) and self.items[left] > self.items[biggest]:
            biggest = left

        # 상위 요소값과 오른쪽 자식 요소값을 비교하여 큰값을 올려준다.
        if right <= len(self) and self.items[right] > self.items[biggest]:
            biggest = right

        # 제일 큰 값이 첫요소가 아닌경우
        if biggest != cur:
            # 자식의 위치와 변경한 후
            self.items[cur], self.items[biggest] = self.items[biggest], self.items[cur]
            # 재귀를 통해서 다음 레벨에서 위치를 확인한다.
            self._percolate_down(biggest)
```
### heapq
사실 힙이 구현되어있다.
위에서 구현한 것과 다른 점은 최소 힙으로 구현,  
그리고 인덱스를 0부터 사용한다는 것이다.

## 배열의 k번째 큰 요소
- 문제 : https://leetcode.com/problems/kth-largest-element-in-an-array/
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/programmers/15_55_kth-largest-element-in-an-array.md  

## [boj]최소 힙
- 문제 : https://www.acmicpc.net/problem/1927
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/Baekjoon-Online-Judge/1927.md  

## [boj]최대 힙
- 문제 : https://www.acmicpc.net/problem/11279
- 풀이 : https://github.com/yogoloper/TIL/blob/master/Algorithm/Baekjoon-Online-Judge/11279.md  

# Retrospect
힙은 정말 힙하다.  
학부때 배운것 같은데 힙에 대한 내용은 전혀 기억이 나질 않는다.  
학부때 열심히 했던거 같은데  
아마 이해를 하지 못해서 기억에도 없는거겠지.. 라고 생각하며 반성하는 하루다.