class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def gcd(a,b):
            while b:
                a , b = b , a % b
            return a

        res = 0

        for i in range(len(nums)):
            cur = 0
            for j in range(i,len(nums)):
                cur = gcd(cur,nums[j])
                if cur == k:
                    res += 1
                if cur < k:
                    break
        return res