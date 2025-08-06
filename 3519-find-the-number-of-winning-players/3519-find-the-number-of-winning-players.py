class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        d = Counter(map(tuple, pick))
        return len({p for (p, _), c in d.items() if p < c})