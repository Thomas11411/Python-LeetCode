class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        return [sum(map(lambda x: x < i, nums)) for i in nums]