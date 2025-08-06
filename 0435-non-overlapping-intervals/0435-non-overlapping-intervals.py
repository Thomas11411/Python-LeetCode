class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals = sorted(intervals, key = lambda x: x[1])
        curr = - float('inf')
        count = 0
        for i in range(len(intervals)):
            if intervals[i][0] >= curr:
                curr = intervals[i][1]
                count += 1
        return len(intervals) - count