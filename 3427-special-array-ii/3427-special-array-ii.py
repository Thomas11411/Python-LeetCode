class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        l = [0]

        for i in range(1, len(nums)):
            l.append(l[-1] + ((nums[i] ^ nums[i - 1]) % 2 != 0))
            
        return [(l[e] - l[s]) == (e - s) for s, e in queries]
        