class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_list = set(wordDict)
        d = {}
        
        def dfs(idx,s):
            if idx == len(s):
                return True
            
            if (idx,s) in d:
                return d[(idx,s)]
            
            d[(idx,s)] = False
            for i in range(idx,len(s)):
                new_word = s[idx:i+1]
                
                if new_word in word_list:
                    d[(idx,s)] = d[(idx,s)] or dfs(i+1, s)
                    if d[(idx,s)]:
                        return d[(idx,s)]
            return d[(idx,s)]
            
        return dfs(0,s)