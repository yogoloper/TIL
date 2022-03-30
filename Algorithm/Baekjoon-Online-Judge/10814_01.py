n = int(input())
ans = []

for _ in range(n):
    i, j = map(str, input().split())
    ans.append([int(i), j])

ans = sorted(ans, key = lambda x: (x[0]))

for i in ans:
    print(i[0], i[1])