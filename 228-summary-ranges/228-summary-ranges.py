class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        
        if not nums:
            return res
        
        i = 0
        j = 0
        
        while j < len(nums):
            if j+1 < len(nums) and nums[j]+1 != nums[j+1]:
                if i != j:
                    val = str(nums[i]) + '->' + str(nums[j])
                    res.append(val)
                else:
                    val = str(nums[i])
                    res.append(val)
                i = j+1
            j += 1
        
        if i == j-1:
            val = str(nums[i])
            res.append(val)
        else:
            val = str(nums[i]) + '->' + str(nums[j-1])
            res.append(val)
            
        return res
                