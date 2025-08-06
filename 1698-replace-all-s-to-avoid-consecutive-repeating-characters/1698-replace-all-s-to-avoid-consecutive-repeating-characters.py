class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)):

            if s[i] == "?":
                sample = list(range(26))
                if i > 0:
                    sample.remove(ord(s[i-1]) - ord("a"))
                if i < len(s) - 1 and s[i+1] != "?" and s[i+1] != s[i-1]:
                    sample.remove(ord(s[i+1]) - ord("a"))

                s[i] = chr(ord("a") + sample[0])
        return ''.join(s)