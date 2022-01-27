class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        num = str(x)
        
        return True if num == num[::-1] else False
        