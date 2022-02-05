from fractions import Fraction
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        
        for i,val in enumerate(equations):
            graph[val[0]].append((val[1], values[i]))
            reciprocal = Fraction(1/values[i]).limit_denominator()
            graph[val[1]].append((val[0], reciprocal))
        # print(graph)
        
        res = []
        def dfs(start, end, visited, curr):
            if start == end:
                self.flag = 1
                res.append(curr)
                return
            
            val = graph[start]
            for i in val:
                if i[0] not in visited:
                    visited.add(i[0])
                    curr *= i[1]
                    dfs(i[0], end, visited, curr)
                    curr /= i[1]
        
        for i in queries:
            visited = set()
            self.flag = 0
            
            if i[0] not in graph or i[1] not in graph:
                res.append(float(-1))
            else:
                visited.add(i[0])
                dfs(i[0], i[1], visited, float(1)) 
                if not self.flag:
                    res.append(float(-1))
                
        return res