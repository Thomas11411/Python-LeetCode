class Solution:
    def numSub(self, s: str) -> int:
        count = 0
        now = 0
        m = int(1e9+7)
        for i in s:
            if i == "1":
                now += 1
            else:
                now = 0
            count = (count + now) % m
        return count