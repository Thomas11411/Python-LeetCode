class Solution:
    def distinctAverages(self, nums: List[int]) -> int:

        from collections import deque

        nums.sort()
        nums = deque(nums)
        res = set()
        while nums:
            mx = nums.pop()
            mn = nums.popleft()
            res.add((mx + mn) / 2)

        return len(res)