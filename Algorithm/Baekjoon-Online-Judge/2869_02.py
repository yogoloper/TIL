a, b, v = map(int, input().split())

move = a - b
day = (v - a) // move + 1
if (v - a) % move != 0:
    day += 1

print(day)