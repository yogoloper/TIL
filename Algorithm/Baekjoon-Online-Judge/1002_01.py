case = int(input())

for i in range(case):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    r = ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)
    R = [r1, r2, r]
    m = max(R)
    R.remove(m)
    if r == 0 and r1 == r2:
        print(-1)
    elif r == r1 + r2 or m == sum(R):
        print(1)
    elif m > sum(R):
        print(0)
    else:
        print(2)
