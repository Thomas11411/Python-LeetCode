class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        res = [0] * len(queries)
        now , ii = 0 , 0

        for x , i in sorted((x, i) for i, x in enumerate(queries)):

            while ii < len(items) and items[ii][0] <= x:
                now = max(now,items[ii][1])
                ii += 1

            res[i] = now
            
        return res