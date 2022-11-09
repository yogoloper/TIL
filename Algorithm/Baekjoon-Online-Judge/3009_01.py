xDic = {}
yDic = {}
t = 3
while t > 0:
    t = t - 1
    x, y = map(str, input().split())

    if x not in xDic:
        xDic[x] = 1
    else:
        xDic[x] = xDic[x] + 1
    
    if y not in yDic:
        yDic[y] = 1
    else:
        yDic[y] = yDic[y] + 1

x = min(xDic, key=(lambda k: xDic[k]))
y = min(yDic, key=(lambda k: yDic[k]))

print(x, y)
