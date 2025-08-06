class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = ['a'] * n
        i = n - 1
        k -= n

        while i >= 0 and k > 0:
            res[i] = chr(ord('a') + min(k,25))
            k -= min(k,25)
            i -= 1

        return ''.join(res)