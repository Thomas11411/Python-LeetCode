class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        res = set()

        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                res.add(tuple(nums[i:j]))

        return sum(1 for i in res if sum(j % p == 0 for j in i) <= k)