class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        d = Counter(nums)

        left , right = 0 , len(nums)

        res = 0

        for _ , mid in d.items():
            right -= mid
            res += (left * mid * right)
            left += mid

        return res