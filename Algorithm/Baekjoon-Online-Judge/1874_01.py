from inspect import stack
from re import L


def stack_sequence():
    cnt = int(input())
    sequence = []
    stack = []
    result = []
    seq_idx = 1
    
    for i in range(cnt):
        sequence.append(int(input()))

        if len(stack) == 0:
            for j in range(sequence[i]):
                stack.append(seq_idx)
                result.append("+")
                seq_idx += 1

        while sequence[i] > stack[-1]:
            stack.append(seq_idx)
            result.append("+")
            seq_idx += 1

        while stack and sequence[i] <= stack[-1]:
            stack.pop()
            result.append("-")
            
    if stack:
        print("NO")
    else:
        for i in result:
            print(i)
        
stack_sequence()