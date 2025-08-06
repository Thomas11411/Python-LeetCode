class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bin_num = "{0:b}".format(n)
        for i in range(0,len(bin_num) - 1):
            if bin_num[i] == bin_num[i + 1]:
                return False
        return True