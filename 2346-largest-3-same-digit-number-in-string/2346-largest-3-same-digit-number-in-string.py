class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""

        l , n = 0 , len(num) - 2

        while l < n:
            if num[l] == num[l + 1] == num[l + 2]:
                res = max(res,num[l])
                l += 3
            else:
                l += 1
        return res * 3