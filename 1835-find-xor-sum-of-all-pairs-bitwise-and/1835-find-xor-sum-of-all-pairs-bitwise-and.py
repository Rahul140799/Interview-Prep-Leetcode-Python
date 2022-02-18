class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        s1 = 0
        for i in arr1:
            s1 ^= i
        
        s2 = 0
        for i in arr2:
            s2 ^= i
        
        return s1 & s2
            