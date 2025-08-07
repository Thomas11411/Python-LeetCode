class Solution:
    def digitCount(self, num: str) -> bool:
        from collections import Counter

        d = Counter(num)

        for i in range(len(num)):
            if d[str(i)] != int(num[i]):
                return False
        return True