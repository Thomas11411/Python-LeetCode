class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        lst = [0] * 10
        res = 0
        mx = -9999

        for num in nums:
            dt = list(str(num))
            dt_mx, dt_mn = int(max(dt)), int(min(dt))
            dif = dt_mx - dt_mn
            lst[dif] += num
            if dif >= mx: 
                res = lst[dif]
                mx = dif
        return res