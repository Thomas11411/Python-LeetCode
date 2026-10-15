class Solution:
    def countValidPrefixes(self, s: str) -> int:
        cnt = [0, 0]
        res = 0

        for i in s:
            if i == "1":
                cnt[1] += 1
            else:
                cnt[0] += 1
            res += (abs(cnt[1] - cnt[0]) <= 1)
        return res