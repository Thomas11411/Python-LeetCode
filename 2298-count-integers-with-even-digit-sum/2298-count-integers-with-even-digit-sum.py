class Solution:
    def countEven(self, num: int) -> int:
        res = 0
        for i in range(1,num+1):
            sm = sum(map(int,str(i)))
            if sm % 2 == 0:
                res += 1

        return res