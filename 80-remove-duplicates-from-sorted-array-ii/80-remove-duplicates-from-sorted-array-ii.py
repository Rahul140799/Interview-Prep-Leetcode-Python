class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        count = 0
        
        while i < len(nums)-1:
            if nums[i] == nums[i+1] and count < 1:
                count += 1
            elif nums[i] == nums[i+1] and count >= 1:
                del nums[i+1]
                i -= 1
            else:
                count = 0
            i += 1
            
        return len(nums)