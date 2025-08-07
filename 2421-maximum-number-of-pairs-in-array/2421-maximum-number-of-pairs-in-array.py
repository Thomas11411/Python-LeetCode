class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        from collections import Counter

        d = Counter(nums)

        res = [0,0]
        #d.values()
        for i in d.values():
            res[0] += (i // 2)
            res[1] += (i % 2)

        return res