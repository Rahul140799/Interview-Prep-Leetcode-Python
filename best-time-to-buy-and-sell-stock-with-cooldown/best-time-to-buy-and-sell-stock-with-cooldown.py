class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        d = {}
        
        def dp(i, state):
            if i >= len(prices):
                return 0
            
            if (i, state) in d:
                return d[(i, state)]
            
            hold = dp(i+1, state)
            
            sell = 0
            buy = 0
            
            if state:
                sell = dp(i+2, 0) + prices[i]
            else:
                buy = dp(i+1, 1) - prices[i]
            
            d[(i, state)] = max(buy, sell, hold)
            return d[(i, state)]
        
        return dp(0,0)
