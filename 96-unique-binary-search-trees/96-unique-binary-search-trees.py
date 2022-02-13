class Solution:
    def numTrees(self, n: int) -> int:
        d = {}
        d[0] = 1
        d[1] = 1
        
        def dfs(n):
            if n in d:
                return d[n]
            
            s = 0
            for i in range(1,n+1):
                s += dfs(i-1)*dfs(n-i)
            
            d[n] = s
            return d[n]
        
        return dfs(n)
    