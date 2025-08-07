class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        from collections import defaultdict

        d = defaultdict(list)

        for i, ch in enumerate(s):

            posi = ord(ch) - ord('a')
            if(d[posi]):
                if distance[posi] != (i - d[posi][0] - 1):
                    return False
            else:
                d[posi].append(i)

        return True