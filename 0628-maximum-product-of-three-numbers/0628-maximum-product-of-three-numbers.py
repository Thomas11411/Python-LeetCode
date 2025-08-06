class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        sort_nums = sorted(nums,reverse=True)
        max_nums = max(sort_nums[0] * sort_nums[1] * sort_nums[2],sort_nums[0] * sort_nums[-1] * sort_nums[-2])
        return max_nums