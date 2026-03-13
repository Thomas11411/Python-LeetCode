class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        from collections import Counter
        d = Counter(sorted(bulbs))
        return [i for i, v in d.items() if v % 2 == 1]