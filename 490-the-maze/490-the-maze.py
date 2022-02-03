from collections import deque
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        queue = deque([])
        queue.append((start[0], start[1]))
        
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        
        visited = set()
        visited.add((start[0], start[1]))
        
        while queue:
            x,y = queue.popleft()
            
            for i,j in dirs:
                dx = x
                dy = y
                flag = 0
                
                while 0 <= dx < len(maze) and 0 <= dy < len(maze[0]) and maze[dx][dy] != 1:
                    dx += i
                    dy += j
                    flag = 1
                
                if flag:
                    dx -= i
                    dy -= j
                
                if dx == destination[0] and dy == destination[1]:
                    return True
                
                if 0 <= dx < len(maze) and 0 <= dy < len(maze[0]) and (dx,dy) not in visited:
                    visited.add((dx,dy))
                    queue.append((dx,dy))
        return False
        
        