class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]
        self.weight = 0
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[self.parent[node]])
        return self.parent[node]
     
    def union(self, x, y, cost):
        px = self.find(x)
        py = self.find(y)
        
        if px == py:
            return  
        
        if self.size[px] >= self.size[py]:
            self.parent[py] = px
            self.size[px] += self.size[py]
        else:
            self.parent[px] = py
            self.size[py] += self.size[px]
            
        self.weight += cost

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        connections.sort(key = lambda x:x[2])
        
        uf = UnionFind(n)
        
        for start,end,cost in connections:
            uf.union(start-1, end-1, cost)
        
        if max(uf.size) != n:
            return -1
        
        return uf.weight