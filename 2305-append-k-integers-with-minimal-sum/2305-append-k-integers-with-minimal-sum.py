class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:

        nums.append(0)
        nums = sorted(set(nums))

        n = len(nums)
        res = 0

        for i in range(1,n):
            l = nums[i-1] + 1
            r = nums[i] - 1
            d = (r - l + 1)
            if d >= k:
                res += (2 * l + k - 1) * k / 2
                return int(res)

            res += (l + r) * d / 2
            k -= d

        if k > 0:
            l = nums[-1] + 1
            res += (2 * l + k - 1) * k / 2
            return int(res)