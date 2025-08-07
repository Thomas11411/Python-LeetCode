class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        from collections import defaultdict

        d = defaultdict(list)

        res = 0

        for i in tasks:

            if i not in d:
                d[i].append(float("-inf"))
            res = max(d[i][-1] + space + 1,res + 1)

            d[i].append(res)

        return res