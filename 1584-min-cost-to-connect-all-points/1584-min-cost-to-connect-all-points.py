class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]
    
    def find(self, node):
        while self.parent[node] != node:
            node = self.parent[self.parent[node]]
        return node
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        
        if px == py:
            return 
        
        if self.size[px] >= self.size[py]:
            self.size[px] += self.size[py]
            self.parent[py] = px
        else:
            self.size[py] += self.size[px]
            self.parent[px] = py

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        edges = []
        for i in range(n):
            for j in range(i+1,n):
                dist = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                edges.append((dist, i, j))
                
        edges.sort()
        
        uf = UnionFind(n)
        amount = 0
        
        for cost,u,v in edges:
            if uf.find(u) != uf.find(v):
                uf.union(u,v)
                amount += cost
        
        return amount
        