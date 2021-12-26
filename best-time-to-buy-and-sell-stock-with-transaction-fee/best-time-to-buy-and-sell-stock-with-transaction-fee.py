class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        d = {}
        
        def dp(i, state):
            if i >= len(prices):
                return 0
            
            if (i, state) in d:
                return d[(i,state)]
            
            hold = dp(i+1, state)
            
            buy = 0
            sell = 0
            
            if state:
                sell = dp(i+1, 0) + prices[i] - fee
            else:
                buy = dp(i+1, 1) - prices[i]
            
            d[(i,state)] = max(buy, sell, hold)
            return d[(i,state)]
        
        return dp(0,0)