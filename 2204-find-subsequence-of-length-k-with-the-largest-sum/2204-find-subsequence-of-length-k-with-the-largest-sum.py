class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        k = len(nums) - k
        res = []
        while k > 0:
            nums.remove(min(nums))
            k -= 1
        nums

        return nums