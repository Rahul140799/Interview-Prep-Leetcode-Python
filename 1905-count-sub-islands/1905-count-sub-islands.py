class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(i,j):
            if i < 0 or i >= len(grid2) or j < 0 or j >= len(grid2[0]) or not grid2[i][j]:
                return True
            
            if grid2[i][j] != grid1[i][j]:
                return False
        
            grid2[i][j] = 0

            down = dfs(i+1, j)
            top = dfs(i-1, j)
            left = dfs(i, j+1)
            right = dfs(i, j-1)

            return down&top&left&right
        
        count = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j]:
                    count += 1 if dfs(i,j) else 0
        return count