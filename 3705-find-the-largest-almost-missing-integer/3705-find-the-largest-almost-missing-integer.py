class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        from collections import Counter

        if k == len(nums): return max(nums)

        d = Counter(nums)

        if k == 1: return max((num for num in d if d[num] == 1), default = -1)

        res = -1

        if d[nums[0]] == 1: res = nums[0]
        if d[nums[-1]] == 1: res = max(res, nums[-1])

        return res