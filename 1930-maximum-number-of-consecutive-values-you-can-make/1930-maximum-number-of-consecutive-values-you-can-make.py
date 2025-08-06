class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        curr = 0

        for c in coins:
            if c > curr + 1:
                break
            curr += c

        return curr + 1