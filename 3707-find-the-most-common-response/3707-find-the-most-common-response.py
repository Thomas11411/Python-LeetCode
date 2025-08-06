class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        from collections import Counter

        d = Counter()

        for i in responses:
            for ii in set(i):
                d[ii] += 1

        max_val = max(d.values())
        all_key = d.keys()
        return min(w for w in all_key if d[w] == max_val)