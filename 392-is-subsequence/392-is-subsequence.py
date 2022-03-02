class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        arr = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
        
        ls = len(s)
        lt = len(t)
        
        if not ls:
            return True
        
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1] == t[j-1]:
                    arr[i][j] = arr[i-1][j-1] + 1
                else:
                    arr[i][j] = max(arr[i-1][j], arr[i][j-1])
            
            
                if arr[ls][j] == ls:
                    return True
                
        return False
        
        
    