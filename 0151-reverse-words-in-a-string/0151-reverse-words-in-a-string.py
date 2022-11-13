class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(' ')
        
        return ' '.join([i for i in arr[::-1] if i])