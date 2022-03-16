import sys

num_1 = int(input())
numbers_1 = list(map(int, input().split()))
numbers_1 = sorted(numbers_1)

num_2 = int(input())
numbers_2 = list(map(int, input().split()))

if num_1 < len(numbers_1):
  sys.exit(0)
if num_2 < len(numbers_2):
  sys.exit(0)

for i in numbers_2:
  left = 0
  right = num_1 - 1
  
  check = False 
  while left <= right:
    idx = (left + right) // 2
    if i == numbers_1[idx]:
      check = True
      break
    
    if i < numbers_1[idx]:
      right = idx -1
    else:
      left = idx + 1
      
  if check:
    print(1)
  else:
    print(0)    