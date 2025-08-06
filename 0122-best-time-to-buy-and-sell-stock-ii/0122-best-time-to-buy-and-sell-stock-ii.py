class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 10 ** 4
        res = 0
        for i in prices:
            if buy > i:
                buy = i
            elif buy < i:
                res += i - buy
                buy = i
        return res