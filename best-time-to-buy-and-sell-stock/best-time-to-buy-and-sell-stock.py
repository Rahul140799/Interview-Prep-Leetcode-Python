class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minimum = prices[0]
        maximum = prices[0]
        profit = 0
        
        for i in prices[1:]:
            if i < minimum:
                minimum = i
                maximum = i
            else:
                maximum = i
                
            profit = max(profit, maximum - minimum)
        
        return profit