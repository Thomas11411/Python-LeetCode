class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict

        d = defaultdict(int)

        for w,l in matches:
            d[l] += 1
            d[w]

        ans = [[],[]]
        for p,l in d.items():
            if l == 0: ans[0].append(p)
            elif l == 1: ans[1].append(p)

        return map(sorted,ans)