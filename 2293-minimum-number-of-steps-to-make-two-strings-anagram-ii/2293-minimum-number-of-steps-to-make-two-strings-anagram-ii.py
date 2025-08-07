class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt = [0] * 26

        for i in s:
            cnt[ord(i) - ord('a')] += 1

        for i in t:
            cnt[ord(i) - ord('a')] -= 1

        return sum(map(abs,cnt))