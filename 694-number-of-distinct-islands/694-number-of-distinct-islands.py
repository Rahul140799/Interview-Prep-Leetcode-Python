class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        def dfs(i,j,st):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or not grid[i][j]:
                return ''
            
            grid[i][j] = 0
            
            down = dfs(i+1, j, 'D')
            up = dfs(i-1, j, 'U')
            right = dfs(i, j+1, 'R')
            left = dfs(i, j-1, 'L')
            
            return st + down + up + right + left + '0'
        
        seen = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    seen.add(dfs(i,j,"S"))
        return len(seen)
