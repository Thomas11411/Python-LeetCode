class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        l = [1]
        s = 0
        e = len(nums) - 1
        if len(nums) == 1: return True

        for i in range(1, len(nums)):
            l.append(l[-1] + ((nums[i] ^ nums[i - 1]) % 2 != 0))
            
        return (l[e] - l[s]) == (e - s)