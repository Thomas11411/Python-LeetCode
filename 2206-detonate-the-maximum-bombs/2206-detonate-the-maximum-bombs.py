class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        g = [[] for _ in range(len(bombs))]
        for i,(xi,yi,ri) in enumerate(bombs):
            for j,(xj,yj,rj) in enumerate(bombs):
                if j > i:
                    dist = (xi - xj) ** 2 + (yi - yj) ** 2
                    if ri ** 2 >= dist: g[i].append(j)
                    if rj ** 2 >= dist: g[j].append(i)


        def fn(x):
            ans = 1
            seen = {x}
            stack = [x]

            while stack:
                u = stack.pop()
                for v in g[u]:
                    if v not in seen:
                        ans += 1
                        stack.append(v)
                        seen.add(v)

            return ans

        return max(fn(i) for i in range(len(bombs)))
