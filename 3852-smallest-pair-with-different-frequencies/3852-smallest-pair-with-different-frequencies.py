class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        from collections import Counter

        d = Counter(sorted(nums))

        lcnt = 0
        lnum = float("-inf")

        for num, cnt in d.items():
            
            if lnum == float("-inf"):
                lnum = num
                lcnt = cnt
                
            if cnt != lcnt:
                return [lnum, num]

        return [-1, -1]

