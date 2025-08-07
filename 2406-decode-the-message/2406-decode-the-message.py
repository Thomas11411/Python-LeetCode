class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        from collections import defaultdict

        d = defaultdict(str)
        cnt = 0
        d[" "] = " "

        for i in key:
            if i not in d:
                d[i] = chr(97 + cnt)
                cnt += 1


        res = ""

        for i in message:
            res += d[i]

        return res