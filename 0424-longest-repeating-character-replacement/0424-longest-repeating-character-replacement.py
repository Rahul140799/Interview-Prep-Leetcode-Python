import sys
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        maxi = -sys.maxsize
        ans = 0
        
        i = 0
        j = 0
        
        while j < len(s):
            if s[j] not in d:
                d[s[j]] = 1
            else:
                d[s[j]] += 1
            maxi = max(maxi, d[s[j]])
            
            window_size = j-i+1
            
            if window_size - maxi <= k:
                ans = max(ans, window_size)
            else:
                while i < j and window_size - maxi > k:
                    if d[s[i]] > 0:
                        d[s[i]] -= 1
                        maxi = max(d.values())
                    i += 1
                    window_size = j-i+1
            j += 1
        return ans
            