import sys
from collections import deque

N = int(sys.stdin.readline())
tree = [[] for i in range(N+1)]
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

queue = deque()
queue.append(1)

ans = [0]*(N+1)

def bfs():
    while queue:
        now = queue.popleft()
        for nxt in tree[now]:
            if ans[nxt] == 0:
                ans[nxt] = now
                queue.append(nxt)

bfs()
res = ans[2:]
for x in res:
    print(x)