class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.upper() == word:
            return True
        
        if word.lower() == word:
            return True
        
        for i,val in enumerate(word):
            if i > 0 and val.upper() == val:
                return False
        return True
        