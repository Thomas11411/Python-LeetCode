class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:

        res = []
        nums.sort()
        n = len(nums)

        for i in range(0, n, 3):
            a, b, c = nums[i:i+3]
            if c - a > k:
                return []

            res.append([a, b, c])

        return res
        