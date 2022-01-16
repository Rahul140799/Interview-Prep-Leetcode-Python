class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        
        if len(s)%k != 0:
            val = len(s)%k
            s += fill*(k-val)
        
        i = 0
        j = k
        
        res = []
        
        while j <= len(s):
            res.append(s[i:j])
            i = j
            j += k
        
        return res
            