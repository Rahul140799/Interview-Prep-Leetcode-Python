class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(temp):
            if len(temp) == len(nums) and temp not in res:
                res.append(temp[:])
            
            for i in range(len(nums)):
                if nums[i] not in visited:
                    temp.append(nums[i])
                    visited.add(nums[i])
                    dfs(temp)
                    temp.pop()
                    visited.remove(nums[i])
        
        visited = set()
        dfs([])
        return res