INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * ( n + 1) for _ in range(n + 1)]

for idx in range(1, n + 1):
    graph[idx][idx] = 0
    
for _ in range(m):
    a, b, c = map(int, input().split())
    if c < graph[a][b]:
        graph[a][b] = c

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for row in graph[1:]:
    print(' '.join([str(el) if el != INF else '0' for el in row[1:]]))
