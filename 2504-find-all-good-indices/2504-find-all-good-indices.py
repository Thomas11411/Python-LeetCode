class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        
        if len(nums) < (2 * k + 1):
            return []


        dp1 = [1] * len(nums)
        dp2 = [1] * len(nums)

        for i in range(len(nums) - 2, k, -1):

            if nums[i + 1] - nums[i] >= 0:
                dp2[i] = dp2[i + 1] + 1

        res = []

        for i in range(1,len(nums) - k):

            if nums[i - 1] - nums[i] >= 0:
                dp1[i] = dp1[i - 1] + 1


            if i >= k and dp1[i - 1] - dp1[i - k] == (k - 1) and dp2[i + 1] - dp2[i + k] == (k - 1):

                res.append(i)

        return res