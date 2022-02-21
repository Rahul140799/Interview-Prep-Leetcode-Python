class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        req = n//3
        
        d = {}
        visited = set()
        arr = []
        
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
            
            if d[i] > req and i not in visited:
                visited.add(i)
                arr.append(i)
        return arr
        