class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        import bisect
        nums.sort()
        res = 0

        for i in range(len(nums)):
            l = bisect.bisect_left(nums, lower - nums[i])
            r = bisect.bisect_right(nums, upper - nums[i])
            res += (r - l)

            if l <= i < r:
                res -= 1
            
        return res // 2