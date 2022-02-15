class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        l = len(s)
        
        i = 0
        j = 0
        
        seen = set()
        count = 0
        
        while j < len(s):
            while i < j and s[j] in seen:
                seen.remove(s[i])
                i += 1
                
            seen.add(s[j])
            
            if len(seen) == k:
                count += 1
                seen.remove(s[i])
                i += 1
            
            j += 1
            
        return count
                    
                
            