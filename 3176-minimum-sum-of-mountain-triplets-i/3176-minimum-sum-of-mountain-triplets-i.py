class Solution:
    def minimumSum(self, nums: List[int]) -> int:

        n = len(nums)
        r = [0] * n
        l = [0] * n
        r[-1] = nums[-1]
        l[0] = nums[0]

        for i in range(1, n - 1):
            l[i] = min(l[i - 1],nums[i])
            
        for i in range(n - 2, 0, -1):
            r[i] = min(r[i + 1],nums[i])
            
        res = 10 ** 9 + 7
            
            
        for i in range(1, n - 1):
            if nums[i] > r[i] and nums[i] > l[i]:
                res = min(res, r[i] + l[i] + nums[i])

        return res if res != 10 ** 9 + 7 else -1
        