class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        n = len(nums)
        mx = float('-inf')
        mn = float('inf')

        res = float('-inf')

        for j in range(m - 1, n):
            i = j - m + 1
            mx = max(mx, nums[i])
            mn = min(mn, nums[i])
            
            res = max(res, mx * nums[j], mn * nums[j])

        return res
        