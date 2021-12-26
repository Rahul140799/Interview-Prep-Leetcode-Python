class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        d = {}
        
        def dp(i, transactions, state):
            
            if i == len(prices) or transactions == 0:
                return 0
            
            if (i, transactions, state) in d:
                return d[(i, transactions, state)]
            
            hold = dp(i+1, transactions, state)
            
            sell = 0
            buy = 0
            
            if state:
                sell = dp(i+1, transactions-1, 0) + prices[i]
            else:
                buy = dp(i+1, transactions, 1) - prices[i]
            
            d[(i, transactions, state)] = max(buy, hold, sell)
            return d[(i, transactions, state)]
        
        return dp(0,k,0)