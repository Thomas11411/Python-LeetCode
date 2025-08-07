class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        from collections import Counter

        return all(i % 2 == 0 for i in Counter(nums).values())