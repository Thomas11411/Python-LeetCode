class Solution:
    def maxScore(self, nums: List[int]) -> int:
        import itertools

        nums.sort(reverse=True)
        return sum(n > 0 for n in itertools.accumulate(nums)) 