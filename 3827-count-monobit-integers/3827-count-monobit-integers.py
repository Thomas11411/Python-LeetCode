class Solution:
    def countMonobit(self, n: int) -> int:
        return n.bit_length() + (n.bit_length() == n.bit_count())