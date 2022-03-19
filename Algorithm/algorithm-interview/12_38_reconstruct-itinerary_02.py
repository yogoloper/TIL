from collections import deque
import collections
from curses.ascii import SO
from typing import List
from collections import defaultdict, deque
from bisect import insort

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


tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
tickets2 = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
tickets3 = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
o = Solution()
# print(o.findItinerary(tickets))
# print(o.findItinerary(tickets2))
print(o.findItinerary(tickets3))

