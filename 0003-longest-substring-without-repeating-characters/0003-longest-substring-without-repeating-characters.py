import sys
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = sys.maxsize * -1
        i = 0
        j = 0
        d = {}
        
        while j < len(s):
            if s[j] not in d:
                d[s[j]] = 1
            else:
                d[s[j]] += 1
            
            while i < j and d[s[j]] > 1:
                d[s[i]] -= 1
                i += 1
            
            l = max(l, j-i+1)
            j += 1
            
        return len(s) if l == sys.maxsize * -1 else l
        