class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        from collections import Counter

        d = Counter(nums[:k])
        size = len(d)
        cur = sum(nums[:k])
        res = cur if size == k else 0

        for i in range(k,len(nums)):
            old , new = nums[i-k] , nums[i]
            d[old] -= 1
            
            if d[old] == 0:
                d.pop(old)
                size -= 1
            
            d[new] += 1
            
            if d[new] == 1:
                size += 1
                
            cur += (nums[i] - nums[i-k])
            
            if size == k:
                res = max(res,cur)

        return res