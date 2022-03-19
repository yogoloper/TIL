from collections import deque
from re import L
from typing import List


class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    rows, cols = len(grid), len(grid[0])
    cnt = 0
    
    for row in range(rows):
      for col in range(cols):
        if grid[row][col] != '1':
          continue
        
        cnt += 1
        q = deque([(row, col)])
                
        while q:
          x, y = q.popleft()
          for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != '1':
              continue
            grid[nx][ny] = '0'
            q.append([nx, ny])
            
    return cnt


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

o = Solution()
print(o.numIslands(grid))
# print(o.numIslands(grid2))