n = int(input())

org = n
cnt = 0

while True:
    tens = n // 10
    units = n % 10
    cal = (tens + units) % 10
    n = units * 10 + cal
    
    cnt += 1
    
    if n == org:
        break

print(cnt)
