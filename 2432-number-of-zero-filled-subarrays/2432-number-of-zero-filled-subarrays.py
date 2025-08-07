class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res , cnt = 0 , 0

        for i in nums:
            if i == 0:
                cnt += 1
                res += cnt
            else:
                cnt = 0

        return res