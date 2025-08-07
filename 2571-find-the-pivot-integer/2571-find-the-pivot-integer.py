class Solution:
    def pivotInteger(self, n: int) -> int:

        l = 0
        r = sum(range(1,n+1))

        for i in range(1,n+1):
            l += i
            if l == r:
                return i
            r -= i

        return -1