n = int(input())

lst = set()

for _ in range(n):
    lst.add(input())

lst = sorted(list(lst), key = lambda x: (len(x), x))

for i in lst:
    print(i)