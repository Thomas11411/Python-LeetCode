class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        n = len(nums)
        odd = sum(1 for i in nums if i % 2 == 1)
        even = n - odd
        res = []

        for i in nums:
            if i % 2 == 1:
                res.append(even)
                odd -= 1
            else:
                res.append(odd)
                even -= 1
        return res