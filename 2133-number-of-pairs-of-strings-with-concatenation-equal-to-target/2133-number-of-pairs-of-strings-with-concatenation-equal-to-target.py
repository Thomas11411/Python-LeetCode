class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        from itertools import permutations
        return sum(nums[i] + nums[j] == target for i , j in permutations(range(len(nums)), 2))