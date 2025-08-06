class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def prime(n):
            if n <= 1:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True

        res = []

        for i,v in enumerate(nums):
            if prime(v): res.append(i)
        
        return max(res) - min(res)