class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)] 
        self.size = [1 for i in range(size)]
        self.count = size
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[self.parent[node]])
        return self.parent[node]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        
        if px != py:
            if self.size[px] > self.size[py]:
                self.parent[py] = px
            elif self.size[px] < self.size[py]:
                self.parent[px] = py
            else:
                self.parent[py] = px
                self.size[px] += 1
            self.count -= 1

            
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        
        logs.sort(key = lambda x:x[0])
        
        uf = UnionFind(n)
        
        for val,x,y in logs:
            uf.union(x,y)
            if uf.count == 1:
                return val
        return -1
            
    