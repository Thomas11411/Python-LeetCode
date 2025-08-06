class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:

        res = 0
        happiness.sort(reverse = True)

        for i in range(k):
            res += max(0,happiness[i] - i)
            if max(0,happiness[i] - i) == 0:
                return res

        return res
        