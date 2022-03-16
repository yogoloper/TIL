import sys

num_1 = int(input())
numbers_1 = list(map(int, input().split()))

if num_1 < len(numbers_1):
  sys.exit(0)

num_2 = int(input())
numbers_2 = list(map(int, input().split()))

if num_2 < len(numbers_2):
  sys.exit(0)
  
for i in numbers_2:
  if i in numbers_1:
    print(1)
  else:
    print(0)
    
