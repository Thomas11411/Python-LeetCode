class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = [1] * len(nums)
        left = 1
        for i in range(1,len(nums)):
            left *= nums[i - 1]
            prod[i] *= left
        right = 1
        for j in range(len(nums)-2,-1,-1):
            right *= nums[j + 1]
            prod[j] *= right
        return prod
        