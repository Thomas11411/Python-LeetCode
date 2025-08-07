class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        from collections import Counter

        cnt1 , cnt2 = map(Counter,(s,target))

        return min(cnt1[i] // cnt2[i] for i in set(target))