class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        n = len(nums)
        pos_loc = []
        k = 0

        for i,v in enumerate(nums):
            if v > 0:
                k += 1
                pos_loc.append(i)

        k1 = sum(1 for i in pos_loc if i < k)

        return k - k1