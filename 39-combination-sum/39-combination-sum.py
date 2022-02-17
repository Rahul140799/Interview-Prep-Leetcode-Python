class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def recurse(idx,temp):
            if sum(temp) > target:
                return 
            
            if sum(temp) == target and temp not in res:
                res.append(temp[:])
                return
            
            for i in range(idx,len(candidates)):
                temp.append(candidates[i])
                recurse(i,temp)
                temp.pop()
        
        recurse(0,[])
        return res