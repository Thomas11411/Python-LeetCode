class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        from collections import Counter
        n = len(nums)
        res = []
        for i in range(n - k + 1):
            d = Counter(nums[i:(i + k)])
            res.append(sum(c * v for c, v in sorted(d.items(), key = lambda x: (x[1], x[0]), reverse = True)[:x]))

        return res