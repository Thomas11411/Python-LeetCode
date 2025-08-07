class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"

        from collections import Counter

        d = Counter(ranks)

        if max(d.values()) >= 3:
            return "Three of a Kind"
        elif max(d.values()) == 2:
            return "Pair"
        else:
            return "High Card"