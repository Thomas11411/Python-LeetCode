class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        sample = set([i for i in range(1,k+1)])

        for j in range(len(nums)-1,-1,-1):
            sample -= {nums[j]}
            if not sample:
                return len(nums) - j

        return len(nums) - j

        