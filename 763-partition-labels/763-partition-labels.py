class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for i,val in enumerate(s):
            d[val] = i
        print(d)
        
        res = [0]
        maxi = 0
        hold = 0
        
        for i,val in enumerate(s):
            maxi = max(maxi, d[val])
            if maxi == i:
                res.append(i-hold+1)
                hold = i + 1
                
        return res[1:]
    