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
            return False
        
        if self.size[px] >= self.size[py]:
            self.size[px] += self.size[py]
            self.parent[py] = px
        else:
            self.size[py] += self.size[px]
            self.parent[px] = py
            
        return True
    
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n)
        
        for i,j in edges:
            x = uf.union(i-1, j-1)
            if x == False:
                left, right = i,j
        return [left, right]
        