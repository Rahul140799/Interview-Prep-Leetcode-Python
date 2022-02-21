class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)//2
        d = {}
        
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
                
            if d[i] > n:
                return i
                
        