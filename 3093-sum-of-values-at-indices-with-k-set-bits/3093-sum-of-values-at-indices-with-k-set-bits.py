class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:

        n = len(nums)

        return sum(nums[i] for i in range(n) if bin(i).count('1') == k)
        