from collections import deque

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        queue = deque([(start[0], start[1], 0)])
        
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        
        visited = {tuple(start) : 0}
        
        import sys
        ans = sys.maxsize
        
        while queue:
            x,y,distance = queue.popleft()
            
            for i,j in dirs:
                dx = x
                dy = y
                new_distance = distance
                
                while 0 <= dx+i < len(maze) and 0 <= dy+j < len(maze[0]) and maze[dx+i][dy+j] == 0:
                    dx += i
                    dy += j
                    new_distance += 1
                    
                if dx == destination[0] and dy == destination[1]:
                    ans = min(ans, new_distance)
                    continue
                
                if ((dx,dy) not in visited or visited[(dx,dy)] > new_distance):
                    visited[(dx,dy)] = new_distance
                    queue.append((dx,dy,new_distance))
                    
        return -1 if ans == sys.maxsize else ans
                    
        