import sys

input = sys.stdin.readline
n = int(input())
queue = []

while n > 0:
    n -= 1
    cmd = input().strip()

    if cmd == 'front':
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)

    elif cmd == 'back':
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)

    elif cmd == 'size':
        print(len(queue))

    elif cmd == 'empty':
        if len(queue) > 0:
            print(0)
        else:
            print(1)
            
    elif cmd == 'pop':
        if len(queue) > 0:
            print(queue.pop(0))
        else:
            print(-1)
            
    else:
        num = cmd.split()[1]
        queue.append(num)
