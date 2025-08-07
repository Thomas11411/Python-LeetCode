class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict

        d = defaultdict(list)
        for i,j in edges:
            d[i].append(j)
            d[j].append(i)

        visit = set()

        def dfs(node):
            if node in visit:
                return 0

            visit.add(node)
            res = 1

            for n in d[node]:
                res += dfs(n)

            return res


        c = []

        for i in range(n):
            temp = dfs(i)
            if temp != 0:
                c.append(temp)

        res = 0

        for i in c:
            res += (n - i) * i

        return res // 2