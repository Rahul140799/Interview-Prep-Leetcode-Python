class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0],-x[1]))
        
        start = intervals[0][0]
        end = intervals[0][1]
        
        count = 0
        
        for i in intervals[1:]:
            if start <= i[0] and end >= i[1]:
                count += 1
            else:
                start = i[0]
                end = i[1]
                
        return len(intervals) - count
            