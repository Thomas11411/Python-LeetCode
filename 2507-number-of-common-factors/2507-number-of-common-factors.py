class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        ans = 0

        if max(a,b) % min(a,b) == 0:
            ans += 1

        for i in range(1,(min(a,b) // 2) + 1):
            if a % i == 0 and b % i == 0:
                ans += 1

        return ans