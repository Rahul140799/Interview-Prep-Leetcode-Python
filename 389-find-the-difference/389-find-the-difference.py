class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = {}
        for i in t:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        for i in s:
            if i in d:
                d[i] -= 1
                if d[i] == 0:
                    del d[i]
        
        for i in d:
            return i
            
            
            
        