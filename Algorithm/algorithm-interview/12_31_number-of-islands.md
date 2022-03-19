# 섬의 개수

<!-- TOC -->

- [섬의 개수](#%EC%84%AC%EC%9D%98-%EA%B0%9C%EC%88%98)
  - [문제](#%EB%AC%B8%EC%A0%9C)
  - [예시](#%EC%98%88%EC%8B%9C)
  - [숙고 1](#%EC%88%99%EA%B3%A0-1)
  - [코드 1](#%EC%BD%94%EB%93%9C-1)
  - [숙고 2](#%EC%88%99%EA%B3%A0-2)
  - [코드 2](#%EC%BD%94%EB%93%9C-2)
  - [숙고 3](#%EC%88%99%EA%B3%A0-3)
  - [코드 3](#%EC%BD%94%EB%93%9C-3)

<!-- /TOC -->

## 문제
- https://leetcode.com/problems/number-of-islands/
- 1(땅), 0(물)의 지도를 나타내는 m * n 2D 이진 그리드가 주어지면 섬의 수를 반환한다.
- 섬은 물로 둘러 쌓여 있으며 인접한 육지를 수평 또는 수직으로 연결하여 형성된다.  
  그리드의 네 모서리가 모두 물로 둘러싸여 있다고 가정할 수 있다.

## 예시
``` python
Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

## 숙고 1
- 스택을 사용한 방법의 풀이  
- 감이 잡히지 않아서 풀이 방법을 찾아보았다.
- 전달 받은 배열의 크기만큼 행과 열을 반복하며 1을 확인한다. 
  1을 발견하면 카운트를 추가하고  
  스택에 넣어준다.

  스택이 있는동안 반복을 돌며 상하좌우의 노드를 확인한다.
  스택에서 pop()하여 해당 칸의 값이 1인경우 섬인것을 확인했다는 의미로 0으로 전환한다.  
  dx, dy를 통해 0으로 전환한 칸에서 상하좌우를 비교한다.  
  상하좌우 비교시 grid를 벗어 나지 않는지 체크하며, 1인것을 발견하면 스택에 쌓아준다.  
  스택에 쌓아준다. 것은 섬이라는 의미이다.
## 코드 1
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/12_31_number-of-islands_01.py
``` python
class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    # 상하좌우 비교하기 위한 인덱스
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    # grid 크기를 변수에 할당
    rows, cols = len(grid), len(grid[0])
    cnt = 0
    
    # grid 크기 만큼 동작
    for row in range(rows):
      for col in range(cols):
        # 해당 칸이 0이라면 스킵
        if grid[row][col] != '1':
          continue
        
        # 1이라면 섬이라는 의미이므로 카운트
        cnt += 1
        # 섬의 연결을 위해 스택 push
        stack = [(row, col)]
        
        # 스택이 있는동안 반복
        while(stack):
          # 스택에 들어간 건 섬이라는 의미
          x, y = stack.pop()
          # 해당 칸을 0으로 전환
          grid[x][y] = '0'
          
          # 상하좌우 비교하기 위해 반복
          for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # grid를 벗어나거나 0이면 스킵
            if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != '1':
              continue

            # 1이면 스택에 담아준다.
            stack.append((nx, ny))
    return cnt
```

## 숙고 2
- 재귀를 이용한 풀이방법
- 재귀는 언제나 이해하기가 어렵다.  
  grid의 크기만큼 반복하며 1이 있는 칸을 찾으면 해당 칸의 인덱스를 넘겨주며 재귀함수를 호출한다.  
  
  재귀함수에 들어온 인덱스가 1이라면 0으로 만들어 주고  
  상하좌우의 크기인 4만큼 반복하며 상하좌우를 증감시키며 재귀함수를 호출한다.

## 코드 2
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/12_31_number-of-islands_02.py
``` python
class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    # 상하좌우 비교하기 위한 인덱스
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    # grid 크기를 변수에 할당
    m = len(grid)
    n = len(grid[0])
    cnt = 0

    # 상하좌우의 섬이 있는지를 확인하기 위한 재귀함수
    def dfs_recursive(r, c):
      if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
        return

      # 재귀함수를 통해 들어온 인덱스를 방문처리
      grid[r][c] = '0'
      # 상하좌우는 총 4개니까 4번 반복하며 재귀함수를 호출
      for i in range(4):
        dfs_recursive(r + dx[i], c + dy[i])
      return

    # 섬의 크기만큼 반복
    for r in range(m):
      for c in range(n):
        node = grid[r][c]
        if node != '1':
          continue
        
        # 1이라면 재귀함수를 통해 연결된 섬을 확인
        cnt += 1
        dfs_recursive(r, c)

    return cnt
```

## 숙고 3
- 큐를 이용해 BFS로 푸는 방법도 있었다.

## 코드 3
- https://github.com/yogoloper/TIL/blob/master/Algorithm/algorithm-interview/12_31_number-of-islands_03.py
``` python
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
```