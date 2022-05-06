case = int(input())

for i in range(case):
    x, y = map(int, input().split())

    if y-x <= 1:
        print(1)
    elif y-x == 2:
        print(2)
    elif y-x <= 4:
        print(3)
    else:
        cal = (y - x - 5) // 3
        print(cal + 4)
