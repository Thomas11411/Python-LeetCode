class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        res = -1
        nums1 = set(nums)

        for i in nums1:
            if - i in nums1:
                res = max(res,abs(i))

        return res