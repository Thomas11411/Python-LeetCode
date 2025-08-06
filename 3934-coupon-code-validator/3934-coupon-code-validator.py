class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        from collections import defaultdict

        d = defaultdict(int, {"electronics":1, "grocery":2, "pharmacy":3, "restaurant":4})

        data = list(zip(code, businessLine, isActive))
        data.sort(key = lambda x: (d[x[1]], x[0]))

        res = []

        for c, b, a in data:
            if not c.replace('_', 'a').isalnum(): continue
            if d[b] == 0: continue
            if not a: continue
                
            res.append(c)

        return res