class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        return ((n >> 1) & n).bit_count() == 1