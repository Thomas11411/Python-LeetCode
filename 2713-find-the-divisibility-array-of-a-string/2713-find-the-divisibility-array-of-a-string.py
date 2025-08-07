class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:

        res = []
        cur = 0

        for i in word:
            cur = 10 * cur + int(i)
            cur %= m
            if cur == 0: res.append(1)
            else: res.append(0)

        return res