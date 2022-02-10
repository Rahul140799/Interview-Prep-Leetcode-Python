class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0:1}
        s = 0
        count = 0
        
        for i in range(len(nums)):
            s += nums[i]
            
            if s-k in d:
                count += d[s-k]
            
            if s not in d:
                d[s] = 1
            else:
                d[s] += 1
                
        return count
    