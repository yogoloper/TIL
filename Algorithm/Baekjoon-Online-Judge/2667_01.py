from typing import List


def numIslands():
  dx = [0, 0, -1, 1]
  dy = [1, -1, 0, 0]
  grid = []
  
  cnt = int(input())
  for i in range(cnt):
    grid.append(list(map(int, str(input()))))

  m = len(grid)
  n = len(grid[0])
  result = []

  def dfs_recursive(r, c):
    if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != 1:
      return

    # 방문처리
    grid[r][c] = 0
    result.append(result.pop() + 1)
    
    for i in range(4):
      dfs_recursive(r + dx[i], c + dy[i])
    return

  for r in range(m):
    for c in range(n):
      node = grid[r][c]
      if node != 1:
        continue
      
      result.append(1)
      dfs_recursive(r, c)
  
  print(len(result))
  result = sorted(result)
  for i in range(len(result)):
    print(result[i] - 1)

numIslands()