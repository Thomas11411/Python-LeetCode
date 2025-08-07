class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        scores = [- sum(n % d == 0 for n in nums) for d in divisors]
        return sorted(zip(scores,divisors))[0][1]