class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            if i % 2 == 0: res |= i
        return res