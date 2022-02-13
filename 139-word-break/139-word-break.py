class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_list = set(wordDict)
        d = {}
        
        def dfs(idx):
            if idx == len(s):
                return True
            
            if idx in d:
                return d[idx]
            
            d[idx] = False
            for i in range(idx,len(s)):
                new_word = s[idx:i+1]
                
                if new_word in word_list:
                    d[idx] = d[idx] or dfs(i+1)
                    if d[idx]:
                        return d[idx]
                    
            return d[idx]
            
        return dfs(0)