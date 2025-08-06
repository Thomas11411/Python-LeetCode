class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:

        nums = set(nums)

        for From, To in zip(moveFrom, moveTo):
            nums.remove(From)
            nums.add(To)

        return sorted(nums)