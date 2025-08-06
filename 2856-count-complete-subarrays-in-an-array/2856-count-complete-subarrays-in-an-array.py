class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:

        from collections import Counter

        i = 0
        res = 0
        n = len(nums)
        k = len(set(nums))
        d = Counter()

        for j in range(n):
            d[nums[j]] += 1
            while len(d) == k:
                d[nums[i]] -= 1
                if d[nums[i]] == 0:
                    del d[nums[i]]
                    
                i += 1
                
            res += i

        return res