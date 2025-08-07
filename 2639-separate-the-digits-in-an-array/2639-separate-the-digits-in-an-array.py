class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [int(i) for j in nums for i in str(j)]