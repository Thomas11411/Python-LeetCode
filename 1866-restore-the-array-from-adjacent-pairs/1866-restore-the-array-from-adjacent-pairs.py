class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        from collections import defaultdict
        d = defaultdict(list)

        for i,j in adjacentPairs:
            d[i].append(j)
            d[j].append(i)

        s_e = []
        for i,v in d.items():
            if len(v) == 1:
                s_e.append(i)

        s , e = s_e[0] , s_e[1]
        res = [s]
        seen = {s}

        while s != e:
            for i in d[s]:
                if i not in seen:
                    res.append(i)
                    seen.add(i)
                    s = i

        return res