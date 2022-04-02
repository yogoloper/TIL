n, m = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(int(input()))

start = 0
end = min(lst)

result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    
    for i in lst:
        total += (i //  mid)
    
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)