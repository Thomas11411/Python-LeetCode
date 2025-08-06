class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn , res = 10000 , 0
        for i in prices:
            mn = min(mn,i)
            res = max(res , i - mn)

        return res