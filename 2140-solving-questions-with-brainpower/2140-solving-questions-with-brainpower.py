class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        d = {}
        
        def dp(i):
            if i >= len(questions):
                return 0
            
            if i in d:
                return d[i]
            
            solve = questions[i][0] + dp(i+1+questions[i][1])
            not_solve = 0 + dp(i+1)
            
            d[i] = max(solve,  not_solve)
            
            return d[i]
        
        return dp(0)