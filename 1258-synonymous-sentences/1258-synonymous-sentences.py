from collections import defaultdict
class UnionFind:
    def __init__(self, synonyms):
        self.parent = {}
        self.size = {}
        
        for word1,word2 in synonyms:
            self.parent[word1] = word1
            self.parent[word2] = word2
            self.size[word1] = 1
            self.size[word2] = 1
    
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
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        n = len(synonyms)
        uf = UnionFind(synonyms)
        
        for word1, word2 in synonyms:
            uf.union(word1, word2)
        
        d = defaultdict(list)
        
        for k in uf.parent.keys():
            d[uf.find(k)].append(k)
        
        sentence = text.split(' ')
        def dfs(idx):
            if idx == len(sentence)-1:
                if sentence[idx] in uf.parent:
                    curr = d[uf.find(sentence[idx])]
                else:
                    curr = [sentence[idx]]
                
                final = []
                for w in curr:
                    final.append([w])
                return final
            
            arr = dfs(idx+1)
            if sentence[idx] in uf.parent:
                curr = d[uf.find(sentence[idx])]
            else:
                curr = [sentence[idx]]
                
            temp = []
            for word in curr:
                for st in arr: 
                    new_sentence = [word] + st
                    temp.append(new_sentence)
            return temp
                
        ans = dfs(0)
        res = []
        for i in ans:
            st = ' '.join(i) 
            res.append(st)
        output = sorted(res)    
        return output
        
        
            
        
        