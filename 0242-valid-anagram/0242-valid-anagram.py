class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        char_cnt = 0
        
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
            char_cnt += 1
        
        for i in t:
            if i in d:
                d[i] -= 1
                if d[i] < 0:
                    return False
                char_cnt -= 1
            else:
                return False
        
        return not char_cnt
    