from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]:
            return -1
        
        queue = deque([(0,0,1)])
        dirs = [(0,1), (0,-1), (-1,0), (1,0), (-1,-1), (1,1), (1,-1), (-1,1)]
        
        visited = set()
        visited.add((0,0))
        
        while queue:
            x,y,dist = queue.popleft()
            
            for i,j in dirs:
                dx = x+i
                dy = y+j
                
                if (dx,dy) == (len(grid)-1, len(grid[0])-1):
                    return dist+1
                
                if 0 <= dx < len(grid) and 0 <= dy < len(grid[0]) and not grid[dx][dy] and (dx,dy) not in visited:
                    queue.append((dx,dy,dist+1))
                    visited.add((dx,dy))
        return dist if (len(grid)-1, len(grid[0])-1) in visited else -1
            
        