class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        mn = float("inf")
        mx = float("-inf")
        n = len(nums)
        mn_vec = []

        for i in range(n - 1, -1, -1):
            mn = min(mn, nums[i])
            mn_vec.append(mn)

        mn_vec.reverse()

        for i in range(n):
            mx = max(mx, nums[i])
            if mx - mn_vec[i] <= k:
                return i
        return -1