class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x : x[0])
        res = [intervals.pop(0)]
        while intervals:
            now = intervals.pop(0)
            if res[len(res) - 1][1] < now[1]:
                res.append(now)
                
        return len(res)