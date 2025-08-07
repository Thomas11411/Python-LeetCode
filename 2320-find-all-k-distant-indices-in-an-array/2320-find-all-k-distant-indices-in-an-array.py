class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = set()

        r = -1
        for i in range(len(nums)):
            if nums[i] == key:
                r = i + k
            if i <= r:
                res.add(i)

        l = len(nums)
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == key:
                l = i - k
            if i >= l:
                res.add(i)

        return res