class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums1 = [i for i in range(1,len(nums)+1)]
        return set(nums1) - set(nums)