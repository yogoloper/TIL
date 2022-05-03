import sys
input = sys.stdin.readline

n = int(input())

minCnt = 0

while n >= 0:
    if n % 5 == 0:
        minCnt += n // 5
        break
    n -= 3
    minCnt += 1
else:
    minCnt = -1

print(minCnt)
