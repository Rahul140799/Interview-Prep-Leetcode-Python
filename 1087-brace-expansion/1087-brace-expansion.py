class Solution:
    def expand(self, s: str) -> List[str]:
        res = []
        
        def dfs(s, idx, word):
            if idx == len(s):
                res.append(word)
                return
            else:
                if s[idx] == '{':
                    j = idx+1
                    while s[j] != '}':
                        j += 1
                    within_braces = s[idx+1:j]
                    for val in within_braces.split(','):
                        dfs(s, j+1, word+val)
                else:
                    dfs(s, idx+1, word+s[idx])
        
        dfs(s, 0, "")
        return sorted(res)            
                    