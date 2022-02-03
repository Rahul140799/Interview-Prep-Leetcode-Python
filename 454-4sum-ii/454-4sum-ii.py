class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        
        d = {}
        
        for i in nums1:
            for j in nums2:
                curr = i+j
                if curr not in d:
                    d[curr] = 1
                else:
                    d[curr] += 1
        
        for k in nums3:
            for l in nums4:
                req = -(k+l)
                if req in d:
                    count += d[req]
                            
        return count