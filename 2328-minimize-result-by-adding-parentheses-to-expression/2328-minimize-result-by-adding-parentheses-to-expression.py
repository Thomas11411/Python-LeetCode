class Solution:
    def minimizeResult(self, expression: str) -> str:
        l , r = expression.split("+")
        res = float("inf")
        for i in range(len(l)):
            for j in range(1,len(r)+1):
                c = int(l[:i] or 1) * ( int(l[i:] or 0) + int(r[:j] or 0) ) * int(r[j:] or 1)

                if c < res:
                    res = c
                    x , y = i , j

        return l[:x] + "(" + l[x:] + "+" + r[:y] + ")" + r[y:]