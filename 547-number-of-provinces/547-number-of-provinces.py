class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]
        self.component = n
        
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[self.parent[node]])
        return self.parent[node]
        
    def union(self, x, y):
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
            
        self.component -= 1

    
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        
        uf = UnionFind(n)
        
        for i,j in enumerate(isConnected):
            for idx,k in enumerate(j):
                if k == 1:
                    uf.union(i,idx)
        
        print(uf.parent)
        print(uf.size)

        return uf.component
            