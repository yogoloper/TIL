t = int(input())

while t > 0:
    a, b = map(int, input().split())
    print(a ** b % 10)
    t = t - 1