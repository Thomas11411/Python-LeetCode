class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:

        from collections import Counter

        logs.sort(key = lambda x: x[1])
        d = Counter()
        res = [0] * len(queries)
        i, j, used = 0, 0, 0

        for [v, id] in sorted([v, id] for id, v in enumerate(queries)):
            while i < len(logs) and logs[i][1] <= v:
                d[logs[i][0]] += 1
                used += (d[logs[i][0]] == 1)
                i += 1
            while j < i and logs[j][1] < v - x:
                d[logs[j][0]] -= 1
                used -= (d[logs[j][0]] == 0)
                j += 1
                
            res[id] = n - used

        return res