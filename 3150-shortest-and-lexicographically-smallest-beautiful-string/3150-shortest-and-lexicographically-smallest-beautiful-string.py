class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        ans = ""
        i = 0
        j = 0
        c = 0

        while j < n:
            if s[j] == '1':
                c += 1
            if c == k:
                while i < n and c == k:
                    s1 = s[i:j + 1]
                    if not ans or len(s1) < len(ans):
                        ans = s1
                    elif len(s1) == len(ans):
                        ans = min(ans, s1)
                    if s[i] == '1':
                        c -= 1
                    i += 1
            j += 1
        return ans