class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        row = {}
        col = {}
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if i not in row:
                        row[i] = 1
                    else:
                        row[i] += 1
                    if j not in col:
                        col[j] = 1
                    else:
                        col[j] += 1
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if row[i] > 1 or col[j] > 1:
                        res += 1
        return res