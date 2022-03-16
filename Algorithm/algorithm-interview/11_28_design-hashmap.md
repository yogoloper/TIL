# 해시맵 디자인

## 문제
- https://leetcode.com/problems/design-hashmap/
- 내장된 해시 테이블 라이브러리를 사용하지 않고 HashMap을 디자인합니다.
- 클래스 구현 MyHashMap:
  - MyHashMap()빈 맵으로 개체를 초기화합니다.
  - void put(int key, int value)(key, value)HashMap에 쌍을 삽입합니다 .  
    key맵에 이미 있는 경우 해당 value.
  - int get(int key)value지정된 매핑 대상을 반환 key하거나 -1이 맵에 에 대한 매핑이 없는 경우 반환합니다 key.
  - void remove(key)맵에 에 대한 매핑이 포함된 경우 key및 해당하는 항목을 제거합니다 .valuekey

## 예시
``` python
Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]
```

## 설명
``` python
MyHashMap myHashMap = 새로운 MyHashMap();
myHashMap.put(1, 1); // 맵은 이제 [[1,1]]입니다.
myHashMap.put(2, 2); // 맵은 이제 [[1,1], [2,2]]입니다.
myHashMap.get(1); // 반환 1, 맵은 이제 [[1,1], [2,2]]입니다.
myHashMap.get(3); // 반환 -1(즉, 찾을 수 없음), 맵은 이제 [[1,1], [2,2]]입니다.
myHashMap.put(2, 1); // 맵은 이제 [[1,1], [2,1]]입니다(즉, 기존 값 업데이트)
myHashMap.get(2); // 반환 1, 맵는 이제 [[1,1], [2,1]]입니다.
myHashMap.remove(2); // 2에 대한 매핑을 제거합니다. 이제 맵은 [[1,1]]입니다.
myHashMap.get(2); // -1을 반환합니다(즉, 찾을 수 없음). 이제 맵은 [[1,1]]입니다.
```

## 숙고 1
- 입력 받는 키를 int 타입으로 받게 되니까 해시 테이블의 공간 크기로 키와 나머지 연산하여  
  해시 테이블의 인덱스로 사용
- put()  
  해시 테이블의 인덱스에 접근해서 Node가 없으면 바로 연결하고,  
  Node가 있다면 Node의 키와 비교하여 키도 같다면 값을 덮어쓴다.  
  키를 비교하여 다르다면 다음 노드로 넘어가서 키를 비교하는 것을 반복한다.  
  더 이상 연결된 노드가 없다면 입력된 노드를 추가한다.
- get()  
  해시 테이블의 인덱스에 접근해서 Node가 없으면 -1을 반환한다.  
  Node가 있다면 Node를 돌면서 key 값을 비교하여  
  같은 key를 찾으면 값을 반환한다.
- remove()  
  해시 테이블의 인덱스에 접근해서 Node가 없으면 종료한다.
  Node가 있다면 Node를 돌면서 key 값을 비교하여  
  같은 Key를 찾으면 이전 Node와 다음 Node를 연결한다.
  다음 Node가 없다면 이전 Node에 None을 연결한다.

## 코드 1
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/11_28_design-hashmap_01.py  
``` python
class MyHashMap:

  def __init__(self):
    self.size = 1000
    self.table = collections.defaultdict(ListNode)

  def put(self, key: int, value: int) -> None:
    index = key % self.size

    if self.table[index].value is None:
      self.table[index] = ListNode(key, value)
      return

    p = self.table[index]
    while p:
      if p.key == key:
        p.value = value
        return
      if p.next is None:
        break
      p = p.next
    p.next = ListNode(key, value)

  def get(self, key: int) -> int:
    index = key % self.size
    if self.table[index].value is None:
      return -1

    p = self.table[index]
    while p:
      if p.key == key:
        return p.value
      p = p.next
    return -1

  def remove(self, key: int) -> None:
    index = key % self.size
    if self.table[index].value is None:
      return

    # 지울때 key로 첫 Node를 지워야 한다면
    p = self.table[index]
    if p.key == key:
      
      # == `self.table[index] = ListNode() if p.next is None else p.next
      #     return`

      # 다음 Node가 없으면 빈 Node를 만들어주고
      if p.next is None:
        self.table[index] = ListNode() 
      # 다음 Node가 있다면 연결해준다
      else:
        self.table[index] = p.next
      return
    

    prev = p
    while p:
      if p.key == key:
        prev.next = p.next
        return

      prev, p = p, p.next
```