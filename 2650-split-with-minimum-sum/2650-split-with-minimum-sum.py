class Solution:
    def splitNum(self, num: int) -> int:

        n = ''.join(sorted(str(num)))
        return int(n[::2]) + int(n[1::2])