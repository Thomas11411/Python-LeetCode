class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        nums.sort()
        cur = sum(nums)
        n = len(nums)

        for i in range(n - 1, 1, -1):
            cur -= nums[i]
            if cur > nums[i]:
                return cur + nums[i]
                
        return -1