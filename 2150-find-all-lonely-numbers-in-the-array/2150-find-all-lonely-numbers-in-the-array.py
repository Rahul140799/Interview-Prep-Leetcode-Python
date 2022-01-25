class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [nums[0]]
        
        if len(nums) == 2:
            if abs(nums[0] - nums[1]) == 1 or nums[0] == nums[1]:
                return []
            else:
                return [nums[0], nums[1]]
        
        nums.sort()
        
        res = []
        
        if nums[0] == nums[1] or nums[0]+1 == nums[1] or nums[1]-1 == nums[0]:
            pass
        else:
            res.append(nums[0])
        
        for i in range(1,len(nums)-1):
            if nums[i]+1 == nums[i+1] or nums[i]-1 == nums[i-1] or nums[i] == nums[i+1] or nums[i] == nums[i-1]:
                continue
            else:
                res.append(nums[i])
        
        if nums[i] == nums[i+1] or nums[i]+1 == nums[i+1] or nums[i+1]-1 == nums[i] or nums[i] == nums[i+1]:
            pass
        else:
            res.append(nums[i+1])
            
        return res
            