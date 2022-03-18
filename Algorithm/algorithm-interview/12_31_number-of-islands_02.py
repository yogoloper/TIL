from re import L
from typing import List


class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    m = len(grid)
    n = len(grid[0])
    cnt = 0

    def dfs_recursive(r, c):
      if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
        return

      # 방문처리
      grid[r][c] = '0'
      for i in range(4):
        dfs_recursive(r + dx[i], c + dy[i])
      return

    for r in range(m):
      for c in range(n):
        node = grid[r][c]
        if node != '1':
          continue

        cnt += 1
        dfs_recursive(r, c)

    return cnt


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

o = Solution()
print(o.numIslands(grid))
# print(o.numIslands(grid2))
