def is_valid_parenthesis():

    cnt = int(input())

    for i in range(cnt):
        brackets = input()

        stack = []

        for j in brackets:
            if j == '(':
                stack.append(j)
            else:
                if stack and stack[-1] == "(":
                    top = stack.pop()
                else:
                    stack.append(j)
                    break
        
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")
            
is_valid_parenthesis()