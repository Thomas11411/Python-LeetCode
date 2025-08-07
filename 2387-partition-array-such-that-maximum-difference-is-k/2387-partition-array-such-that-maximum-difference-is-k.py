class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        mn = nums[0]

        for i in nums:
            if i - mn > k:
                mn = i
                res += 1

        return res + 1