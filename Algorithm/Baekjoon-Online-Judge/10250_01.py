test = int(input())

while test > 0:
    h, w, n = map(int, input().split())

    no = n // h + 1
    floor = n % h
    if floor == 0:
        no -= 1
        floor = h

    room = str(floor) + str(no).zfill(2)
    print(room)

    test -= 1
