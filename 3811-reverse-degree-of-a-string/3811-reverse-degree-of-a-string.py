class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum((i + 1) * (ord("z") - ord(v) + 1) for i, v in enumerate(s))