import itertools
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = 0
        for i in range(1,len(tiles) + 1):
            res += len(set(itertools.permutations(tiles, i)))
        return res