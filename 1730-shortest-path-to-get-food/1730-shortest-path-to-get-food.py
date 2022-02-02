from collections import deque
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        queue = deque([])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '*':
                    queue.append((i,j,0))
                    visited.add((i,j))
        
        while queue:
            x,y,dist = queue.popleft()
            
            for i,j in dirs:
                dx = x+i
                dy = y+j
                
                if 0 <= dx < len(grid) and 0 <= dy < len(grid[0]):
                    if grid[dx][dy] == '#':
                        return dist + 1
                
                    if grid[dx][dy] == 'O' and (dx,dy) not in visited:
                        new_distance = dist+1
                        queue.append((dx,dy,new_distance))
                        visited.add((dx,dy))

        return -1
        