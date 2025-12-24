class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        res = []
        for i in s:
            if res and res[-1] != i:
                res.pop()
            else:
                res.append(i)
        return len(res)