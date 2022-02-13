class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def dfs(s, count, st):
            if count > 4:
                return 
            
            if count == 4 and len(s) == 0:
                res.append(st[:-1])
                return
            
            for i in range(1,len(s)+1):
                if s[:i] == '0' or (s[0]!='0' and 0 < int(s[:i]) < 256):
                    dfs(s[i:], count+1, st+s[:i]+'.')
        
        res = []
        dfs(s, 0, "")
        return res
        