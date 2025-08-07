class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        from collections import Counter

        d = Counter(nums)
        cnt = 0
        res = float("inf")

        for i,v in d.items():

            if i % 2 == 0:
                if v > cnt:
                    res , cnt = i , v
                elif v == cnt:
                    res = min(res,i)

        return res if cnt > 0 else -1