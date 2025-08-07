class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def is_prime(n):
            if n == 1: return False
            i = 2
            while i ** 2 <= n:
                if n % i != 0:
                    i += 1
                else:
                    return False
            return True

        n = len(nums)

        res = 0

        for i in range(n):
            if is_prime(nums[i][i]): res = max(res,nums[i][i])
            if is_prime(nums[i][n - i - 1]): res = max(res,nums[i][n - i - 1])

        return res