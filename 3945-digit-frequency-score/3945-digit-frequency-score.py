class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        return sum(map(int, list(str(n))))