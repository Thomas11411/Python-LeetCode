class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        from itertools import combinations
        res = 0
        for a,b,c,d in combinations(range(len(nums)),4):
            if nums[a] + nums[b] + nums[c] == nums[d]:
                res += 1

        return res