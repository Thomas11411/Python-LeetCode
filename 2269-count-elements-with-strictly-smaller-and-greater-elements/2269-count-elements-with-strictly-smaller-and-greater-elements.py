class Solution:
    def countElements(self, nums: List[int]) -> int:
        mx = max(nums)
        mn = min(nums)
        return sum(mn < i < mx for i in nums)