class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        from collections import defaultdict

        d = defaultdict(list)

        for e, t in access_times:
            d[e].append(int(t[:2]) * 60 + int(t[2:]))
            
        res = []
            
        for e in d:
            d[e].sort()
            
            for i, j in zip(d[e], d[e][2:]):
                if j - i < 60:
                    res.append(e)
                    break

        return res