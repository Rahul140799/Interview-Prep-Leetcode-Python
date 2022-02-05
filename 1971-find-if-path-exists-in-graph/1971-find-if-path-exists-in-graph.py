from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        
        graph = defaultdict(list)
        visited = [False] * n
        
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        
        def dfs(node):
            if node == destination:
                return True
            
            visited[node] == True
            for val in graph[node]:
                if not visited[val]:
                    visited[val] = True
                    dfs(val)
        
        dfs(source)
        return visited[destination]