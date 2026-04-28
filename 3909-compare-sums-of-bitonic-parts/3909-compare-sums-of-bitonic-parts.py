class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        import numpy as np

        nums = np.array(nums)
        idx = np.argmax(nums)

        l = sum(nums[:idx + 1])
        r = sum(nums[idx:])

        if l > r:
            return 0
        elif l < r:
            return 1
        else:
            return -1