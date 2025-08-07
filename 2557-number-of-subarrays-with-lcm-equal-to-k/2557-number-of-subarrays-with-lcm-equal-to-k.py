class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        def gcd(a,b):
            while b:
                a , b = b , a % b
            return a

        def lcm(a,b):
            return a * b // gcd(a,b)

        res = 0

        for i in range(len(nums)):
            cur = nums[i]
            for j in range(i,len(nums)):
                cur = lcm(cur,nums[j])
                if cur == k:
                    res += 1
                if cur > k:
                    break

        return res