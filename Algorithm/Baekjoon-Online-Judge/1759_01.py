l, c = map(int, input().split())
chars = list(input().split())
chars.sort()

vowels = set(['a', 'e', 'i', 'o', 'u'])
visited = [0] * c

def check(encstr):
    count = 0
    for char in encstr:
        if char in vowels:
            count += 1
    return count

def dfs(depth, encstr, idx):
    if depth == l:
        if check(encstr) >= 1 and (len(encstr) - check(encstr)) >= 2:
            print(''.join(encstr))
            return 
    
    for i in range(c):
        if idx < i:
            if not visited[i]:
                visited[i] = 1
                encstr.append(chars[i])
                dfs(depth + 1, encstr, i)
                visited[i] = 0
                encstr.pop()
                
dfs(0, [], -1)