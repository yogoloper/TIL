import heapq
import sys
input = sys.stdin.readline

n = int(input())

heap = []
result = []

for _ in range(n):
    num = int(input())
    
    if num == 0:
        if heap:
            # print(heapq.heappop(heap))
            result.append(heapq.heappop(heap))
        else:
            # print(0)
            result.append(0)
    else:
        heapq.heappush(heap, num)

for i in result:
    print(i)