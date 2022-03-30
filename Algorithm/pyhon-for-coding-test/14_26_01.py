import heapq


n = int(input())
q = []
ans = []

for _ in range(n):
    heapq.heappush(q, int(input()))
    
while len(q) > 1:
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    heapq.heappush(q, a+b)
    ans.append(a+b)
    
print(sum(ans))