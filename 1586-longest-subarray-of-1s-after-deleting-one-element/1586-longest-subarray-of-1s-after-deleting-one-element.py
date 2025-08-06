class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero = []
        for i, v in enumerate(nums):
            if v == 0:
                zero.append(i)
        ans = 0
        if len(zero) == 1 or len(zero) == 0:
            ans = len(nums) -1
        for i , v in enumerate(zero):
            left = -1 if i == 0 else zero[i - 1]
            right = len(nums) if i == len(zero) - 1 else zero[i + 1]
            ans = max(ans , right - left - 2)
        return ans