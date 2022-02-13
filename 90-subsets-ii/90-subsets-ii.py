class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(idx,temp):
            if temp not in res:
                res.append(temp[:])
                
            for j in range(idx,len(nums)):
                temp.append(nums[j])
                dfs(j+1,temp)
                temp.pop()
        
        nums.sort()
        dfs(0,[])
        return res