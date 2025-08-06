class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float("inf")
        nums = sorted(nums)
        for i in range(len(nums)-2):
            low = i + 1
            high = len(nums) - 1
            while low < high:
                sum_ = nums[i] + nums[low] + nums[high]

                if sum_ > target:
                    high -= 1
                elif sum_ < target:
                    low += 1
                else:
                    return target
                
                if diff > abs(sum_ - target):
                    diff = abs(sum_ - target)
                    res = sum_
        return res