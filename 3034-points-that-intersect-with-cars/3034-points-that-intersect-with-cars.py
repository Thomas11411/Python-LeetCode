class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:

        res = [0] * (max(i[1] for i in nums) + 1)

        for i in nums:
            for j in range(i[0], i[1] + 1):
                res[j] = 1
                
        return sum(res)
                