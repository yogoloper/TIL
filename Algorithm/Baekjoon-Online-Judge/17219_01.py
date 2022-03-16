import collections

n, m = map(int, input().split())

sites = {}

for i in range(n):
  site, pw = map(str, input().split(' '))
  sites[site] = pw
 
for i in range(m):
  site = input()
  print(sites[site])
