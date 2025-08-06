class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:

        from collections import Counter

        d = Counter(moves)

        return abs(d["R"] - d["L"]) + d["_"]
        