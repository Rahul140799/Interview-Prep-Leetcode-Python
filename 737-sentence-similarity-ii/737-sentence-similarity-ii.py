class UnionFind:
    def __init__(self, n, similarPairs):
        self.parent = {}
        self.size = {}
        
        for val1,val2 in similarPairs:
            self.parent[val1] = val1
            self.parent[val2] = val2
            self.size[val1] = 1
            self.size[val2] = 1
    
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
            self.parent[py] = px
            self.size[px] += self.size[py]
        else:
            self.parent[px] = py
            self.size[py] += self.size[px]

class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        n = len(sentence1)
        uf = UnionFind(n, similarPairs)
        
        for i,val in enumerate(similarPairs):
            uf.union(val[0],val[1])
        
        pairs = list(zip(sentence1, sentence2))
        
        for val1, val2 in pairs:
            if val1 == val2:
                continue
                
            if val2 not in uf.parent or val1 not in uf.parent or uf.find(val1) != uf.find(val2):
                return False
        return True