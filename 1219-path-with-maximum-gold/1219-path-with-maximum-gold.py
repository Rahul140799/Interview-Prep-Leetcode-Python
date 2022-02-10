class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        def dfs(i,j,gold):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or not grid[i][j]:
                return gold
            
            tmp = grid[i][j]
            gold += grid[i][j]
            grid[i][j] = 0
            
            down = dfs(i+1, j, gold)
            up = dfs(i-1, j, gold)
            right = dfs(i, j+1, gold)
            left = dfs(i, j-1, gold)
            
            grid[i][j] = tmp
            gold -= grid[i][j]
            
            return max(down,left,right,up)
            
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    res = max(res, dfs(i,j,0))
        return res