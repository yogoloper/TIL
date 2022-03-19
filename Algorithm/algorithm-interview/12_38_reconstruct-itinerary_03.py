import collections
from typing import List


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

tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
tickets2 = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
tickets3 = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
o = Solution()
# print(o.findItinerary(tickets))
print(o.findItinerary(tickets2))
# print(o.findItinerary(tickets3))
