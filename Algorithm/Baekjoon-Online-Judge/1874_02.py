from inspect import stack
from re import L


def stack_sequence():
    cnt = int(input())
    stack = []
    result = []
    seq_idx = 1
    success = True
    
    for i in range(cnt):
        num = int(input())

        while seq_idx <= num:
            stack.append(seq_idx)
            result.append("+")
            seq_idx += 1

        if stack[-1] == num:
            stack.pop()
            result.append("-")
        else:
            print("NO")
            success = False
            break
            
    if success:
        for i in result:
            print(i)
        
stack_sequence()