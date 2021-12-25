class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        if not time:
            return [i for i in range(len(security))]
        
        left = [1]
        right = [1]
        
        curr = 1
        for i in range(1,len(security)):
            if security[i-1] >= security[i]:
                curr += 1
            else:
                curr = 1
            left.append(curr)
        
        curr = 1
        for i in range(len(security)-2, -1, -1):
            if security[i] <= security[i+1]:
                curr += 1
            else:
                curr = 1
            right.append(curr)
        right.reverse()
        
        return [i for i in range(len(left)) if left[i] > time and right[i] > time]
                    
            