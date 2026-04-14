class Solution:
    def scoreBalance(self, s: str) -> bool:
        l = 0
        r = sum(map(lambda x: ord(x) - 96, s))

        for ch in s:
            val = ord(ch) - 96
            l += val
            r -= val
            if l == r: return True
        return False