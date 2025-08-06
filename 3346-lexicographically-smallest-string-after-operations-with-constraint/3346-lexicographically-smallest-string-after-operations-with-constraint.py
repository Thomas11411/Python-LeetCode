class Solution:
    def getSmallestString(self, s: str, k: int) -> str:

        res = ""

        for ch in s:
            mp = min(ord(ch) - ord("a"), ord("z") - ord(ch) + 1)
            if mp <= k:
                k -= mp
                res += "a"
            else:
                res += chr(ord(ch) - k)
                k -= k

        return res
        