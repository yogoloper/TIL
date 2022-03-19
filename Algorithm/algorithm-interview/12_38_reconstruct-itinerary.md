# 일정 재구성

<!-- TOC -->

- [일정 재구성](#%EC%9D%BC%EC%A0%95-%EC%9E%AC%EA%B5%AC%EC%84%B1)
  - [문제](#%EB%AC%B8%EC%A0%9C)
  - [예시](#%EC%98%88%EC%8B%9C)
  - [숙고 1](#%EC%88%99%EA%B3%A0-1)
  - [코드 1](#%EC%BD%94%EB%93%9C-1)
  - [숙고 2](#%EC%88%99%EA%B3%A0-2)
  - [코드 2](#%EC%BD%94%EB%93%9C-2)
  - [숙고 3](#%EC%88%99%EA%B3%A0-3)
  - [코드 3](#%EC%BD%94%EB%93%9C-3)

<!-- /TOC -->

## 문제
- https://leetcode.com/problems/reconstruct-itinerary/
- ticket[i] = [fromi, toi]가 한 항공편의 출발 및 도착 공항을 나타내는 항공권 목록이 제공된다.  
  여정을 순서대로 재구성하여 반한하여라.  

  모든 티켓은 "JFK"에서 출발하는 남성의 것이므로 여정은 "JFK"로 시작해야 한다.  
  유효한 여정이 여러 개인 경우 단일 문자열로 읽을 때 어휘 순서가 가장 작은 여정을 반환해야 한다.  

  예를 들어, 여정 ["JFK", "LGA"]는 ["JFK", "LGB"]보다 어휘 순서가 작다.  
  모든 티켓이 하나 이상의 유효한 일정을 구성한다고 가정하며,  
  모든 티켓은 한 번만 사용해야 한다.

## 예시
``` python
Example 1:
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]

Example 2:
Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
```

## 숙고 1
- 티켓을 모두 큐에 넣어준다.
  출발지를 JFK로 지정해주고  
  큐를 반복하면서 출발지가 같은 것을 가져오는 동안 rotate 한다.
  가져오면 큐에서 제거하고 결과에 출발지를 넣어준다.  
  큐가 비면 마지막 목적지도 결과에 넣어준다.  

  이렇게 하면 한바퀴밖에 못돈다..

## 코드 1
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/12_38_reconstruct-itinerary_01.py
``` python
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ans = []
        queue = deque()
        for i in tickets:
            queue.append((i))
        
        depart = "JFK"

        while queue:
            ticket = queue.popleft()
            if ticket[0] == depart:
                ans.append(ticket[0])
                if not queue:
                    ans.append(ticket[1])
                depart = ticket[1]
            else:
                queue.append(ticket)

        return ans
```

## 숙고 2
- 배열을 큐에 넣지 말고 사전을 큐에 넣으면 어떨까  
  사전은 출발지를 키, 목적지를 배열 값으로 정렬해서 넣어보자
- input = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]] 에서 루프를 빠져나오지 못하였다.
## 코드 2
``` python
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # routes = defaultdict(deque)
        # for k,v in tickets:
        #     insort(routes[k], v)

        ans = []

        dict = collections.defaultdict(list)
        for a, b in sorted(tickets, reverse = True):
            dict[a].append(b)
        
        ls = list(zip(dict.keys(), dict.values()))
        queue = deque()
        for i in ls:
            queue.append(i)
        
        depart = "JFK"
        ans.append(depart)
        while queue:
            ticket = queue.popleft()
            
            if ticket[0] == depart and len(ticket[1]) > 0:
                next = ticket[1].pop()
                ans.append(next)
                # if not queue:
                #     ans.append(ticket[1])
                depart = next
                
                if len(ticket[1]) > 0:
                    queue.append(ticket)
            else:
                queue.append(ticket)

        return ans
```

## 숙고 3
- 풀이를 찾아보았다..  
  어렵다 어려워..

## 코드 3
``` python
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        
        # 그래프 순서대로 구성
        for a, b, in sorted(tickets):
            graph[a].append(b)
            
        route, stack = [], ['JFK']
        
        while stack:
            # 반복으로스택을 구성하되 막히는 부분에서 풀어내는 처리
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())
        
        return route[::-1]
```