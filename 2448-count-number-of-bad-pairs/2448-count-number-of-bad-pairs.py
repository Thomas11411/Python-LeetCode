class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        from collections import defaultdict

        d = defaultdict(int)

        for i in range(len(nums)):
            d[i - nums[i]] += 1

        return len(nums) * (len(nums) - 1) // 2 - sum(i * (i - 1) // 2 for i in d.values())