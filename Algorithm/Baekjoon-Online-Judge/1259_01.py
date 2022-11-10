num = input()

while num != '0':
    numArr = list(num)
    numArr2 = list(num)
    numArr2.reverse()
    
    if numArr == numArr2:
        print('yes')
    else:
        print('no')
        
    num = input()