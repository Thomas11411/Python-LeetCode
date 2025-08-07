class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        from itertools import combinations
        return sum(abs(x - y) == k for x,y in combinations(nums, 2))