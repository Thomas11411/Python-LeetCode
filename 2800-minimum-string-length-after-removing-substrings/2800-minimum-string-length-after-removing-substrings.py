class Solution:
    def minLength(self, s: str) -> int:

        res = []

        for i in s:
            if res and (res[-1] + i == "AB" or res[-1] + i == "CD"):
                res.pop()
            else:
                res.append(i)
                
        return len(res)