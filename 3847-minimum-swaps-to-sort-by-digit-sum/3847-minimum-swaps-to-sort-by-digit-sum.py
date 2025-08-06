class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        digSum = lambda x: (sum(map(int, str(nums[x]))), nums[x])
        perm = sorted(range(n), key = digSum)
        res = 0

        for cur, tar in enumerate(perm):
            while cur != tar:
                perm[tar], tar = tar, perm[tar]
                res += 1

        return res