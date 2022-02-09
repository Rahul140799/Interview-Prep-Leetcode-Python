class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = 0
        d = {}
        
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        print(d)
        
        for i in d:
            if k > 0 and i+k in d:
                count += 1
            elif k == 0 and d[i] > 1:
                count += 1
                
        return count
    