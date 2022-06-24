n = int(input())
stack = []

while n > 0:
    n -= 1
    cmd = input()

    if cmd == 'top':
        print(stack[-1])
    elif cmd == 'size':
        print(len(stack))
    elif cmd == 'empty':
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    elif cmd == 'pop':
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    else:
        num = cmd.split()[1]
        stack.append(num)
