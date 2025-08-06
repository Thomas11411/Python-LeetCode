class Solution:
    def stringHash(self, s: str, k: int) -> str:
        n = len(s)
        res = ''
        sum_ = 0

        for i, v in enumerate(s):
            sum_ += (ord(v) - 97)
            if (i + 1) % k == 0:
                res += chr(97 + (sum_ % 26)) 
                sum_ = 0

        return res