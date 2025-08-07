class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        res = [-1] * len(nums)
        l ,sum_ ,size = 0 , 0 , 2 * k + 1

        for r in range(len(nums)):
            sum_ += nums[r]
            if (r - l + 1) == size:
                res[l + k] = sum_ // size
                sum_ -= nums[l]
                l += 1

        return res