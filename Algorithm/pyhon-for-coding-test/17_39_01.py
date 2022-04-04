import heapq

def mars(graph):
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    
    N = len(graph)
    dist = [[INF] * N for _ in range(N)]

    q = []
    dist[0][0] = graph[0][0]
    heapq.heappush(q, (graph[0][0], 0, 0))
    while q:
        acc, r, c = heapq.heappop(q)
        
        if dist[r][c] < acc:
            continue
            
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if 0 <= nr < N and 0 <= nc < N:
                cost = dist[r][c] + graph[nr][nc]
                if cost < dist[nr][nc]:
                    dist[nr][nc] = cost
                    heapq.heappush(q, (cost, nr, nc))
    
    return dist[N-1][N-1]

INF = int(1e9)

T = int(input())
for _ in range(T):
    N = int(input())
    graph = []
    for __ in range(N):
        graph.append(list(map(int, input().split())))
        
    print(mars(graph))