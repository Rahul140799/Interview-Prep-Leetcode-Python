class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        if len(graph) == 1:
            return 0
        
        n = len(graph)
        
        end = (1 << n) - 1
        queue = [(node, 1 << node) for node in range(n)]
        
        visited = set(queue)
        level = 0
        
        while queue:
            li = []
            for node, mask in queue:
                for val in graph[node]:
                    new_val = mask | (1 << val)
                    
                    if new_val == end:
                        return level + 1
                    
                    if (val, new_val) not in visited:
                        visited.add((val, new_val))
                        li.append((val, new_val))
                        
            level += 1
            queue = li