from collections import deque
class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        
        queue = deque([(start[0], start[1], 0)])
        
        visited = set()
        visited.add((start[0], start[1]))
        
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        needed = []
        
        if pricing[0] <= grid[start[0]][start[1]] <= pricing[1]:
            needed.append((start[0], start[1], 0, grid[start[0]][start[1]]))
        
        m = len(grid)
        n = len(grid[0])
        
        while queue:
            x, y, distance = queue.popleft()
            
            for i,j in directions:
                dx = i+x
                dy = j+y
                
                if 0 <= dx < m and 0 <= dy < n and (dx, dy) not in visited and grid[dx][dy] > 0:
                    new_distance = distance + 1
                    if pricing[0] <= grid[dx][dy] <= pricing[1]:
                        needed.append((dx, dy, new_distance, grid[dx][dy]))
                    queue.append((dx, dy, new_distance))
                    visited.add((dx,dy))
        
        needed.sort(key = lambda x:(x[2],x[3],x[0],x[1]))
        
        ans = []
        
        for i in needed:
            if len(ans) < k:
                ans.append([i[0], i[1]])
        return ans                    
        