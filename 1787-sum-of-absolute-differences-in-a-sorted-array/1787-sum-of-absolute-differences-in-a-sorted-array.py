class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        count = -1 * (len(nums)-1)
        before = sum(nums)
        after = 0
        res = []
        for i in nums:
            before -= i
            res.append(before - after + count * i)
            after += i
            count += 2
        return res