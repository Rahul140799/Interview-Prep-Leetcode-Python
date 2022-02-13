class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def dfs(s,temp):
            if not s:
                res.append(temp[:])
                return
            
            for i in range(1,len(s)+1):
                if s[:i] == s[:i][::-1]:
                    dfs(s[i:],temp+[s[:i]])
        
        dfs(s,[])
        return res
    