class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        d = [(0 , 0)]
        res = 0
        while d:
            pos , xor = d.pop()
            res += xor
            for i in range(pos,len(nums)):
                d.append((i + 1 , xor ^ nums[i]))

        return res