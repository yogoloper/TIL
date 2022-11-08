preValue = [[10], [1], [2, 4, 8, 6], [3, 9, 7, 1], [4, 6], [5], [6], [7, 9, 3, 1], [8, 4, 2, 6], [9, 1]]

t = int(input())

while t > 0:
    t = t -1
    a, b = map(int, input().split())
    
    a = a % 10
    
    if a == 0:
    	print(preValue[0][0])
    elif a == 1 or a == 5 or a == 6:
    	print(preValue[a][0])
    elif a == 4 or a == 9:
    	c = b % 2 - 1
    	print(preValue[a][c])
    elif a == 2 or a == 3 or a == 7 or a == 8:
    	c = b % 4 - 1
    	print(preValue[a][c])
    	
