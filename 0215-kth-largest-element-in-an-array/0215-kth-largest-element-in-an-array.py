class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sort_nums = sorted(nums)
        final = sort_nums[-k]
        return final