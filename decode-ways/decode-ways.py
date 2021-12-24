class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [-1 for _ in range(len(s))]
        
        def decode_ways(idx):
            if idx == l:
                return 1
            
            if dp[idx] != -1:
                return dp[idx]
            
            one = 0
            two = 0
            
            if 1 <= int(s[idx]) <= 9:
                one = decode_ways(idx+1)
            if 10 <= int(s[idx:idx+2]) <= 26:
                two = decode_ways(idx+2)
            
            dp[idx] = one + two
            return dp[idx]
        
        l = len(s)
        return decode_ways(0)