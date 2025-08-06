class Solution:
    def splitArray(self, nums: List[int]) -> int:
        allsm, n = sum(nums), len(nums)

        for i in range(2, n):
            if nums[i] == 0: continue
            for j in range(i * i, n, i): nums[j] = 0
                
        partsm = sum(nums[2:])

        return abs(partsm - (allsm - partsm))