class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        import sortedcontainers

        new = sortedcontainers.SortedList()
        res = []

        for i,v in enumerate(nums):
            new.add(v)
            if i >= k:
                new.remove(nums[i - k])
            if i >= k - 1:
                res.append(min(0, new[x - 1]))

        return res