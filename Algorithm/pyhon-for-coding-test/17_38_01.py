INF = int(1e9)

n, m = map(int, input().split())
dist = [[INF] * (n + 1) for _ in range(n + 1)]

for idx in range(1, n + 1):
    dist[idx][idx] = 0
    
for _ in range(1, n + 1):
    a, b = map(int, input().split())
    dist[a][b] = 1
    
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])
            
result = 0

for cur in range(1, n + 1):
    cnt = 0
    
    for node in range(1, n + 1):
        if dist[cur][node] != INF or dist[node][cur] != INF:
            cnt += 1
    if cnt == n:
        result += 1
print(result)