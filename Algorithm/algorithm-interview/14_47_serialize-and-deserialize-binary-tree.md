# 이진 트리 직렬화 & 역직렬화

<!-- TOC -->

- [이진 트리 직렬화 & 역직렬화](#%EC%9D%B4%EC%A7%84-%ED%8A%B8%EB%A6%AC-%EC%A7%81%EB%A0%AC%ED%99%94--%EC%97%AD%EC%A7%81%EB%A0%AC%ED%99%94)
  - [문제](#%EB%AC%B8%EC%A0%9C)
  - [에시](#%EC%97%90%EC%8B%9C)
  - [숙고 1](#%EC%88%99%EA%B3%A0-1)
  - [코드 1](#%EC%BD%94%EB%93%9C-1)

<!-- /TOC -->

## 문제
- 문제 : https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
- 직렬화는 데이터 구조 또는 개체를 비트 시퀀스로 변환하여  
  파일 또는 메모리 버퍼에 저장하거나 네트워크 연결 링크를 통해  
  전송하여 나중에 동일하거나 다른 컴퓨터 환경에서 재구성 하는 프로세스이다.
- 이진 트리를 직렬화 및 역직렬화 하는 알고리즘을 설계하여라.  
  직렬화/역직렬화 알고리즘이 작동하는 방식에는 제한이 없다.  
  이진 트리를 문자열로 직렬화할 수 있고 이 문자열을 원래 트리 구조로 역질렬화할 수 있는지 확인하기만 하면 된다.  
-  

## 에시
![Example 1](./images/14_47_serialize-and-deserialize-binary-tree_01.jpeg)
``` python
Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:
Input: root = []
Output: []
```

## 숙고 1
- 직렬화란? 객체의 내용을 바이트 단위로 변환하여 파일 또는 네트워크를 통해서 송수신이 가능하도록 하는 것
- serialize  
  트리의 루트를 받아서 문자열 형태로 반환  
  트리를 받으면 큐를 활용하여 BFS 구조를 통해 배열에 차곡차곡 넣는다.  
  큐를 다 돌면 배열의 값들에 구분자를 추가하여 문자열 형태로 반환한다.
- deserialize  
  문자열을 받아서 트리의 루트를 반환 
  구분자를 통해서 문자열을 배열에 담는다.  
  배열의 0번 인덱스 값을 트리 노드로 만들어 넣고  
  큐를 통해 반복하며 배열의 값들을 노드의 자식들에게 입력한다.
## 코드 1
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/14_47_serialize-and-deserialize-binary-tree_01.py
``` python

class Codec:

    def serialize(self, root):
        # 트리를 담을 배열 선언
        ans = []
        
        # 트리의 루트를 큐에 삽입
        q = deque([root])
        
        # 큐가 있는동안 반복
        while q:
            # 큐에서 노드를 꺼내 배열에 값을 넣고 자식 노드들을 큐에 삽입
            node = q.popleft()
            if node:
                ans.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            # 노드의 값이 없으면 결과에 None 추가
            else:
                ans.append('None')

        # 배열을 문자열 형태로 반환
        return ' '.join(ans)

    def deserialize(self, data):
        # 문자열을 배열 형태도 담는다.
        nodes = data.split()
        
        # 루트가 None이면 None 반환 예외처리
        if nodes[0] == 'None':
            return None
        
        # 반환할 루트 노드 설정
        root = TreeNode(int(nodes[0]))
        # 큐에 루트를 리스트 형식으로 삽입
        q = deque([root])
        # 배열의 값을 관리할 인덱스
        index = 1
        
        # 큐가 있는 동안 반복
        while q:
            # 큐에서 노드를 꺼내고
            node = q.popleft()
            # 배열에서 해당 인덱스의 값을 확인하여
            # 있을 경우 자식 노드로 추가
            if nodes[index] != 'None':
                node.left = TreeNode(int(nodes[index]))
                q.append(node.left)
            # 배열의 다음 인덱스를 확인하기 위해 인덱스 증가
            index += 1
            
            # 배열에서 해당 인덱스의 값을 확인하여
            # 있을 경우 자식 노드로 추가
            if nodes[index] != 'None':
                node.right = TreeNode(int(nodes[index]))
                q.append(node.right)
            # 배열의 다음 인덱스를 확인하기 위해 인덱스 증가
            index += 1
        
        # 루트를 반환            
        return root
```