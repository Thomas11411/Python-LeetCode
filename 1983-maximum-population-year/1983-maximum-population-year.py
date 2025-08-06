class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        from collections import defaultdict
        d = defaultdict(int)
        res = 2051
        count = 0
        for start,end in logs:
            for i in range(start,end):
                d[i] += 1
                if d[i] > count:
                    res = i
                    count = d[i]
                elif d[i] == count:
                    res = min(res,i)
        return res