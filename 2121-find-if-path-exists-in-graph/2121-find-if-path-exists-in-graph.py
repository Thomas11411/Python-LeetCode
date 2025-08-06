class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        from collections import defaultdict
        d = defaultdict(list)

        for i,j in edges:
            d[i].append(j)
            d[j].append(i)

        q = [start]
        visit = set()

        while q:
            now = q.pop()
            if now in visit:
                continue
            if now == end:
                return True
            
            visit.add(now)

            for i in d[now]:
                q.append(i)
                

        return False