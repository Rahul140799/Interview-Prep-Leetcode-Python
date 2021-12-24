class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        
        start = intervals[0][0]
        end = intervals[0][1]
        
        res = []
        
        for i in intervals[1:]:
            if i[0] <= end:
                end = max(end, i[1])
            else:
                res.append([start, end])
                start = i[0]
                end = i[1]
        res.append([start, end])
        return res
            