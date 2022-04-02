n = int(input())
lst = list(map(int, input().split()))
m = int(input())

start = 0
end = max(lst)

result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    
    for i in lst:
        if i > mid:
            total += mid
        else:
            total += i
    
    if total > m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)