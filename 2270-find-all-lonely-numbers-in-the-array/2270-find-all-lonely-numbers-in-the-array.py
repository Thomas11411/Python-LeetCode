class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        from collections import Counter
        c = Counter(nums)
        return [n for n in set(nums) if c[n] == 1 and c[n-1] == c[n+1] == 0]