from collections import deque
from curses.ascii import SO
from typing import List


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


tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
o = Solution()
print(o.findItinerary(tickets))