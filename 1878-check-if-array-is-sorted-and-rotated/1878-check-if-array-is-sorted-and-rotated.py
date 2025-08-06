class Solution:
    def check(self, nums: List[int]) -> bool:
        cut = len(nums)
        sort_nums = sorted(nums)
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                cut = i
                break
        return nums[cut+1:] + nums[:cut+1] == sort_nums