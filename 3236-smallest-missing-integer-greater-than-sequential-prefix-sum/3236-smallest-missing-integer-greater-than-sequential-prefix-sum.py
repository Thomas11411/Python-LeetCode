class Solution:
    def missingInteger(self, nums: List[int]) -> int:
                
        sum_ = nums[0]
        n = len(nums)

        for i in range(1,n):
            if nums[i] == nums[i - 1] + 1:
                sum_ += nums[i]
            else:
                break
                
        nums.sort()

        for i in range(n):
            if nums[i] == sum_:
                sum_ += 1

        return sum_