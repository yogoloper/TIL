import sys
input = sys.stdin.readline

while 1:
    n = int(input())

    if n == 0:
        break

    cnt = 0
    for i in range(n + 1, n * 2 + 1):
        check = 0
        for j in range(2, i):
            if i % j == 0:
                check = 1
                break
        if check == 0:
            cnt += 1

    print(cnt)
