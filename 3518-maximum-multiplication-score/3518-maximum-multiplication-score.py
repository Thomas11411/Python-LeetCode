class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        @cache
        def f(i,j):
            if i == len(a):
                return 0
            if j == len(b):
                return float("-inf")
            
            return max(
                f(i + 1, j + 1) + a[i] * b[j],
                f(i, j + 1)
            )

        return f(0,0)