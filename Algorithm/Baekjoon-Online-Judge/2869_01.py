a, b, v = map(int, input().split())

move = a - b
day = v // move
if v % move != 0:
    day += 1

print(day)