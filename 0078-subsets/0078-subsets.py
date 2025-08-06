class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        x = []
        k = len(nums)
        while k >=0:
            x += list(itertools.combinations(nums,k))
            k -= 1
        return x