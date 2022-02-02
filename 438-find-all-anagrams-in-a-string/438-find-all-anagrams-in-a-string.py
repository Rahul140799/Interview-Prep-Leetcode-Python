class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d = {}
        for i in p:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        i = 0
        j = 0
        l = len(p)
        res = []
        temp = {}
        
        while j < len(s):
            
            while j < len(s) and sum(temp.values()) < sum(d.values()):
                if s[j] not in temp:
                    temp[s[j]] = 1
                else:
                    temp[s[j]] += 1
                j += 1
            
            j -= 1
            
            if temp == d:
                res.append(i)
            
            if s[i] in temp:
                temp[s[i]] -= 1
                if temp[s[i]] == 0:
                    del temp[s[i]]
                i += 1
            j += 1
        return res
            
            