class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = [True] * len(l)
        for i in range(len(l)):
            sub = sorted(nums[l[i]:(r[i]+1)])
            if len(sub) <= 2:
                pass
            diff = sub[1] - sub[0]

            for j in range(2,len(sub)):
                if diff != (sub[j] - sub[j-1]):
                    res[i] = False
                    break
        return res