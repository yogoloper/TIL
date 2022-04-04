import heapq


def dijkstra_pq(graph, start):
    n = len(graph)
    dist = [INF] * n
    
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    
    while q:
      
        acc, cur = heapq.heappop(q)
        
        if dist[cur] < acc:
            continue
        
        for adj, d in graph[cur]:
            cost = acc + d
            if cost < dist[adj]:
                dist[adj] = cost
                heapq.heappush(q, (cost, adj))
    return dist


INF = int(1e9)

n, m  = map(int, input().split())

start = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

print(dijkstra_pq(graph, start))