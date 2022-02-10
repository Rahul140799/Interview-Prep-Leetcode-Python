from collections import deque 
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        d = {}
        n = len(graph)
        visited = set()
        
        for i, val in enumerate(graph):
            d[i] = val
        
        for i in range(n):
            queue = deque([(i,1)])
            paint = {i:1}

            while queue:
                node, color = queue.popleft()
                visited.add(node)

                if paint[node] != color:
                    return False

                for curr in d[node]:
                    if curr not in visited:
                        if not color:
                            queue.append((curr,1))
                            paint[curr] = 1
                        else:
                            queue.append((curr,0))
                            paint[curr] = 0
        return True
            