from collections import defaultdict
class UnionFind:
    def __init__(self, accounts):
        self.parent = {}
        self.size = {}
        self.mapper = {}
        
        for i, val in enumerate(accounts):
            for j in val[1:]:
                self.parent[j] = j
                self.size[j] = 1
                self.mapper[j] = i
                
    
    def find(self, email):
        while self.parent[email] != email:
            email = self.parent[self.parent[email]]
        return email
    
    
    def union(self, email1, email2, i):
        px = self.find(email1)
        py = self.find(email2)
        
        if px == py:
            return 
        
        if self.size[px] >= self.size[py]:
            self.parent[py] = px
            self.size[px] += self.size[py]
            self.mapper[px] = i
        else:
            self.parent[px] = py
            self.size[py] += self.size[px]
            self.mapper[py] = i

        
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(accounts)
        
        for i,val in enumerate(accounts):
            for l in range(1,len(val)-1):
                uf.union(val[l], val[l+1], i)
        
        d = defaultdict(list)
        for i in uf.mapper:
            d[uf.find(i)].append(i)
        
        res = []
        for i in d:
            name = accounts[uf.mapper[i]][0]
            temp = [name]
            sorted_emails = sorted(d[i])
            final = temp + sorted_emails
            res.append(final)
        return res
        