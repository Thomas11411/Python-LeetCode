class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
                
        d = dict()

        for i,v in enumerate(s): d[v] = i

        res = 0

        for i,v in enumerate(t): res += abs(i - d[v])

        return res