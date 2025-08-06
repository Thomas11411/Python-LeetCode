class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        return (min(x, y + 1) + min(x + 1, y) + z) * 2