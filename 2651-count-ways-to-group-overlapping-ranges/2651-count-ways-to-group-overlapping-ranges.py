class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort()
        hi = -1
        cnt = 0

        for a,b in ranges:
            cnt += hi < a
            hi = max(hi,b)

        return pow(2, cnt, 10 ** 9 + 7)