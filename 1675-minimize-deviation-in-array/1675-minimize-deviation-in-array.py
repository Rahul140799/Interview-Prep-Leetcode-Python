import heapq
import sys
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        mini = sys.maxsize
        ans = sys.maxsize
        
        for i in range(len(nums)):
            if nums[i]%2:
                nums[i] *= 2
            mini = min(mini, nums[i])
        
        for i in range(len(nums)):
            nums[i] *= -1
        
        heapq.heapify(nums)
        
        while not nums[0]%2:
            val = heapq.heappop(nums) * -1
            ans = min(ans, val-mini)
            new_value = val//2
            mini = min(mini, new_value)
            heapq.heappush(nums, new_value*-1)
            
        return min(ans, -1*nums[0]-mini)
        
        