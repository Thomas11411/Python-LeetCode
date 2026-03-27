class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        one = t.count("1")
        zero = len(s) - one
        res = ""

        for i in s:
            if (i == "1" and zero > 0) or (i == "0" and one > 0):
                res += "1"
                zero -= (i == "1")
                one -= (i == "0")
            else:
                res += "0"
                zero -= (i == "0")
                one -= (i == "1")
        return res