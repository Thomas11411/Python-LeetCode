class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []

        def f(i, s):
            if i == n:
                res.append(s)
                return res
            if s[-1] == "0":
                f(i+1, s + "1")
            else:
                f(i+1, s + "0")
                f(i+1, s + "1")
            
        f(1, "0")
        f(1, "1")
        return res