from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        cnt = 0
        q = deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    q.append((i,j))
                    grid[i][j] == '2' # 재방문 안하기 위해

                    while q:
                        # pop하고 x,y랑 인접한 노드 찾기
                        x, y = q.popleft()
                        for dx, dy in (0,1),(0,-1),(1,0),(-1,0):
                            nx, ny = x+dx, y+dy
                            if 0<=nx<m and 0<=ny<n and grid[nx][ny]=='1':
                                q.append((nx,ny))
                                grid[nx][ny]='2' # 방문체크
                    cnt += 1
        return cnt   
       
a = Solution()
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(a.numIslands(grid))