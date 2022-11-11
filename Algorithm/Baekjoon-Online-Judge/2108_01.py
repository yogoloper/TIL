from collections import defaultdict
from collections import Counter

def modefinder(numbers):
    c = Counter(numbers)
    order = c.most_common()
    maximum = order[0][1]

    modes = []
    for num in order:
        if num[1] == maximum:
            modes.append(num[0])
    return sorted(modes)

t = int(input())
dic = defaultdict(int)
list = []
while t > 0:
    num = int(input())
    list.append(num)
    dic[num] += 1
    t = t - 1

keyList = sorted(dic.keys())

valueDesc = sorted(dic.items(), key=lambda x: x[1], reverse=True)
values = modefinder(list)

avg = int(round(sum(keyList) / len(keyList), 0))
mid = keyList[int(len(keyList) / 2)]
fre = 0
if len(values) == 1:
    fre = values[0]
else:
    fre = values[1]
range = keyList[-1] - keyList[0]

print(avg)
print(mid)
print(fre)
print(range)

