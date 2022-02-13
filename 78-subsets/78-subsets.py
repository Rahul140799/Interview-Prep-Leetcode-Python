class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(idx,temp):
            if temp not in res:
                res.append(temp[:])
            
            for j in range(idx,len(nums)):
                if nums[j] not in visited:
                    temp.append(nums[j])
                    visited.add(nums[j])
                    dfs(j+1,temp)
                    temp.pop()
                    visited.remove(nums[j])
        
        visited = set()
        dfs(0,[])
        return res
    