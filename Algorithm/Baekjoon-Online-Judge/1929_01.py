n, m = map(int, input().split())

for i in range(n, m + 1):
    check = True
    for j in range(2, i):
        if i % j == 0:
            check = False
            break
    if check:
        print(i)
            
