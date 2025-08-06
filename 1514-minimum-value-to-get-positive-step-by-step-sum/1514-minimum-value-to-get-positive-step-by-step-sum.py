class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        total = 0
        min_total = float("inf")
        for i in nums:
            total += i
            min_total = min(min_total, total)



        return 1 - min_total if min_total < 1 else 1