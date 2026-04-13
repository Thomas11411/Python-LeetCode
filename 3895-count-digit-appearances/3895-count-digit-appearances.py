class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        vec = ''.join(map(str,nums))
        return vec.count(str(digit))