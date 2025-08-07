class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        e , o = 0 , 1

        for i in nums:
            if i > 0:
                res[e] = i
                e += 2
            else:
                res[o] = i
                o += 2

        return res