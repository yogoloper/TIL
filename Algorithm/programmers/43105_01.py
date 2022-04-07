def solution(triangle):
    INF = int(1e9)
    answer = 0
    n = len(triangle)
    
    memo = [[INF] * (i + 1) for i in range(n)]
    memo[0][0] = triangle[0][0]
    
    def dp(r, c):
        if not (0 <= r < n and 0 <= c < len(triangle[r])):
            return 0

        if memo[r][c] != INF:
            return memo[r][c]
        
        memo[r][c] = triangle[r][c] + max(dp(r-1, c-1), dp(r-1, c))
        return memo[r][c]
    
    for col in range(n):
        dp(n-1, col)
        
    answer = max(memo[n-1])
    
    return answer


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))