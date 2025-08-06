class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:

        from sortedcontainers import SortedList

        d = SortedList([])
        res = 0
        l = 0
        n = len(nums)

        for r in range(n):
            d.add(nums[r])
            
            while l < r and d[-1] - d[0] > 2:
                d.remove(nums[l])
                l += 1
            
            res += (r - l + 1)

        return res