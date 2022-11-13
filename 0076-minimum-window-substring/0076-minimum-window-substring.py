import sys
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mini = sys.maxsize
        d = {}
        
        for i in t:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        i = 0
        j = 0
        st = ""
        start = 0
        counter = len(t)
        
        while j < len(s):
            if s[j] in d:
                d[s[j]] -= 1
                if d[s[j]] >= 0:
                    counter -= 1
            
            while counter == 0:
                if s[i] in d:
                    d[s[i]] += 1
                    if d[s[i]] > 0:
                        counter += 1
                        window_size = j-i+1
                        if mini > window_size:
                            mini = window_size
                            start = i
                i += 1
                
            j += 1
            
        return "" if mini == sys.maxsize else s[start:start+mini] 
    