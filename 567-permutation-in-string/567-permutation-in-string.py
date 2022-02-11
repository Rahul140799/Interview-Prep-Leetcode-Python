class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        
        d1 = {}
        d2 = {}
        
        for i in s1:
            if i not in d1:
                d1[i] = 1
            else:
                d1[i] += 1
        
        i = 0
        j = 0
        
        while j < l2:
            
            if s2[j] not in d2:
                d2[s2[j]] = 1
            else:
                d2[s2[j]] += 1
                
            while i < j and sum(d2.values()) > l1:
                d2[s2[i]] -= 1
                if d2[s2[i]] == 0:
                    del d2[s2[i]]
                i += 1
            
            if d1 == d2:
                return True
            
            j += 1
            
        return False
            
            