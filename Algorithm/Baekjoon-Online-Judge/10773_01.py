n = int(input())
arr = []

while n > 0:
    n -= 1
    
    num = int(input())
    if num == 0:
        if len(arr) > 0:
            arr.pop()
        else:
            print(-1)
            break
    else:
        arr.append(num)

print(sum(arr))