from collections import deque
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visited = set()
        
        for i in dislikes:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        
        for i in range(1,n+1):
            queue = deque([(i,1)])
            paint = {i:1}
            
            while queue:
                curr, color = queue.popleft()
                visited.add(curr)
                
                if color != paint[curr]:
                    return False
                
                for val in graph[curr]:
                    if val not in visited:
                        if not color:
                            queue.append((val, 1))
                            paint[val] = 1
                        else:
                            queue.append((val, 0))
                            paint[val] = 0
        return True
    