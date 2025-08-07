class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        tmp = set()
        res = 1
        nums = set(nums)

        for n in sorted(nums):
            if n in tmp:
                next
                
            cnt = 1
            tmp.add(n)
            
            while (n ** 2 in nums):
                n *= n
                tmp.add(n)
                cnt += 1
            
            res = max(res,cnt)

        return res if res > 1 else -1