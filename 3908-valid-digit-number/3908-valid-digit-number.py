class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        from collections import Counter
        str_n = str(n)
        str_x = str(x)
        return Counter(str_n)[str_x] != 0 and str_n[0] != str_x