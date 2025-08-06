class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        res = 0
        if m > k: res += (m - k) * k
        if n > k: res += (n - k) * k
        return res