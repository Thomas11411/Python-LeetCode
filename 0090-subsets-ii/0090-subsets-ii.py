import itertools
import numpy as np
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        k = len(nums)
        x = []
        while k > -1:
            x += list(itertools.combinations(nums,k))
            k -= 1
        x = list(np.unique(x))
        return x