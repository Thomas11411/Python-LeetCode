class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        return abs(sum(map(lambda x: sum(int(i) for i in str(x)), nums)) - sum(nums))