class Solution:
    def integerBreak(self, n: int) -> int:
        import sys
        
        d = {}
        
        def dp(n):
            if n == 2:
                return 1
            if n < 2:
                return 0
            
            if n in d:
                return d[n]
            
            maximum = -sys.maxsize
            for i in range(1,n):
                maximum = max(maximum, i*dp(n-i), i*(n-i))
                
            d[n] = maximum
            return d[n]
        
        return dp(n)